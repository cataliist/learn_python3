import os
import pickle
import cataliistNester

os.getcwd()
os.chdir('data')
os.getcwd()

man=[]

try:
    with open("man_dialog.pickle", 'rb') as man_data:
        man = pickle.load(man_data)
except IOError as err:
    print("File Error" +str(err))
except pickle.PickleError as perr:
    print("Picking Error" +str(perr))

cataliistNester.nested(man)