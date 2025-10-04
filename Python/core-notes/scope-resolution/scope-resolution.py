# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    x = 1
    print(x)
    
def func2():
    x = 2
    print(x)
    
#functions cant see inside of other functions

#Built-in are read in the most outer function like import math and math.pi 
#variables can be same if they are in different scope. 