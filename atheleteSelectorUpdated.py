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


print(julie['name'] + "'s fastest times are: " + str(julie['times']))
print(james['name'] + "'s fastest times are: " + str(james['times']))
print(mikey['name'] + "'s fastest times are: " + str(mikey['times']))
print(sarah['name'] + "'s fastest times are: " + str(sarah['times']))

"""
sarah_dict = {}
sarah_dict['name'] = sarah.pop(0)
sarah_dict['dob'] = sarah.pop(0)
sarah_dict['timing'] = sarah

print(sarah_dict['name'] + "'s fastest times are: " + str(sorted(set([cataliistSanitizer.sanitize(each) for each in sarah_dict['timing']]))[0:3]))
#(name,dob) = sarah.pop(0),sarah.pop(0)
#print(name + "'s fastest times are: " + str(sorted(set([cataliistSanitizer.sanitize(each) for each in sarah]))[0:3]))


#print(sorted(set([cataliistSanitizer.sanitize(each) for each in julie]))[0:3])
#print(sorted(set([cataliistSanitizer.sanitize(each) for each in james]))[0:3])
#print(sorted(set([cataliistSanitizer.sanitize(each) for each in mikey]))[0:3])
#print(sorted(set([cataliistSanitizer.sanitize(each) for each in sarah]))[0:3])



"""
