
class dec2bin:

	def __init__(self):
		self.decimal = input("enter a decimal : ")
		self.left_part = self.decimal.split(".")[0]
		try:
			self.right_part  = self.decimal.split(".")[1]
		except:
			self.right_part = "0"

	def convert_right_part(self):
		binary = ''
		length = len(self.right_part)
		self.list = [self.right_part]
		while int(self.right_part) > 0 :
			number = int(self.right_part)*2
			if len(str(number)) > length:
				binary +='1'
				self.right_part = str(number)[1:]
			else:
				binary += '0'
				self.right_part = str(number)
			pass
			if self.right_part in self.list:
				break
			self.list.append(self.right_part)

		return binary



	def convert_left_part(self):
		binary = ''
		while int(self.left_part) > 0:
			binary = str(int(self.left_part)%2) + binary
			self.left_part = int(self.left_part)//2

		return binary
if __name__ == '__main__':
	while True:
		mode = input("select - convert(c)/quit(q) : ")
		if mode=='c':
			convert = dec2bin()
			binary = convert.convert_left_part() + '.' + convert.convert_right_part()
			print(f"decimal of binary {convert.decimal} is {binary}")
		if mode=="q":
			break
		
