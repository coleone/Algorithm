import sys

def find_substring(string, substring):
	i = 0
	j = 0
	i_max = len(string)
	j_max = len(substring)
	
	if j_max > i_max:
		return None
	
	for i in range(i_max):
		print r"i is: " + str(i)
		print r"j is: " + str(j)
		
		temp = i
		
		while (substring[j] == string[i]):
			if j == j_max - 1:
				return (True, temp)
			else:
				i += 1
				j += 1
				print r"i in while loop is: " + str(i)
				print r"j in while loop is: " + str(j)
		
		if i == i_max - j_max + 1:
			return None
		
		else:
			j = 0
			i = temp


if __name__ == "__main__":
	string = r"abcdefghijkz"
	substring = r"hij"
	print find_substring(string, substring)
	