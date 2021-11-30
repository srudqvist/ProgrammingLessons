### 
### Programming Lessons 5: Reading from a CSV file, sorting objects by an attribute, 
### and writing to a .txt file
###
### Author: Samuel Rudqvist
###



class MyData:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    


def readData():
    dataFile = open("Lesson5CSV.csv","r")
    #print(dataFile.read())
    objectList = []
    for line in dataFile:
        thisLine = line.split(",")
        name = thisLine[0]
        number = int(thisLine[1])
        objectList.append(MyData(name, number))
    dataFile.close()
    return objectList


def readDataTest():
    testList = readData()
    for i in range(len(testList)):
        print(testList[i].name + ",", testList[i].number)

def sortByName():
    myList = readData()
    for index in range(1, len(myList)):
        temp = myList[index]
        secondIndex = index - 1

        while secondIndex >= 0 and myList[secondIndex].name > temp.name:
            myList[secondIndex + 1] = myList[secondIndex]
            secondIndex = secondIndex - 1
        myList[secondIndex + 1] = temp

    for item in myList:
        print(item.name, item.number)

def sortByNumbers():
    myList = readData()
    for index in range(1, len(myList)):
        temp = myList[index]
        secondIndex = index - 1

        while secondIndex >= 0 and myList[secondIndex].number > temp.number:
            myList[secondIndex + 1] = myList[secondIndex]
            secondIndex = secondIndex - 1
        myList[secondIndex + 1] = temp
    
    for item in myList:
        print(item.name, item.number)

def writeToTextfile():
    results = open("Lesson5results.txt", "w")
    myList = readData()
    for index in range(5):
        results.write(myList[index].name + "\n")
    results.close()


def test():
    new = MyData("David", 68)
    print(new.name, new.number)


#test()
#readDataTest()
#sortByName()
sortByNumbers()
writeToTextfile()