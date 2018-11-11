import struct

class File:
	def __init__(self,name):
		self.binFile=open(name,"+ab")
		self.binFile.seek(0)

	def truncate(self,size):
		self.binFile.truncate(int(size))

	def readBytes(self,offset,bytesCount):
		self.binFile.seek(int(offset))
		return self.binFile.read(int(bytesCount))

	def writeBytes(self,offset,chunk):
		self.binFile.seek(int(offset))
		self.binFile.write(chunk)

	def __del__(self):
		self.binFile.close()
	
