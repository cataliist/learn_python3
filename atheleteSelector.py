import os
import cataliistSanitizer
import cataliistFilePicker




os.chdir('data/coach_kelly')

julie=[]
james=[]
sarah=[]
mikey=[]

try:
    julie = cataliistFilePicker.filePicker("julie.txt")
    james = cataliistFilePicker.filePicker("james.txt")
    mikey = cataliistFilePicker.filePicker("mikey.txt")
    sarah = cataliistFilePicker.filePicker("sarah.txt")
    
except IOError as err:
    print("File Error" +str(err))        




print(sorted(set([cataliistSanitizer.sanitize(each) for each in julie]))[0:3])
print(sorted(set([cataliistSanitizer.sanitize(each) for each in james]))[0:3])
print(sorted(set([cataliistSanitizer.sanitize(each) for each in mikey]))[0:3])
print(sorted(set([cataliistSanitizer.sanitize(each) for each in sarah]))[0:3])


"""
julie = sorted([sanitize(each) for each in julie])
james = sorted([sanitize(each) for each in james])
mikey = sorted([sanitize(each) for each in mikey])
sarah = sorted([sanitize(each) for each in sarah])

unique_julie=[]
unique_james=[]
unique_mikey=[]
unique_sarah=[]

for each in julie:
    if each not in unique_julie:
        unique_julie.append(each)

for each in james:
    if each not in unique_james:
        unique_james.append(each)

for each in mikey:
    if each not in unique_mikey:
        unique_mikey.append(each)

for each in sarah:
    if each not in unique_sarah:
        unique_sarah.append(each)

print(unique_julie[0:3])
print(unique_james[0:3])
print(unique_mikey[0:3])
print(unique_sarah[0:3])
"""

