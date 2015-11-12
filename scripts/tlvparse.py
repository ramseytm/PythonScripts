#-------------------------------------------------------------------------------
# Name:         tlvparse.py
# Purpose:      A simple python script that parses a tlv formatted string and
#				and prints the results in a table.
#
# Author:       Tyler Ramsey
#
# Created:      10/08/2015
# Copyright:    (c) Tyler Ramsey 2015
# Licence:      The MIT License (MIT)

# Copyright (c) 2015 Tyler Ramsey

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# ONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#-------------------------------------------------------------------------------

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