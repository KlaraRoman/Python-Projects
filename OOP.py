#OOP

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def myFunct(self):
        print("Hello my name is "+ self.name)

p1=Person("Bianca", 36)
p1.age=40

p1.myFunct()
print("\n")



#OOP + BOOLEAN

a=int(input("Number: "))
b=int(input("Numbe 2: "))

def myFunction(num1,num2):
    print(isinstance(num1, int))
    return(num1>num2)

print(myFunction(a,b))
print("\n")



#TUPLES

myTuple=tuple(("hakdog","krispy kram", "yeetlog"))
word=input("Gimme a word: ")

if word in myTuple:
    print("Heckin yes")
else:
    print("No heckin")

print("\n")


#FUNCTIONS

def myKids(*kids):
    print("The youngest child of "+kids[0]+" is: "+kids[-1])

myKids("Emily","Aziraphael","Nerlan")
myKids("Xiao bai","Yingluo","Hai-lan Cha")







