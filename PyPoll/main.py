# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

total_votes = 0
last_name =[]
name = []
nombre_completo = ""
nombre_candidato =[]


csvpath = os.path.join("..","Resources","Homework3_PyPoll_Resources_election_data.csv")
# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        total_votes= total_votes + 1
        #last_name =(row[1])
        name = (row[2])
        #nombre_completo = last_name + name
        nombre_candidato.append(nombre)
        
print(total_votes)

        