class Student:
    #class variable which is common for entire class
    college_name = "BBD"
    #the first parameter is always self which is reference to current object of the class
    #constructor always takes one parameter which is self
    #default constructor which only have self attributes or parameter
    def __init__(self):
        print("Creating new student....")

    #parameterezid constructor which have attributes or parameter more than self        
    def __init__(self, name, marks):
        #object attribute which is different for each object 
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome...", self.name)

    def get_marks(self):
        print("Your mraks is: ",self.marks)
s = Student("Karan", 97)
s.welcome()
s.get_marks()



    
