"""
Disclaimer: Most common functions are demostrated
"""

#Declare an empty dictionary
myDict = {}

#Decalre a dictionary with values
#Dictionary {Key:Value}
myDict = {
    "India": "New Delhi",
    "America": "Washington DC",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "China": "Shanghai" 
}
#print myList
print(myDict)

#get India's capital
print("India's capital is: " + myDict["India"])
#get item using get()
print("India's capital is: " + myDict.get("India"))
#if key is not defined it returns None
print("Sweden's capital is: " + str(myDict.get("Sweden")))
#if key is not defined it returns defined value given as second argument
print("Sweden's capital is: " + str(myDict.get("Sweden","Not Found")))

#to change value
myDict["China"] = "Beijing"
print("China's capital is: " + myDict["China"])

#add new item to the dictionary
myDict["Australia"] = "Sydney"
print(myDict)

#remove element from the dictionary
del myDict["China"]
print(myDict)
#delete entire dictionary
myNewDict = myDict
del myNewDict


#check item in dictionary
print("India" in myDict)
print("New Delhi" in myDict.values())

#get dictionary keys
print(myDict.keys())

#get dictionary values
print(myDict.values())


#length of dictionary / number of items in the dictionary
print(len(myDict))

#update dictionary (works as extention of list)
myDict2 = {
    "Sweden": "Stockholm",
    "S.Korea": "Seol",
    "India": "New Delhi"
}
myDict.update(myDict2)
print(myDict)
"""
Note: repeated (redundant) key will be ignored. In this case India
"""


