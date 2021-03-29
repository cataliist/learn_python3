#module prime
#function checkPrime

def checkPrime(the_num):
    for each in range(2,the_num):
        if the_num%each == 0:
            return "Not a prime number"
    return "Prime number entered"
 
