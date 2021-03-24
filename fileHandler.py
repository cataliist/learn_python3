import os
import cataliistNester

os.getcwd()
os.chdir('data')
os.getcwd()

man=[]
other =[]

try:
    with open("sketch_r1.txt") as data:
        for each in data:
            try:
                (role, dialog) = each.split(':',1)
                dialog = dialog.strip()
                
                if role=='Man':
                    man.append(dialog)
                elif role == 'Other Man':
                    other.append(dialog)    

            except ValueError:
                pass
        
except IOError as err:
    print("File Error" + str(err))

try:
    with open("man_dialog.txt","w") as man_data:
        cataliistNester.nested(man,fh=man_data)    

    with open("other_dialog.txt","w") as other_data:
        cataliistNester.nested(other,fh=other_data)
    
except IOError as err:
    print("File Error" + str(err)) 
