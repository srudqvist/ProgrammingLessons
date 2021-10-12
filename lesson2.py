### 
### Programming Lessons: Anonymous Functions, div and mod
### Author: Samuel Rudqvist
###

def myfun(n):
  return lambda a : a * n

double = myfun(2)
triple = myfun(3)

print(double(5))
print(triple(5))

def test(n):
   return lambda k:k

test1 = test(1)
print(test1(1))
#def foo(myfun, num1,num2):
   # print(myfun(num1, num2))

#foo(lambda x, y : x + y, 6, 7)

#foo(lambda x, y : x * y, 10, 3)

#print('500//60:', 500//60)
#print('500.0//60:', 500.0//60)
#print('500/60:', 500/60)
#print('500 % 60:', 500 % 60)
#print('10 % 2:', 10 % 2)


#print('divmod(500,60):', divmod(500,60))
#print('divmod(10,2):', divmod(10,2))