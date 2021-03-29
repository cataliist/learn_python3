"""
Disclaimer: Most common tricks are demostrated for input (getting input from the terminal) and print (display results on terminal as default)
"""

#Get below details from user through terminal
myCompany = input("Where are you working?\n")
myDesignation = input("What is your designation?\n")

#Print whatever has inputted
print("Hey there, I'm working at " + myCompany + " as " + myDesignation + "!")
print("Hey there, I'm working at %s as %s!" %(myCompany, myDesignation)) #cataliister's choice
print("Hey there, I'm working at {} as {}!".format(myCompany, myDesignation))
print(
"""
Hey there, 
I'm working at %s as %s!
""" 
%(myCompany, myDesignation)
)


