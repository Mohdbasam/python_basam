class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return (self.length * self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
r1 = Rectangle(10,20)
r2 = Rectangle(15,25)
print(f"Area of First rectangle is : {r1.area()}")
print(r1.perimeter())
print(r2.area())
print(r2.perimeter())