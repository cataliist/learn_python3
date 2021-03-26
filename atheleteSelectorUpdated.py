import os
import cataliistSanitizer
import cataliistFilePicker


class Athelete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return(sorted(set([cataliistSanitizer.sanitize(each) for each in self.times]))[0:3])

    def add_time(self,new_time):
        self.times.append(new_time)

    def add_times(self,new_time=[]):
        self.times.extend(new_time)



def filePicker(file):
    try:
        with open(file) as fh:
            data = fh.readline().strip().split(',')
            return(Athelete(data.pop(0),data.pop(0),data))
    except IOError as err:
        print("File Error" +str(err))
        return(None)  



os.chdir('data/coach_kelly_updated_data')

try:
    julie = filePicker("julie2.txt")
    #james = cataliistFilePicker.filePicker("james2.txt")
    #mikey = cataliistFilePicker.filePicker("mikey2.txt")
    #sarah = cataliistFilePicker.filePicker("sarah2.txt")
    
except IOError as err:
    print("File Error" +str(err))        

julie.add_time("2.99")
julie.add_times(["5.99","1-99"])

print(julie.times)
print(julie.name + "'s fastest times are: " + str(julie.top3()))
#print(james['name'] + "'s fastest times are: " + str(james['times']))
#print(mikey['name'] + "'s fastest times are: " + str(mikey['times']))
#print(sarah['name'] + "'s fastest times are: " + str(sarah['times']))

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
