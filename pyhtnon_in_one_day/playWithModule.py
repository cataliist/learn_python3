import sys
sys.path.append("modules")

"""
Note: sys.path is system path for all the modules of python
which means whenever we import python inbuilt modules it searchs at system path

sys.path.append() add our module "prime.py" path to the system path list
"""

import prime

myNum = int(input("Enter a prime number: "))
print(prime.checkPrime(myNum))
