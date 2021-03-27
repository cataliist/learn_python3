
import sqlite3
import glob
import athletemodel

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

data_files = glob.glob("../data/*.txt")
athletes = athletemodel.put_to_store(data_files)

for each in athletes:
    name = athletes[each].name
    dob = athletes[each].dob
    cursor.execute("INSERT INTO athletes (name,dob) VALUES (?,?)",(name,dob))
    connection.commit()

    cursor.execute("SELECT id FROM athletes WHERE name=? AND dob=?",(name,dob))

    the_current_id =  cursor.fetchone()[0]
    
    for each in athletes[each].clean_data:
        cursor.execute("INSERT INTO timing_data (athlete_id,value) VALUES (?,?)",(the_current_id,each))
    connection.commit()    

connection.close()