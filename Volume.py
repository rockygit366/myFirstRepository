class Volume:
   'Volume object'
   volCount = 7

   def __init__(self, name, parent, size, fs):
      self.name = name
      self.parent = parent
      self.size = size
      self.fs = fs
      Volume.volCount += 1
	  
   def displayVolume(self):
      print "Total Volume %d" % Volume.volCount

   def displayArray(self):
      print "Name : ", self.name,  ", Parent: ", self.parent,  ", Size: ", self.size