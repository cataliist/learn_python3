import random
import os

#print(random.randint(1,9))

def getUserPoint(userName):
    try:
        with open("userScores.txt","r") as userFile:
            userDict = {}
            for each in userFile:
                (name, score) = each.split(",")
                userDict[name] = score
            if userName in userDict.keys():
                return(userDict[userName])
            return("-1")    
    except Exception as err:
        return(err)            



def updateUserPoints(newUser, userName, userScore):
    if newUser:
        try:
            with open("userScores.txt","a") as userFile:
                userFile.write(userName + "," + userScore + "\n")
        except Exception as err:
            return(err)        
    else:
        try:
            with open("userScores.tmp","w") as userFileTmp:
                with open("userScores.txt","r") as userFile:
                    for each in userFile:
                        (name,score) = each.strip().split(",")
                        if name == userName:
                            userFileTmp.write(name + "," + userScore + "\n")
                        else:
                            userFileTmp.write(name + "," + score + "\n")
            os.remove("userScores.txt")
            os.rename("userScores.tmp","userScores.txt")                    
        except Exception as err:
            return(err)                    



def generateQuestion():
    
    operandList = [0,0,0,0,0]
    operatorList = ['','','','']
    operatorDict = {
        1:"+",
        2:"-",
        3:"**",
        4:"*"
    }

    for each in range(0,5):
        operandList[each] = random.randint(1,9)

    counter = 0
    while counter < 4:
        randomInt = random.randint(1,4)
        if counter > 0 and operatorDict[randomInt] == "**" and operatorList[counter-1] == "**":
            operatorList[counter] = operatorDict[1]
        else:
            operatorList[counter] = operatorDict[randomInt]
        counter = counter + 1    

    questionString = ''
    counter = 0
    while counter < 5:
        questionString = questionString + str(operandList[counter])
        if counter < 4:
            questionString = questionString + str(operatorList[counter])
        counter = counter + 1    

    questionString = questionString.replace("**","^")    
    print("\n",questionString)

    userAnswer = input("Answer: ")

    while True:
        try:
            if int(userAnswer) == eval(questionString):
                print("Your answer was correct")
                return(1)
            else:
                print("The correct answer was: " + str(eval(questionString)))
                return(0)               
        except:
            print("Please enter a valid number")
            userAnswer = input("Reenter your answer: ")
    


