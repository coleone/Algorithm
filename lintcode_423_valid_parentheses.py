import sys

def match(input_string):
	string = input_string
	size = len(string)
	print size

	list_left_brace = []
	if string == "":
		print "input string is empty!"
		return None
		
	else:
		string = string.replace("\r\n", "")
		
		for i in range(0, size):
			if  string[i] == "[" or string[i] == "{" or string[i] == "(":
				list_left_brace.append(string[i])
			elif string[i] == "]" or string[i] == "}" or string[i] == ")":
				try:	
					left = list_left_brace.pop()
					print left
					
					if left == "[":
						if string[i] == "]":
							print left, string[i]
							continue
						else:
							print left, string[i]
							print "Not matching!"
							return None
					
					if left == "(":
						if string[i] == ")":
							print left, string[i]
							continue
						else:
							print left, string[i]
							print "Not matching!"
							return None
					
					if left == "{":
						if string[i] == "}":
							print left, string[i]
							continue
						else:
							print left, string[i]
							print "Not matching!"
							return None
					
				except:
					print "left is {}, right is {}".format(left, string[i])
					return None
			
			else:
				continue
				
		if len(list_left_brace) != 0:
			print "list_left_brace is not empty, not matching!", list_left_brace, " ", len(list_left_brace)
			return None
		else:
			print "list_left_brace is empty, matching!", list_left_brace, " ", len(list_left_brace)
			return True

if __name__ == "__main__":
	string = "abc{([])}def[()]"
	print match(string)
	sys.exit()