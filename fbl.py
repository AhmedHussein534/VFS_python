import struct

class SLinkedList:
	def __init__ (self):
		self.headval=None

class Node:
	def __init__ (self,start=None,count=None):
		self.start = start
		self.count = count
		self.nextval = None

class fbl:

	def __init__(self):
		self.linkedList = SLinkedList()
		self.blockCount = 0
	
	def fblToBytes (self):
		op = bytes()
		temp = self.linkedList.headval
		while temp is not None:
			op += struct.pack("i",int(temp.start)) + struct.pack("i",int(temp.count))
			temp = temp.nextval
		return op

	def bytesToFbl (self,input,size):
		numInt = int(size/4)
		temp=struct.unpack("i"*numInt,input)
		self.blockCount = 0
		first=Node(temp[0],temp[1])
		self.blockCount += first.count
		self.linkedList.headval = first
		for i in range (2,numInt,2):
			next=Node(temp[i],temp[i+1])
			self.blockCount += next.count
			first.nextval = next
			first=next

	def __validateBlocks__ ():
		node = self.linkedList.headval
		while node.nextval is not None:
			if node.nextval.start == (node.start+node.count-1):
				node.count += node.nextval.count
				node.nextval = node.nextval.nextval
				
		
	
	
	def __getBestFit__(self,blockCount):
		bestFit = self.linkedList.headval
		node = self.linkedList.headval
		while node.nextval is not None:
			if (bestFit.count - blockCount) > (node.nextval.count - blockCount):
				bestFitPre = node
				bestFit = node.nextval
			node = node.nextval

		if bestFit.count <= blockCount:
			if self.linkedList.headval == bestFit:
				self.linkedList.headval == bestFit.nextval
			else:
				bestFitPre.nextval = bestFit.nextval
			return bestFit
		out = Node(bestFit.start,blockCount)
		bestFit.start += blockCount
		self.__validateBlocks__()
		return out

	def allocateBlocks(bytes):
		blockCount = int(int(bytes)/blockSize + 0.5)
		if blockCount > self.blockCount:
			return None
		outList = list()
		#try to find best fit
		while blockCount > 0:
			bestFit=self.__getBestFit__(blockCount)
			if bestFit == None:
				print("Error")
			outList.append(bestFit)
			blockCount -= bestFit.Count
		return outList		
	
	def printFBL (self):
		next = self.linkedList.headval
		while next is not None:
			print("start:" + str(next.start) + "\ncount" + str(next.count))
			next = next.nextval

	def testInit (self):
		e1 = Node(0,6)
		e2 = Node(6,6)
		e3 = Node(11,5)
		self.linkedList.headval = e1
		e1.nextval = e2
		e2.nextval = e3




file=open("test","+ab")
file.seek(0)
fblInstance = fbl()
#"""
#fblInstance.testInit()
#test=fblInstance.fblToBytes()
#file.write(test)
#"""
#"""
x=file.read(24)
print(x)
fblInstance.bytesToFbl(x,24)
fblInstance.printFBL()
#"""
			
		
		
		

			
    

		
