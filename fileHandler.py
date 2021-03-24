import os

os.getcwd()
os.chdir('data')
os.getcwd()

try:
    data = open("sketch.txt")

    for each in data:
        try:
            (role, dialog) = each.split(':')
            print(role,end='')
            print(" said: ",end='')
            print(dialog,end='')
        except ValueError:
            pass

    data.close()        
except IOError:
    print("The input file is missing!")