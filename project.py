class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return self.radius*2*3.14
radius=int(input("Enter the radius:"))
Newcircle=Circle(radius)
print(Newcircle.area())
print(Newcircle.perimeter())