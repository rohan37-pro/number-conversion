hexdigit = "0123456789ABCDEF"
hex_dictionry = {}
for i in range(len(hexdigit)):
	nibble = bin(i).replace("0b","")
	if len(nibble)%4 != 0 :
		nibble = "0"*(4-(len(nibble)%4)) +nibble
	hex_dictionry[hexdigit[i]] = nibble



class bin2hex:

	def __init__(self):
		self.binary	= input("enter a binary : ")
		self.right_part = self.binary.split(".")[0]
		try:
			self.left_part = self.binary.split('.')[1]
			self.hexadecimal = "."
		except:
			self.left_part = ""
			self.hexadecimal = ""

	def convert_left(self):
		hexadecimal = self.hexadecimal
		if len(self.left_part)%4 != 0:
			self.left_part += "0"*(4-len(self.left_part)%4)
		range_ = len(self.left_part)//4
		for i in range(range_):
			nibble_ = self.left_part[i*4:4*(i+1)]
			for j in hex_dictionry:
				if int(nibble_) == int(hex_dictionry[j]):
					hexadecimal+=j
		print(hexadecimal)
		return hexadecimal


	def convert_right(self):
		hexadecimal = ""
		if len(self.right_part)%4 != 0:
			self.right_part = "0"*(4-len(self.right_part)%4)+self.right_part
		range_ = len(self.right_part)//4
		for i in range(range_):
			nibble_ = self.right_part[i*4:4*(i+1)]
			for j in hex_dictionry:
				if int(nibble_) == int(hex_dictionry[j]):
					hexadecimal+=j
		return hexadecimal

class hex2bin:

	def __init__(self):
		self.hex	= input("enter a hexadecimal number : ")
		self.hex = self.hex.upper()
	
	def convert_binary(self):
		binary = ""
		for i in self.hex:
			if i == ".":
				binary += i
			else:
				binary += hex_dictionry[i]

		return binary


print("enter 'quit' or 'q' to exit")
print("for binary to hexadecimal convertion type 'b'")
print("for hex to binary convertion type 'h'")
while True:
	mode = input("select mode : ")
	if mode == 'b':
		converter = bin2hex()
		if converter.binary == 'quit' or converter.binary == 'q':
			break
		hexadecimal = converter.convert_right() + converter.convert_left()
		print(f"hexadecimal of the binary is {hexadecimal}")
	if mode == 'h':
		converter = hex2bin()
		binary = converter.convert_binary()
		print(f"binary  = {binary}")
	if mode == "quit" or mode == 'q':
		break