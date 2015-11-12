#-------------------------------------------------------------------------------
# Name:         genUUID.py
# Purpose:      A simple python script with command line interface for generating
#               UUIDs with a variety of formatting options.
#
# Author:       Tyler Ramsey
#
# Created:      09/10/2013
# Copyright:    (c) Tyler Ramsey 2013
# Licence:      The MIT License (MIT)

# Copyright (c) 2013 Tyler Ramsey

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
import uuid

from optparse import OptionParser

def main():
    """Parse command line options provided by the user and run the program."""

    USAGE = "usage: %prog [options] -c [count]"

    #Generate options supported by the prog...
    parser = OptionParser(USAGE)
    parser.add_option("-c", "--count",
                      action="store", type="int", dest="count",
                      help="Number to generate")
    parser.add_option("-u", "--upper",
                      action="store_true", dest="uppercase", default=False,
                      help="To Uppercase [default: %default]")
    parser.add_option("-r", "--remove-hyphens",
                      action="store_true", dest="hyphens", default=False,
                      help="Remove hyphens [default: %default]")
    parser.add_option("-b", "--braces",
                      action="store_true", dest="braces", default=False,
                      help="Wrap GUID in braces [default: %default]")
    parser.add_option("-l", "--line-numbers",
                        action="store_true", dest="linenumbers", default=False,
                        help="Add line numbers to output [default: %default]")

    (options, args) = parser.parse_args()

    #As long as count is specified, run...
    if(options.count == None):
        parser.error("You must enter the number of guids to generate")
    else:
        printGUIDs(options.count, options.uppercase, options.hyphens, options.braces, options.linenumbers)


def printGUIDs(amount, upper, hyphens, braces, linenumbers):
    """Generates and prints a list of guids to stdout

    Parameters:
        amount -- The amount of guids to generate and print
        upper -- A value that determines whether the guids should be uppercase
        hyphens -- A value that determines whether the guids should have hyphens
        braces -- A value that determines whether the guids should be wrapped in braces
        linenumbers -- A value that determines whether the linenumbers should be generated for the output."""

    guidList = getGuidList(amount)

    if upper:
        guidList = [x.upper() for x in guidList]

    if hyphens:
        guidList = [x.replace("-", "") for x in guidList]

    if braces:
        guidList = [("{0}" + x + "{1}").format("{", "}") for x in guidList]

    if linenumbers:
        guidList = [str(i) + ". " + x for i, x in enumerate(guidList, 1)]

    for item in guidList:
        print(item)


def getGuidList(n):
    """Generate a list of guids

    Parameters:
        n (int) -- The number of guids to generate"""

    for x in range(0, n):
        yield str(uuid.uuid4())


if __name__ == "__main__":
	main()

