def counter():
	def incrementer():
		num = 0
		num += 1
		return num
	return incrementer()

print(counter())