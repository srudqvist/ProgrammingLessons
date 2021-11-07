### 
### Programming Lessons 4: Recursion
### Author: Samuel Rudqvist
###
import time

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#for i in range(1,6):
 #   print(factorial(i))

def snafu():
    snafu()

#snafu()

#f(0) = 5 and f(k) = f(k-1) + 7 for integers k > 0

def myfunc(n):
    if n < 0:
        return -1
    if n == 0:
        return 5
    else:
        return myfunc(n-1) + 7

#print("n = 1:",myfunc(1))
#print("n = 2:",myfunc(2))
#print("n = 3:",myfunc(3))

def fibonacci(k):
    if k < 0:
        print("This function only takes positive numbers.")
        return -1
    elif k == 0:
        return 0
    elif k == 1 or k == 2:
        return 1
    else:
        return fibonacci(k-1) + fibonacci(k-2)
startTime = time.time()
print("Fibonacci, 10:", fibonacci(10))
endTime = time.time()
print("Time for k = 10:", endTime - startTime)

print("Fibonacci, 20:", fibonacci(20))
print("Fibonacci, 30:", fibonacci(30))

startTime1 = time.time()
print("\nFibonacci, 34:", fibonacci(34))
endTime1 = time.time()
totTime1 = endTime1 - startTime1
print("Time for k = 34:", totTime1)

startTime2 = time.time()
print("\nFibonacci, 35:", fibonacci(35))
endTime2 = time.time()
totTime2 = endTime2 - startTime2
print("Time for k = 35:", totTime2)

startTime3 = time.time()
print("\nFibonacci, 36:", fibonacci(36))
endTime3 = time.time()
totTime3 = endTime3 - startTime3
print("Time for k = 36:", totTime3)

print("\nTime 34 + 35:", totTime1 + totTime2)


