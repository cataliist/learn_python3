"""
Disclaimer: Most common functions are demostrated
"""

#Declare an empty list
myList = []

#Decalre a list with values
myList = ["Lets", "start", "python", "programming", "on a count of", 1, 2, 3, 4, 5]

#print myList
print(myList)

#print first item of list
print(myList[0])

#print second item of list
print(myList[1])

#print last item of list
print(myList[-1])

#print second last item of list
print(myList[-2])

#slice list from 0 to 3 index
print(myList[0:4])
"""
Note that last index of slice will not be included
"""

#stepper in slice
print(myList[0: :2])
"""
"0" => first argument means the slicing start point/index
" " => second argument blank means slicing will be done to the last item of the list
"2" => third argument set a stepper that is every 2nd item will be included between the range
"""

#change or modify list item
myList[2] = "python3"
print(myList)

#add single item in the list
myList.append(6)
print(myList)

#add multiple items to the list
myList.extend([7,8,9,10])
print(myList)

#remove item from the list
del myList[3]
print(myList)

#chek if an item is in the list
print(11 in myList)
print(10 in myList)

#insert item to a particular position
myList.insert(3,"programming")
print(myList)

#lenght of the list or number of items in the list
print(len(myList))

#remove last item from the list
print("last item was: " + str(myList.pop()))
print(myList)

#remove item from the list by its value
myList.remove("python3")
print(myList)

#reverse the items in the list
myList.reverse()
print(myList)

#sort the list
myNewList = myList[:9]
print(myNewList)
myNewList.sort()
print(myNewList)

#sort the list using sorted
mySortedList = sorted(myList[:9])
print(mySortedList)