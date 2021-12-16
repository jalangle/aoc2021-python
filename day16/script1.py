#!python3
import logging
import pprint
import unittest

logging.basicConfig(filemode='w', level=logging.WARN)
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

def inputToBinary(value):
	binaryValues = list()
	res = ""
	for c in value:
		res += charToBin(c)
	binaryValues.append(res)
	return res

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

	logging.info("=" * 40)
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


def fromString(hexValue):
	binaryValue = inputToBinary(hexValue)

	logging.debug(hexValue)
	(bitsRead, versionSum) = parsePacket(binaryValue)

	logging.debug("Total Bits Read: " +  str(bitsRead))

	logging.debug("=" * 40)	
	logging.debug("Value: " + str(versionSum))

	return versionSum

def fromPath(path):
	hexValues = parseFile(path)
	assert(len(hexValues) == 1)
	return fromString(hexValues[0])

class TestDay16Part1(unittest.TestCase):

	def test_testdata1(self):
		self.assertEqual(fromString('D2FE28'), 6)

	def test_testdata2(self):
		self.assertEqual(fromString('38006F45291200'), 9)

	def test_testdata3(self):
		self.assertEqual(fromString('EE00D40C823060'), 14)

	def test_testdata4(self):
		self.assertEqual(fromString('8A004A801A8002F478'), 16)

	def test_testdata5(self):
		self.assertEqual(fromString('620080001611562C8802118E34'), 12)

	def test_testdata6(self):
		self.assertEqual(fromString('C0015000016115A2E0802F182340'), 23)

	def test_testdata7(self):
		self.assertEqual(fromString('A0016C880162017C3686B18A3D4780'), 31)

	def test_inputdata(self):
		self.assertEqual(fromPath('input'), 847)

if __name__ == '__main__':
	unittest.main()