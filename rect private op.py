class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length * self.__width
    def __lt__(self,other):
        if self.area() < other.area():
            return True
        else :
            return False
r1 = Rectangle(5,10)
r2 = Rectangle(10,1)
if r1 < r2:
    print("r2 is greater")
else :
    print("r1 is greater")
