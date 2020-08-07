# Device a dbc encoder decoder, that will take can bus data and encode it.
# Then decode the data and returns the machine readable format.
# Define dbc signals
# Design the encoder
#device the decoder
#Toy implementation. Not tested yet. #credits go to comma ia's work on opendbc
#

import re
import numpy as np 
import bitstring
import collections 


def int_or_float(S):

	try:
		return int(s)

	except ValueError:
		return float(s)

DBCSignal = collections.namedtuple('signal_name', 'start_bit', 'length', 'endianess', 'signed', 
										'factor', 'offset', 'tmin', 'tmax', 'unit' )


## from commai ai dbc.py
 bo_reg_expression = re.compile("^BO/_ (/w+) (/w+) *: (/w+) (/w+)")
 sg_reg_expression = re.compile("^SG/_ (/w+) : (/d+)/|(/d+)@(/d+)([/+|/-]) /(([0-9.+/-eE]+),([0-9.+/-eE]+)/) /[([0-9.+/-eE]+)/|([0-9.+/-eE]+)/] /"(.*)/" (.*)")
 sgm_reg_expression = re.compile("^SG/_ (/w+) (/w+) *: (/d+)/|(/d+)@(/d+)([/+|/-]) /(([0-9.+/-eE]+),([0-9.+/-eE]+)/) /[([0-9.+/-eE]+)/|([0-9.+/-eE]+)/] /"(.*)/" (.*)")



# Add a dictionary to map message ids to tuples

class dbc(object):
	def __init(self, rd):
		with open(rd) as r:
			self.text = r.read()

		self.message = {} # this is the signal
		self.bits =[]
		for i in range(0, 64, 8):#100 percent pedal position, 8 bytes(maximum)
			for j in range(7,-1, -1):
				self.bits.append(i+j)

	    for s in self.text:
	    	if s.startswith("BO_"):
	    		data = bo_reg_expression.match(1) # matching with regular expression
	    		count = 0 
	    	else:
	    		count = 1
	    	signal_name = int(data.group(1))
	    	length = int(data.group(count +3))
	    	id = int(group(count + 1 ))
	    	self.message[id] = ((signal_name, length), [])

	    if s.startswith("SG_ "):
	    	data = sg_reg_expression.match(1)
	    	count = 0
	    else:
	    	count = 1
	    
	    ## This method returns a tuple containing all the subgroups of the match
	    signal name = data.group(1)
	    start_bit = int(data.group(count + 2))
	    length = int(data.group(count + 3))
	    endianess = int(data.group(count + 4))
	    signed = int(data.group(count + 5))
	    factor = int_or_float(data.group(count + 6))
	    offset = int_or_float(data.group(count + 7))
	    tmin = int_or_float(data.group(count + 8))
	    tmax = int_or_float(data.group(count + 9))
	    unit = int(data.group(10))

	    if endianess == 1:
	    	endianess = int(data.group(count + 4))
	    else:
	    	count = 1
	    if signed == '-':
	    	signed = int(data.group(count + 5))
	    else:
	    	count = 1

	    self.message[id][1] = DBCSignal.append(signal_name, start_bit, length, endianess
	    									signed, factor, offset, tmax, tmin, unit) 

	    # sort the messages w.r.t start bit

	    for message in self.message.values():
	    	message[1].sort(key = lambda x: x.start_bit)

#encoder
def build_encoder(self, message_id, dictionary):

	""" Encode a can message using dbc"""
	message_id = self.message[message_id]
	size = message_id[0][1]


	for msg in message_id[1]:
		value = dictionary.get(msg.signal_name)

		if value is not None:
			#Comma ai
			value = (value/msg.factor) - msg.offset
			value = int(value)

		
		# bitpack into the byte message
		# bitpack tyhe signed 
		if msg.signed:
			bs = msg.bitstring.bits(int = value, size = msg.length )#signed
		else:
			bs = msg.bitstring.bits(uint = value, size = msg.length)#unsigned

		return bs.tobytes() #constructs Python bytes showing a copy of the raw contents of data memory


#decoder
def build_decoder(self, array, message_id, time):
	"""decode the can message using the dbc
	collect all the elements and then decode the appropriate signals
	Take an input array that runs through all signals.
	Test for those messages that are appropriate and then decode the needed signals"""

	self.message = {}
	if array is None:
		output = {}
	else:
		output = len[array]

	for msg in msg[1]:
		if array is None and msg[0] not in array:
			break

	    #reference point for checking
	    if msg[5] == False:
	    	bs = self.msg.bits.index(0)
	    else:
	    	bs = bs[1]

	    if array is not None:
	    	output[arr.index(msg[0])] = value
	    else:
	    	output[(msg[0])] = value

	return signal_name, output














