
class bin2dec :

	def __init__(self):
		self.binary = input("enter the binary : ")
		self.left_part = self.binary.split(".")[0]
		try:
			self.right_part  = self.binary.split(".")[1]
		except:
			self.right_part = ''

	def convert_right(self):
		decimal = 0
		pow = -1
		for i in range(len(self.right_part)):
			decimal += int(self.right_part[i])*(2**pow)
			pow-=1
		return decimal

	def convert_left(self):
		decimal = 0
		pow = 0
		for i in range(-1,-len(self.left_part)-1,-1):
			decimal += int(self.left_part[i])*(2**pow)
			pow+=1
		return decimal

if __name__ == "__main__":
	while True:
		mode = input("select mode- convert(c)/quit(q) : ")
		if mode=="c":
			convert = bin2dec()
			decimal = convert.convert_left() + convert.convert_right()
			print(f"decimal of binary {convert.binary} is {decimal}")
		if mode=="q":
			break
		
