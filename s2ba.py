import sys

def main():
	if len(sys.argv) < 2:
		print "Please provide a tlv formatted string."
		return
		
	for stringVar in sys.argv[1:]:
		counter = 0
		result = ""

		if len(stringVar) % 2 != 0:
			raise ValueError("String entered does not have an even amount of characters.")

		for c in stringVar:
			if counter % 2 == 0:
				result += "0x"

			result += c
			counter +=1

			if counter % 2 == 0:
				result += ", "

		print result[0:len(result) - 2]

if __name__ == "__main__":
	main()