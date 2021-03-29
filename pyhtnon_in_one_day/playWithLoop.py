"""
Disclaimer: for while
"""

#iterations can be worked on string, tuple, list or dictionary
myString = "this is a string"
myTuple = ("this","is","tuple")
myList = ["this","is","list"]
myDict = {
    0:"this",
    1:"is",
    2:"dictionary"
}


#iterate through all above data types

#for loop
for each in myString:
    print(each)

for each in myTuple:
    print(each)

for each in myList:
    print(each)

for each in myDict:
    print(myDict[each])

#for loop comprehansion
[print(each) for each in myString]
[print(each) for each in myTuple]
[print(each) for each in myList]
[print(myDict[each]) for each in myDict]

#while loop
counter = 0
while counter<len(myList):
    print(myList[counter])
    counter = counter + 1        

#for loop using range
for each in range(1,11):
    print(each)

#break (exit the loop if certain condition matched)
for each in range(1,11):
    if each==5:
        break
    else:
        print(each)

#continue (skip the particular iteration in the loop if certain condition matched and continue the loop)
for each in range(1,11):
    if each==5:
        continue
    else:
        print(each)        



