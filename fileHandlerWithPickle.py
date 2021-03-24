import os
import pickle

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
    with open("man_dialog.pickle","wb") as man_data:
        pickle.dump(man,man_data)    

    with open("other_dialog.pickle","wb") as other_data:
        pickle.dump(other,other_data)
    
except IOError as err:
    print("File Error" + str(err)) 

except pickle.PickleError as perr:
    print("Pickling Error " + str(perr))