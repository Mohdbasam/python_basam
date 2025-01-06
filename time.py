class Time:
    def __init__(self,hrs,min,sec):
        self.__hrs=hrs
        self.__min=min
        self.__sec=sec

    def __add__(self, other):
        hrs = self.__hrs + other.__hrs
        min = self.__min + other.__min
        sec = self.__sec + other.__sec

        if sec>=60:
            min+=int(sec/60)
            sec=sec%60
        if min>=60:
            hrs+=int(sec/60)
            min=min%60
        t3 = Time(hrs,min,sec)
        return t3
    def display(self):
        print(self.__hrs)
        print(self.__min)
        print(self.__sec)

t1 = Time(3,50,55)
t2 = Time(5,16,56)
t3 = t1+t2
t3.display()
