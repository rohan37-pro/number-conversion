oct_str = "012345678"
bin_lis = ["000",'001','010','011','100','101','110','111']
oct_dict = {}
for i in range(8):
	oct_dict[oct_str[i]] = bin_lis[i]


class oct2bin:

	def __init__(self):
		self.octal = input("enter a octal number : ")
		self.left_part = self.octal.split(".")[0]
		try:
			self.right_part = self.octal.split(".")[1]
			self.binary = self.convert(self.left_part) + '.' + self.convert(self.right_part)
		except:
			self.right_part = ""
			self.binary = self.convert(self.left_part) 


	def convert(self,octal):
		binary = ""
		for i in octal:
			binary += oct_dict[i]

		return binary

if __name__ == '__main__':
	convert = oct2bin()
	print(f"binary is \n{convert.binary}")
