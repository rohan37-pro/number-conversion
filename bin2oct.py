oct_str = "012345678"
bin_lis = ["000",'001','010','011','100','101','110','111']
oct_dict = {}
for i in range(8):
	oct_dict[oct_str[i]] = bin_lis[i]

class bin2oct:

	def __init__(self):
		self.binary = input("enter a binary : ")
		self.left_part = self.binary.split('.')[0]
		try:
			self.right_part = self.binary.split('.')[1]
			self.octal = bin2oct.convert_left(self.left_part) + '.' + bin2oct.convert_right(self.right_part)
		except:
			self.octal = bin2oct.convert_left(self.left_part)

	def convert_right(binary):
		octal = ""
		if len(binary)%3 != 0:
			binary += '0'*(3-len(binary)%3)
		for i in range(len(binary)//3):
			_3bits = binary[i*3:3*(i+1)]
			for j in oct_dict:
				if oct_dict[j] == _3bits:
					octal += j
		return octal


	def convert_left(binary):
		octal = ""
		if len(binary)%3 != 0:
			binary = '0'*(3-len(binary)%3) + binary
		for i in range(len(binary)//3):
			_3bits = binary[i*3:3*(i+1)]
			for j in oct_dict:
				if oct_dict[j] == _3bits:
					octal += j

		return octal


if __name__ == '__main__':
	convert = bin2oct()
	print(f"octal : {convert.octal}")