#!python3

import logging
logging.basicConfig(filemode='w', level=logging.INFO, format="")

import pprint
pp = pprint.PrettyPrinter(indent=4)

def parseFile(path):
	contents = list()
	with open(path, 'r') as f:
		for l in f:
			contents.append(l.rstrip())
	return contents

def charToBin(c):
	if c == '0':
		return '0000'
	elif c == '1':
		return '0001'
	elif c == '2':
		return '0010'
	elif c == '3':
		return '0011'
	elif c == '4':
		return '0100'
	elif c == '5':
		return '0101'
	elif c == '6':
		return '0110'
	elif c == '7':
		return '0111'
	elif c == '8':
		return '1000'
	elif c == '9':
		return '1001'
	elif c == 'A': #10
		return '1010'
	elif c == 'B': #11
		return '1011'
	elif c == 'C': #12
		return '1100'
	elif c == 'D': #13
		return '1101'
	elif c == 'E': #14
		return '1110'
	elif c == 'F': #15
		return '1111'

def inputToBinary(values):
	binaryValues = list()
	for l in values:
		res = ""
		for c in l:
			res += charToBin(c)
		binaryValues.append(res)
	return binaryValues

def parseType4Number(value):
	bitsRead = 0
	number = ""
	for i in range(6, len(value), 5):
		bitsRead += 5
		block = value[i:i+5]
		shouldContinue = block[0]
		number += block[1:]
		if(shouldContinue == '0'):
			#if(i + 5 < len(value)):
				#remainder = value[i+5:]
				#bitsRead += len(remainder)
				#assert(0 == int(remainder, 0))
			break
	return (int(number, 2), bitsRead)

def parsePacket(value, packetId = "0"):
	bitsRead = 0
	versionSum = 0

	print("=" * 40)
	logging.info("Packet Id: " + str(packetId))
	logging.debug("  V: " + value)

	version = str(int(value[0:3], 2))
	versionSum += int(version)

	bitsRead += 3
	logging.debug("*** Bits Read: " + str(bitsRead) + " ***")
	logging.debug("  VER: " + version)

	typeId = str(int(value[3:6], 2))
	bitsRead += 3
	logging.debug("*** Bits Read: " + str(bitsRead) + " ***")
	logging.debug("  Type: " + typeId)

	if(typeId == '4'): # a Number packet
		(num, type4bitsRead) = parseType4Number(value)
		bitsRead += type4bitsRead
		logging.debug("*** Bits Read: " + str(bitsRead) + " ***")
		logging.info("  Number: " + str(num))

	else: # an Operator packet with a length in bits
		lengthTypeId = value[6]
		if(lengthTypeId == '0'):
			length = 15
			bitsRead += 1
			logging.debug("*** Bits Read: " + str(bitsRead) + " ***")
			logging.debug("  Operator Length: " + str(length))

			subPacketLength = int(value[7:7+length],2)
			bitsRead += length
			logging.debug("*** Bits Read: " + str(bitsRead) + " ***")
			logging.debug("  Sub-packet Length (in bits): " + str(subPacketLength))

			subPacketBitsRead = 0
			subPacketId = 0
			while(subPacketBitsRead != subPacketLength):
				logging.debug("  Sub-packet bits read: " + str(subPacketBitsRead))
				(br, packetVersion) = parsePacket(value[bitsRead + subPacketBitsRead:], packetId + "." + str(subPacketId))
				versionSum += packetVersion
				subPacketBitsRead += br
				subPacketId += 1

			bitsRead += subPacketBitsRead

		elif(lengthTypeId == '1'):
			length = 11
			bitsRead += 1
			logging.debug("*** Bits Read: " + str(bitsRead) + " ***")
			logging.debug("  Operator Length: " + str(length))

			subPacketCount = int(value[7:7+length],2)
			bitsRead += length
			logging.debug("*** Bits Read: " + str(bitsRead) + " ***")
			logging.debug("  Sub-packet Length (in bits): " + str(subPacketCount))

			subPacketBitsRead = 0
			subPacketId = 0
			while(subPacketId != subPacketCount):
				(br, packetVersion) = parsePacket(value[bitsRead + subPacketBitsRead:], packetId + "." + str(subPacketId))
				versionSum += packetVersion
				subPacketBitsRead += br
				subPacketId += 1

			bitsRead += subPacketBitsRead


		else:
			logging.error( "VER: " + version)
			logging.error( "TypeId: " + typeId)
			#assert(False)

	return (bitsRead, versionSum)


def main():
	hexValues = parseFile("input")
	binaryValues = inputToBinary(hexValues)

	case = 0
	logging.debug(hexValues[case])
	(bitsRead, versionSum) = parsePacket(binaryValues[case])

	logging.debug("Total Bits Read: " +  str(bitsRead))

	print("=" * 40)	
	print("Value: " + str(versionSum))


	return

main()