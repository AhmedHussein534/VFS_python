import struct

class SuperBlock:
	def __init__(self):
		self.superBlock={'blockSize':"1024",'numberOfFiles':"0",'fileSize':"0",\
		'freeSize':"0",'fblSize':"0",'numberOfFolders':"0"}
	
	def SuperBlockBytes(self):
		op=struct.pack("i",int(self.superBlock["blockSize"]))
		op+=struct.pack("i",int(self.superBlock["numberOfFiles"]))
		op+=struct.pack("i",int(self.superBlock["fileSize"]))
		op+=struct.pack("i",int(self.superBlock["freeSize"]))
		op+=struct.pack("i",int(self.superBlock["fblSize"]))
		op+=struct.pack("i",int(self.superBlock["numberOfFolders"]))
		return op

	def SuperBlockFromBytes(self,input):
		temp=struct.unpack("iiiiii",input)
		self.superBlock["blockSize"]=str(temp[0])
		self.superBlock["numberOfFiles"]=str(temp[1])
		self.superBlock["fileSize"]=str(temp[2])
		self.superBlock["freeSize"]=str(temp[3])
		self.superBlock["fblSize"]=str(temp[4])
		self.superBlock["numberOfFolders"]=str(temp[5])

	def SuperBlockPrint(self):
		print("***SuperBlockPrint***")
		print("BlockSize:" + self.superBlock["blockSize"])
		print("NumberFiles:"+ self.superBlock["numberOfFiles"])
		print("FileSize:"+self.superBlock["fileSize"])
		print("FreeSize:"+self.superBlock["freeSize"])
		print("fblSize:"+self.superBlock["fblSize"])
		print("FoldersCount:"+self.superBlock["numberOfFolders"])

