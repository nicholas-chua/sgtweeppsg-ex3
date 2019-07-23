with open ('Data/data.csv', 'r') as f:
	headers = next(f)
	print (headers)
	for line in f:
		line = line.strip()
		parts = line.split(',')
		parts[1] = float(parts[1])
		parts[2] = float(parts[2])
		if parts[2] == 0.00:
			parts[3] = 0.00
		else:
			parts[3] = parts[2]/parts[1]
		print(parts)
