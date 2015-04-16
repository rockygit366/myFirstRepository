class Array:
   'Array object'
   arrayCount = 0

   def __init__(self, name, level, member):
      self.name = name
      self.level = level
      self.member = member
      Array.arrayCount += 1
	  
   def displayArray(self):
     print "Total Array %d" % Array.arrayCount

   def displayArray(self):
      print "Name : ", self.name,  ", Level: ", self.level,  ", Member: ", self.member