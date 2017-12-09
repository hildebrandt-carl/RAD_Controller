from serial_utils import *

# usage: sendFile( fileName )
# example: sendFile( 'patterns/SimpleBeat.csv' )
def sendFile(*args):
	f =  open(args[0])
	content = f.readlines()
	content = [x.strip() for x in content]

	for line in content:
		list = line.split(',')
		if list[1]:
			drums = list[1].split('+')
			for drum in drums:
				d = 0
				if drum == 'BASS':     # (1<<7) = 128
					d = d + 128
				elif drum == 'FLTOM':  # (1<<6) = 64
					d = d + 64
				elif drum == 'LOTOM':  # (1<<5) = 32
					d = d + 32
				elif drum == 'HITOM':  # (1<<4) = 16
					d = d + 16
				elif drum == 'SNARE':  # (1<<3) = 8
					d = d + 8
				elif drum == 'HIHAT':  # (1<<2) = 4
					d = d + 4
				elif drum == 'CYMBAL': # (1<<1) = 2
					d = d + 2
			sendMessage(8, d, int(list[0])) # 8=SCHDL message
