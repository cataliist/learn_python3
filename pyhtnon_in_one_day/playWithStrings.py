#Assign a string value to a variable
myString = "This is cataliister speaking, I am pushing python tutorial to github using a feature branch 'python in one day'."

#Display content of myString on STDOUT (your terminal) by default
print(myString)

#Assigning another string to an another variable
myAnotherString = "Isn't it cool!"

#Concatenate strings using "+" operator
myConcatenatedString = myString + " " + myAnotherString
print(myConcatenatedString)

'''
Using python's BIFs (Built In Functions) for string
'''

#Count the number of occurance for a keyword in the string
keyword = "cataliister"
count = myConcatenatedString.count(keyword)
print(keyword + " found " + str(count) +" time(s) in above string.")

#Check if string is starts with specific preffix
preffix = ">"
check = myConcatenatedString.startswith(preffix)
print("String starts with '" + preffix + "':" + str(check))


#Check if string is ends with specific suffix
suffix = "!"
check = myConcatenatedString.endswith(suffix)
print("String ends with '" + suffix + "':" + str(check))


#Find the keywork position in string
keyword = "cataliister"
find = myConcatenatedString.find(keyword)
print(keyword + "is at index " + str(find) + " in the string.")

#Join elements of list, tuple or string and return as a string
delimitter = "-"
myTuple = ("This","is","tuple")
myList = ["This","is","list"]
myString = "This is string"
print(str(delimitter.join(myTuple)))
print(str(delimitter.join(myList)))
print(str(delimitter.join(myString)))


#replace keyword1 in string with keyword2
keyword1 = "python"
keyword2 = "python3"
#Replace all occurance
print(str(myConcatenatedString.replace(keyword1,keyword2)))
#Replace first occurance
print(str(myConcatenatedString.replace(keyword1,keyword2,1)))


#split string with delimiter return a list
delimitter = ","
myList = myConcatenatedString.split(delimitter)
print(myList)


#Remove leading and trailing whitespaces from the string
myConcatenatedStringWithSpace = "     " + myConcatenatedString
print(myConcatenatedStringWithSpace)
print(myConcatenatedStringWithSpace.strip())

#Convert string to all upper case
print(myConcatenatedString.upper())

#Convert string to all lower case
print(myConcatenatedString.lower())