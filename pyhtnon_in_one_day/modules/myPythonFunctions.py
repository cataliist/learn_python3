import random
import os

#print(random.randint(1,9))

def getUserPoint(userName):
    try:
        with open("userScores.txt","r") as userFile:
            userDict = {}
            for each in userFile:
                (name, score) = each.strip().split("\t")
                userDict[name] = score
            if userDict[userName]:
                return(userDict[userName])
            return("-1")    
    except Exception as err:
        return(err)            