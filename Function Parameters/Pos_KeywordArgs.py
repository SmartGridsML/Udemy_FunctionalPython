#
"""
Positional args
Most common way of assigning args to function params via order in which they are passed

Defult values 
def my_func(a , b = 10)
b is now given a default val therefore it is ioptional to pass during the function call
Caveat: default values if positional param is defined with a defined value
        -> every positional param after it MUST also be given a default

Keyword(named) arguments
def my_func(a , b = 5 , c = 10)
calling funtion 
def my_func(a = 1 , c = 2) # translates to a = 1 , b = 5 , c = 2
"""
print("HW")