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

#to change value
myDict["China"] = "Beijing"
print("China's capital is: " + myDict["China"])

#add new item to the dictionary
myDict["Australia"] = "Sydney"
print(myDict)

#remove element from the dictionary
del myDict["China"]
print(myDict)