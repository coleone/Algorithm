def first_non_repeat(string):
	str_hash = {}
	length = len(string)

	if length == 0:
		print "ERROR: Input string length is 0\r\n"
		return None
	
	# This for loop is for assigning values to the keys.
	for i in range(length):
		if string[i] not in str_hash.keys():
			str_hash[string[i]] = 1
		else:
			str_hash[string[i]] += 1

	print str_hash

	# This for loop is for checking first non repeat letter of the string.
	for i in range(length):
		if str_hash[string[i]] == 1:
			print "First non repeat letter is %s \r\n" %string[i]
			return string[i]

	# Return None if all letters are repeated.
	return None

if __name__ == "__main__":
	string = "abccbsabcdefgabcde"
	print "Input string is %s\r\n"%string
	string_2 = first_non_repeat(string)
	print "string_2 is %s\r\n" %string_2