#-------------------------------------------------------------------------------
# Name:         hexdump.py
# Purpose:      A simple python script with command line interface for dumping a 
#				files contents or a string as hex.
#
# Author:       Tyler Ramsey
#
# Created:      11/12/2015
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

from optparse import OptionParser

def main():
	"""Parse command line options provided by the user and run the program."""

	USAGE = "usage: %prog [options]"

	#Generate options supported by the prog...
	parser = OptionParser(USAGE)
	parser.add_option("-f", "--file",
						action="store", type="string", dest="file_path",
						help="File to generate hexdump for.")
	parser.add_option("-d", "--data",
					action="store", type="string", dest="data",
					help="Data to genereate hexdump for.")

	(options, args) = parser.parse_args()

	if(options.file_path == None and options.data == None):
		parser.print_help()

	run(options.file_path, options.data)


def run(file_path, data):
	if file_path:
		f = open(file_path, "rb")
		try:
			byte = f.read(1)
			while byte != "":
				byte = f.read(1)
				print byte.encode('hex'),
		finally:
			f.close()
	elif data:
		byteData = data.encode('utf-8')
		for byte in byteData:
			print byte.encode('hex'),


if __name__ == "__main__":
	main()