#https://docs.micropython.org/en/latest/esp32/quickref.html#uart-serial-bus
# https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299
from time import sleep
from machine import UART
import sys
uart1 = UART(1, baudrate=9600, tx=16, rx=17)

# STARTBYTE, VER, Len, CMD, FEEDBACK, PARA1, PARA2, PARA3, PARA4, CHECKSUM, ENDBYTE
play = bytes([0x7E, 0xFF, 0x06, 0x0D, 0x00, 0x00, 0x01, 0xFE, 0xED, 0xEF])
pause = bytes([0x7E, 0xFF, 0x06, 0x0E, 0x00, 0x00, 0x00, 0xFE, 0xED, 0xEF])

volume10 = bytes([0x7E, 0xFF, 0x06, 0x06, 0x00, 0x00, 0x10, 0xFE, 0xE5, 0xEF])
volume15 = bytes([0x7E, 0xFF, 0x06, 0x06, 0x00, 0x00, 0x15, 0xFE, 0xE0, 0xEF])
volume20 = bytes([0x7E, 0xFF, 0x06, 0x06, 0x00, 0x00, 0x20, 0xFE, 0xD5, 0xEF])

uart1.write(volume10)
