import sys

if __name__ == "__main__":
	dict_name = {'Li': ['Jeff', 'Bai'],
				 'Liu': 'Liu',
				 'Bai': 'Yun'}
	
	# Sort last name
	last_name_sorted = sorted(dict_name.items(), key = lambda d:d[0])
	print last_name_sorted
	
	# Sort first name
	first_name_sorted = []
	for i, j in last_name_sorted:
		try:
			j.sort()
			for k in j:
				first_name_sorted.append((i,k))
		except:
			first_name_sorted.append((i,j))
			pass

	print first_name_sorted
	
	sys.exit()