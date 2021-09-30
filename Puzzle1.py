
// S'ha modificat la llibreria per tal d'afegir el mètode ask_text_multiline() i poder reutilitzar el codi a codis posteriors.


import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.ask_text_multiline()
