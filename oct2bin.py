#initialize a reference dictionary
oct_str = "012345678"
bin_lis = ["000",'001','010','011','100','101','110','111']
oct_dict = {}
for i in range(8):
	oct_dict[oct_str[i]] = bin_lis[i]

#create a class for convertion 
class oct2bin:
	'''this class takes octal number as input and convert it into a corresponding binary,
	input can be a float point or can be a integer type, it can take care of both of them.
	'''
	def __init__(self):
		#take input and split it in two parts
		self.octal = input("enter a octal number : ")
		self.left_part = self.octal.split(".")[0]
		#function call inside the class 
		try:
			self.right_part = self.octal.split(".")[1]
			self.binary = self.convert(self.left_part) + '.' + self.convert(self.right_part)
		except:
			self.right_part = ""
			self.binary = self.convert(self.left_part) 
	
	#function to do the real job
	def convert(self,octal):
		binary = ""
		for i in octal:
			binary += oct_dict[i]

		return binary

#starting the process
if __name__ == '__main__':
	convert = oct2bin()
	print(f"binary is \n{convert.binary}")
