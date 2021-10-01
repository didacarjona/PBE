
# S'ha modificat la llibreria per tal d'afegir el mètode write_text_multiline() i poder reutilitzar el codi a codis posteriors.
# package LCD_PBE instalat de manera general

from LCD_PBE import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()


print("Introdueix un text. Per canviar de linea prem enter. Per acabar fes ctrl+D: ")
contents = []
while True:
   try:
       line = input()
   except EOFError:
       break
   contents.append(line)

mylcd.write_text_multiline(contents)

