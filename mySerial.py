from serial_utils import *
import struct

connect()

sendMessage(0,4,3)
sendMessage(0,8,6)
sendMessage(0,16,60)
