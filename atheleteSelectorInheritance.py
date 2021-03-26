import os
import cataliistSanitizer
import cataliistFilePicker


os.chdir('data/coach_kelly_updated_data')

try:
    julie = cataliistFilePicker.filePicker("julie2.txt")
    james = cataliistFilePicker.filePicker("james2.txt")
    mikey = cataliistFilePicker.filePicker("mikey2.txt")
    sarah = cataliistFilePicker.filePicker("sarah2.txt")
    
except IOError as err:
    print("File Error" +str(err))        

julie.append("2.99")
julie.extend(["5.99","1-99","0:99"])

print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(james.name + "'s fastest times are: " + str(james.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
