class employee:
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        print("Destructor Called")
def Creatobj():
    print("Making Object")
    obj=employee()
    print("function end")
    del obj
print("Calling Createobj() function")
obj=Creatobj()
print("Program end")