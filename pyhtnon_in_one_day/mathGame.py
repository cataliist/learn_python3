try:
    import os
    import sys
    sys.path.append("modules")
    from myPythonFunctions import getUserPoint, updateUserPoints, generateQuestion

    userName = input("Enter your user name: ")
    
    if getUserPoint(userName) == -1:
        newUser = True

    userChoice = 0
        

except Exception as err:
    print("Unknown Error: " + str(err))
