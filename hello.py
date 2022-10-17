# print("hello world!")
# print("구해원")

# TRUD = 1

# if TRUD:
#     print ("나는 ")
#     print ("바보입니다.")

# else:
#    print ("그런데 ")
#    print ("바보와 천재는 종이한장 차이 입니다.")

#!/usr/bin/python3

# counter = 100
# miles = 1000.0
# name = "John"

# print(counter)
# print(miles)
# print(name)

# str = 'Hello World!'

# print(str)
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str * 2)
# print(str + "TEST")

# list = ['abcd', 786, 2.23, 'john', 70.2]
# tinylist = [123, 'john']

# print(list)
# print(list[0])
# print(list[1:3])
# print(list[2:])
# print(tinylist * 2)
# print(list + tinylist)

# dict = {}
# dict['one'] = "This is one"
# dict[2]     = "This is two"

# tinydict = {'name': 'john','code':6734, 'deot': 'sales'}

# print(dict['one'])
# print(dict[2])
# print(tinydict)
# print(tinydict.keys())
# print(tinydict.values())

# counter = 100
# miles = 1000.0
# name = "john"

# print(counter);
# print(miles);
# print(name);

# str = 'Hello world!'

# print(str)
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str * 2)
# print(str + "TEST")

# list = ['abcd', 786, 2.23, 'john', 70.2]
# tinylist = [123, 'john']

# print(list)
# print(list[0])
# print(list[1:3])
# print(list[2:])
# print(tinylist * 2)
# print(list + tinylist)

# tuple = ( 'abcd', 786, 2.23, 'john', 70.2) tuple만 안에 값을 바꿀 수 없다.
# tinytuple = (123, 'john')

# print(tuple)
# print(tuple[0])
# print(tuple[1:3])
# print(tuple[2:])
# print(tinytuple * 2)
# print(tuple + tinytuple)

# dict = {}
# dict['one'] = "this is one"
# dict[2] = "this is two"

# tinydict = {'name' : 'john', 'code' : 6734, 'dept' : 'sales'}

# print( dict['one'])
# print(dict[2])
# print(tinydict)
# print(tinydict.keys())
# print(tinydict.values())

# var = 50
# if(var > 75) : 
#     print( "Var는 75초과입니다" )
# elif (var <= 75 & var > 25) :   
#     print("var는 25초과, 75이하 입니다.")
# else :
#     print("var는 25이하입니다.")

# import sys

# list = [1,2,3,4]
# it = iter(list)
# print(next(it))

# for x in it:
#     print(x, end=" ")
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# def printme(str):
#     "This prints a passed string into this function"
#     print (str)
#     return

# printme("THis is firtst call to the user defined function!")
# printme("Again second call to the same function")

# def changeme(mylist):
#     "This changes a passed list into this function"
#     print("Values inside the function before change: ", mylist)
#     mylist[2]=50
#     print("Values inside the function after change", mylist)
#     return

# mylist = [10,20,30]
# changeme(mylist)
# print("Values outside the function:", mylist)

# def changeme(mylist):
#     "Thisn changes a passed list into this fucntion"
#     mylist = [1,2,3,4]
#     print("Values inside the function: ", mylist)
#     return

# mylist = [10,20,30]
# changeme(mylist)
# print("Values outside the function:", mylist)

# def printme(str):
#     "This prints a passed string into this function"
#     print (str)
#     return

# printme()

# def printme(str):
#     "This prints a passed string into this function"
#     print(str)
#     return

# printme( str = "My string")

def printinfo( name, age):
    "This prints a passed info into this funcion"
    print("Name: ", name)
    print("Age", age)
    return

printinfo(age = 50, name = "miki")

def printinfo( name, age = 35):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return

printinfo(age = 50, name = "miki")
printinfo(name = "miki")

def printinfo( arge1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

printinfo(10)
printinfo(70, 60, 50)

sum = lambda arg1, arg2: arg1 + arg2

print ("Value of total :", sum(10, 20))
print ("Value of total :", sum(20, 20))

def sum(arg1, arg3):
    total = arg1 + arg2
    print("Inside the funcion :", total)
    return total

total = sum(10, 20)
print("Outside the function : ", total)

total = 0
def sum(arg1, arg2):
    total = arg1 + arg2;
    print("Inside the function local total : ", total)
    return total

sum(10, 20)
print("Outside the function global total : ", total)




