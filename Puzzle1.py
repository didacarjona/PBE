import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.ask_text_multiline()
