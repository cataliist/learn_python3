"""
Disclaimer: if elif else and inline if
"""

#user input
userInput = input("Enter \"1\" or \"2\"\n")


#if elif and else
if userInput == "1":
    print("You have entered: " + userInput)
elif userInput == "2":
    print("You have entered: " + userInput)
else:
    print("Invalid input given!")

#inline if
print("You have entered: " + userInput) if userInput=="1" or userInput=="2" else print("Invalid input given!")            