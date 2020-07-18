# functions
# def printName():
#     print("pratap")
# printName()

# def printName():
#     return "pratap"
# print(printName())

# def printName():
#     return "pratap"
# a=printName()
# print(a)

# positional arguments
# def printName(name):
#     print(name)
# printName("pratap")

# default arguments
# def greet(age, name="John"):
#     print("Hello", name, age)
# greet()
# greet(28)
# greet(27, name="mike")

# keyword arguments
# def greet(name="", msg="welcome!"):
#     print("Hello", name + ', ' + msg)
# greet(msg="Good morning!", name="pratap")
# greet(name="naveen", msg="Good morning!")

# positional, default, keyword arguments
# def details(name, married=True, children=None):
#     print(f"name:{name}, married:{married}, children:{children}")
# details("pratap")
# details(married=False, name="pratap")
# details(children="john", name="Mike")

# *args
# def greet(*args):
#     for name in args:
#         print("Hello", name)
# greet("mike", "Luke", "Steve", "John")
# greet("mike")
# greet("mike", "max")

# **kwargs
# def greet(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
# greet(name="mike", msg="gud mrng")
# greet(name="mike")

# factorial program
# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         factorial = 1
#         i = n
#         while i >= 1:
#             factorial = factorial*i
#             i = i -1
#         return factorial
# print(factorial(5))

# recursion
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return (n * factorial(n-1))
# print(factorial(5))

# Anonymous function(lambda)
# sqr=lambda x,y:x+y
# print(sqr(4,5))
