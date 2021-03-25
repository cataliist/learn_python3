import os


os.chdir('data/coach_kelly')

julie=[]
james=[]
sarah=[]
mikey=[]
cjulie=[]
cjames=[]
csarah=[]
cmikey=[]


try:
    with open("julie.txt") as julief:
        data = julief.readline()
        julie = data.strip().split(',')
        

    with open("james.txt") as jamesf:
        data = jamesf.readline()
        james = data.strip().split(',')

    with open("mikey.txt") as mikeyf:
        data = mikeyf.readline()
        mikey = data.strip().split(',')  

    with open("sarah.txt") as sarahf:
        data = sarahf.readline()
        sarah = data.strip().split(',')

except IOError as err:
    print("File Error" +str(err))        


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    

    (min,sec) = time_string.split(splitter)
    return(min + '.' + sec)




for each in julie:
    cjulie.append(sanitize(each))

for each in james:
    cjames.append(sanitize(each))

for each in mikey:
    cmikey.append(sanitize(each))

for each in sarah:
    csarah.append(sanitize(each))

print(sorted(cjulie))
print(sorted(cjames))
print(sorted(cmikey))
print(sorted(csarah))