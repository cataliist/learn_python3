#!/usr/bin/python3

import athletemodel
import yate
import glob

data_files = glob.glob("data/*.txt")
atheletes = athletemodel.put_to_store(data_files)

print(yate.start_response())


print(yate.include_header("Coach Kelly's List of Atheletes"))

print(yate.start_form("/cgi-bin/generate_timing_data.py"))
print(yate.para("Select an athelete from this list to work with:"))
for each in atheletes:
    print(yate.radio_button("which_athelete",atheletes[each].name))

print(yate.end_form("Select"))    
print(yate.include_footer({"Home": "/index.html"}))
