class IOstring():
    def __init__(self):
        self.str1=""
    def getstring(self):
        self.str1=input("Enter String:")
    def printstring(self):
        print("Result is equal to:",self.str1.upper())
str1=IOstring()
str1.getstring()
str1.printstring()
