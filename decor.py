# function  as an object

def func():
    return "hello"
print("fun =", func())
ass1 = func                 #here assigning function to a variable,it will take the function object of func
print("sec=",ass1())

def sum(a,b):
    return a+b
print("sum =",sum(2,3))

add = sum
print("add=",add(5,6))

# function as argument
def find(text):
     if "d" in text:
         return "welcome"

     else:
         return "not allow"

def allow(func):
    greeting = func("divya")
    print(greeting)
    return greeting

msg = allow(find)  # giving find function as arugument to allow function


#inner function
def outerFunction(text):
    print(text +" "+"welcome")

    def innerFunction():
        print(text)

    innerFunction()

outerFunction('hi divya')

#decorat function

def sub(a,b):
    print("sub=",a-b)

def super_sub(func):
    
    def inner(a,b):
        if a<b:
            a,b =b,a
        return func(a,b)
    return inner

sub1 = super_sub(sub)
sub1(2,4)