### 
### Programming Lessons 3: List Comprehensions 
### Author: Samuel Rudqvist
###


#print([x*x for x in range(1,15) if x%2==0])

# Question 1 part a.
print("Question 1 Part A")
print("print([x for x in range(1,100) if x%7==0]): ")
print([x for x in range(1,100) if x%7==0])

# Question 1 part b.
print("\nQuestion 1 Part B")
print('''print([x.upper() for x in "Happy Valentine's Day".split(" ")]): ''')
print([x.upper() for x in "Happy Valentine's Day".split(" ")])

# Question 2
print("\nQuestion 2")
print("print([x for x in range (1,50) if x % 3 == 0]): ")
print([x for x in range (1,50) if x % 3 == 0])

# Question 3
print("\nQuestion 3")
mystring = "myString"
print('print([letter for letter in mystring if letter in "aeiouAEIOU"])')
print([letter for letter in mystring if letter in "aeiouAEIOU"])

# Question 4 Part A
print("\nQuestion 4 Part A")
mylist = [17, 13, 12, 15, 16, 11, 14]
print("print([index for index in range(0,len(mylist) - 1) if mylist[index] < mylist[index + 1]])")
print([index for index in range(0,len(mylist) - 1) if mylist[index] < mylist[index + 1]])
print([mylist[index] for index in range(0,len(mylist)) if mylist[index] < mylist[index - 1]])

# Question 4 Part B
print("\nQuestion 4 Part B")
def myfun(mylist):
    print("mylist: ", mylist)
    indexList = [index for index in range(0, len(mylist) - 1) if mylist[index] < mylist[index + 1]]
    print("indexList len: ",len(indexList))
    if len(indexList)==0:
        return -1
    else:
        print(indexList[0])
        print(mylist[indexList[0]])
        return indexList[0]

myfun(mylist)

# Question 5
print("Question 5")
class Element:
    def __init__(self,value):
        self.value = value
        self.indicator = (-1)**value
def main():
    initialArray=[Element(x) for x in range(1,11)]
    print(initialArray[4].value,initialArray[4].indicator)
    valueIndex = [index for index in range(0, len(initialArray)) if initialArray[index].indicator == -1]
    print([initialArray[index].value for index in valueIndex])
main()