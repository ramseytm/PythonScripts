import sys

from prettytable import PrettyTable

bitMask = 0x1F

def formatHexValue(stringValue):
	counter = 0
	result = ""

	for c in stringValue:
		if counter % 2 == 0:
			result += "0x"

		result += c
		counter +=1

		if counter % 2 == 0:
			result += ", "

	return result[0:len(result) - 2]

def main():
	if len(sys.argv) < 2:
		print "Please provide a tlv formatted string."
		return

	table = PrettyTable(["Tag", "Length", "Value"])
	table.align["Value"] = "l"

	tlvData = sys.argv[1]
	position = 0

	array = bytearray.fromhex(tlvData)
	while position < len(array):
		tag = format(array[position], "02X")

		if array[position] & bitMask == bitMask:
			tag += format(array[position+1], "02X")
			position += 1

		position +=1
		length = format(array[position], "02X")

		position +=1
		value = formatHexValue(''.join(format(b, "02X") for b in array[position : position + array[position-1]]))

		position += array[position-1]
		table.add_row([tag, length, value])

	table.sortby = "Tag"
	print table


if __name__ == "__main__":
	main()