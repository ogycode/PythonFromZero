"""module for A class"""

class A(object):

    F = "F's var"
    _P = "private"              #_  - private
    __G = "undefind"            #__ - undefind 
    
    def test1(self):
        print("hello! im A class")

    def test2(self):
        print("hello 2! im A class, F: {}".format(self.F))

    def GetP(self):
        print("P: {}".format(self._P))

    def GetG(self):
        print("G: {}".format(self.__G))