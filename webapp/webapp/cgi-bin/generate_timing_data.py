#!/usr/bin/python3

import athletemodel
import yate
import cgi
import cgitb
cgitb.enable()

form_data = cgi.FieldStorage()

athelete_name = form_data['which_athelete'].value

atheletes = athletemodel.get_from_store()

print(yate.start_response())


print(yate.include_header("Coach Kelly's Timing Data"))

print(yate.header("Timing data for :" + athelete_name + ", DOB: " + atheletes[athelete_name].dob))
print(yate.para("The top times for this athelete are:"))

print(yate.u_list(atheletes[athelete_name].top3))
print(yate.include_footer({"Home": "/index.html","Select Another Athelete": "/cgi-bin/generate_list.py"}))
