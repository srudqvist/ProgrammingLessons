### 
### Programming Lessons 4: Recursion
### Author: Samuel Rudqvist
###

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,6):
    print(factorial(i))
