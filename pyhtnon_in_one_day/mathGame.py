try:
    import os
    import sys
    sys.path.append("modules")
    from myPythonFunctions import getUserPoint, updateUserPoints, generateQuestion

    userName = input("Enter your user name: ")
    
    if getUserPoint(userName) == "-1":
        newUser = True
    else:
        newUser = False    

    userChoice = ''
    userScore = 0
    while userChoice != "-1":
        userScore = userScore + generateQuestion()
        userChoice = input("Enter -1 to exit the game or press any key to continue: ")
    
    updateUserPoints(newUser,userName,str(userScore))         

except Exception as err:
    print("Unknown Error: " + str(err))


