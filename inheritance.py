class Publisher:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("name : ",self.name)
class Book(Publisher):
    def __init__(self, title, author, name):
        super().__init__(name)
        self.title = title
        self.author = author
    def display(self):
        super().display()
        print("Title : ",self.title)
        print("Author : ",self.title)
class Python(Book):
    def __init__(self,title,author,name,price,pages):
        super().__init__(name,title,author)
        self.price=price
        self.pages=pages
    def display(self):
        super().display()
        print("Price : ",self.price)
        print("No. Of Pages : ",self.pages)


p1 = Python("ABC","basam","xyz",2000,45)
p2 = Python("DEF","hamsa","abd",8999,69)

p1.display()
print("\nSecond :\n")
p2.display()