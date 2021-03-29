import os #python module to interact with operating system
os.chdir("data")
import time

#open file 
myFile = open("dummyData.txt","r")

#print first line of the file and remove it
print(myFile.readline())

#read limited bytes at a time and remove it 
print(myFile.read(8))

#convert whole file as list and each line as its item
myList = myFile.readlines()
print(myList)

#writing to a file
try:
    with open("dummyData.txt","a") as myFile: 
        """
        second argument: 
        "r" - reading; 
        "w" -> writing; 
        "w+" -> if file not exist creat new and write; 
        "a" -> append existing file; 
        "r+" -> readable and writable (append)
        """
        print("\nThis line has been added at " + str(time.asctime(time.localtime())) + ".", file=myFile)
except Exception as err:
    print("Unknown Error: " +str(err))

#close file
myFile.close()

#open file again
try:
    with open("dummyData.txt","r+") as myFile:
        [print(each) for each in myFile]
        myFile.write("I love python .... PYTHON3!")

except Exception as err:
    print("Unknown Error: " + str(err))        
