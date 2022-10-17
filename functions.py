def printme(str):
    "This prints a passed string into this function"
    print(str)
    return

printme("This is first call to the user difined function!")
printme("Again secound call to the same function")

def printinfo( name, age = 35 ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return

printinfo( age = 50, name = "miki")
printinfo( name = "miki" )

import support


support.print_func("Zara")

import time

localtime = time.asctime( time. localtime()) 
print("Local current time :", localtime)

class Employee:
    'comnon base class for all employees'
    empCount = 0
    
    def _init_(self, name, salary):
        self.name = Name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        pint (" total Employee %d" % Employee.empCount)
        
    def displayEmployee(self):
        print(" Name : ", self.namem ,"salary:", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

class Parent:
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")

    def parentMethod(self):
        print('calling parent method')

    def setAttr(self, attr):
        parent.parentAttr = attr

    def getAttr(self):
        print ("Parent attribute :", parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethhod(self):
        print ('calling child method')

c = Child()
c.childMethhod()
c.parentMethod()
c.setAttr(200)
c. getAttr()