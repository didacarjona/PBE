'''Codi en Python del puzzle 2 LCD. S'ha dissenyat tenint en compte els següents aspectes:
1. L'usuari pot escriure més de 4 línies. LCD només en té 4.
2. Es pot escriure varies línies sense "\n", cosa que el text buffer no reconeix.
3. Que no estigui connectada l'LCD quan s'arranqui el programa o durant l'execució

M'he anticipat a l'usuari solventat aquests problemes

També té una petita modificació en CSS, tot i que el puzzle per la LCD no té molt a oferir
en quant estilitzat CSS.'''

import gi
import textwrap
from LCD_PBE import I2C_LCD_driver

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):
	def __init__(self):
        
		super().__init__(title="PBE-Puzzle 2 - Didac Arjona")
		self.not_connected = False
		self.set_resizable(False)
		try:
			self.mylcd = I2C_LCD_driver.lcd()
			
			self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
			self.add(self.vbox)
			
			self.button1 = Gtk.Button(label="Display")
			self.button1.connect("clicked", self.display_clicked, self.mylcd)
			self.create_textview()
			self.vbox.pack_start(self.button1, True, True, 0)
			
			css = "stylish.css"
			css_provider = Gtk.CssProvider()
			css_provider.load_from_path(css)
			context = Gtk.StyleContext()
			screen = Gdk.Screen.get_default()
			context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

		except OSError:
			self.lcd_not_connected(self)
			self.not_connected = True
			
				
	def get_not_connected(self):
		return self.not_connected
			
	def lcd_not_connected(self, widget):
		dialog = Gtk.MessageDialog(
			transient_for=self,
			flags=0,
			message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Pantalla LCD no trobada",
        )
		dialog.format_secondary_text(
            "No s'ha pogut trobar la pantalla LCD. Comprova que estigui ben connectada i torna-ho a intentar."
        )
		dialog.run()
		dialog.destroy()
		
		
	def check_lcd_max_lines_and_fix(self, text):
		l = len(text)
		if l > 4:
			for i in range(4,l):
				text.pop(4)
		return text
				
	def adapt_to_lcd(self, button):
		text = self.textbuffer.get_text(self.textbuffer.get_start_iter(),self.textbuffer.get_end_iter(),-1).splitlines()
		text2 = []
		for i in text:
			if i != "":
				if len(i) > 20:
					count = 0
					while(len(i) - count > 20):
						text3 = ""
						for j in range(count, count+20):
							text3 = text3 + i[j]
						count = count + 20
						text2.append(text3)
					if count != len(i):
						text3 = ""
						for j in range(count, len(i)):
							text3 = text3 + i[j]
						text2.append(text3)
				else:
					text2.append(i) 
			else:
				text2.append("")
		text2 = self.check_lcd_max_lines_and_fix(text2)
		return text2

	def display_clicked(self, button, mylcd):
		try:
			mylcd.lcd_clear()
			text2 = self.adapt_to_lcd(self)
			mylcd.write_text_multiline(text2)
		except OSError:
			self.lcd_not_connected(self)
			self.destroy()
		
	def create_textview(self):
		self.textview = Gtk.TextView()
		self.textview.set_size_request(205, 80)
		self.textview.set_monospace(True)
		self.textview.set_wrap_mode(Gtk.WrapMode.CHAR)
		self.textbuffer = self.textview.get_buffer()
		self.vbox.pack_start(self.textview, True, True, 0)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

if win.get_not_connected() == False:
	Gtk.main()
