#Inheritance is one of the fundamental concepts of oops in which one class use characteristics of another classes

class A:
    def display():
        print("In class A")

class B(A):
    def show():
        print("In class B")


#creating object of class B: we always create object of most recent derived class
obj = B

#calling show method of class B
obj.display()
obj.show()
