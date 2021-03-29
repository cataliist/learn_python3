"""
Exception handling with try, except and with
"""

#devide and integer with zero
#myNum = 10/0
#print(myNum) #will give you ZeroDivisionError

try:
    myNum = 10/0
    print(myNum)
except Exception as err:
    print("Unknown Error: " + str(err))

try:
    with open("cataliister.py") as ii: #with is used to close the opend file even the exception happened
        myFile = ii

except Exception as err:
    print("Unknown Error: " + str(err))        

try:
    myInt = int(input("Enter a number: "))
    print(myInt*5)
except Exception as err:
    print("Unknown Error: " + str(err))        