#define a function using def keyword

def checkPrime(the_num):
    for each in range(2,the_num):
        if the_num%each == 0:
            return "Not a prime number"
    return "Prime number entered"

myNum = int(input("Enter a prime number: "))
print(checkPrime(myNum))

"""
Note: any function can return one value and with first return function exits
Here first return is in if condition, if condition matched return will be taken and function exits with the message "Not a prime number"
If condition not mached loop will be ended and second return will be taken and function exits with the message "Prime number entered"
""" 
