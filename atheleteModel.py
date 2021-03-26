
import cataliistSanitizer
import cataliistFilePicker
import os
import pickle

os.chdir("data/coach_kelly_updated_data")

def put_to_store(files_list):
    all_atheletes = {}
    for each_file in files_list:
        athelete = cataliistFilePicker.filePicker(each_file)
        all_atheletes[athelete.name] = athelete

    
    try:
        with open("atheleteData.pickle","wb") as all_atheletes_data:
            pickle.dump(all_atheletes,all_atheletes_data)
    except IOError as err:
        print("File Error" +str(err))        
    except PickleError as perr:
        print("Pickling Error" +str(perr))

    return(all_atheletes)


def get_from_store():
    try:
        with open("atheleteData.pickle","rb") as all_atheletes_data:
            all_atheletes = pickle.load(all_atheletes_data)
    except IOError as err:
        print("File Error" +str(err))
    except PickleError as perr:
        print("Pickling Error" +str(perr))            

    return(all_atheletes)    


the_files = ['julie2.txt','james2.txt','mikey2.txt','sarah2.txt']
data = put_to_store(the_files)
#print(data)

data_copy = get_from_store()

for each in data:
    print(data[each].name +"'s DOB is "+data[each].dob)

for each in data_copy:
    print(data_copy[each].name +"'s DOB is "+data_copy[each].dob)    