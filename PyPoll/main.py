# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

total_votes = 0
name = []
nombre_candidato =[]
votes={}
porc_primero=0
porc_segundo=0
porc_tercero=0
porc_cuarto=0
para_imprimir =""

csvpath = os.path.join("..","Resources","Homework3_PyPoll_Resources_election_data.csv")
# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        total_votes= total_votes + 1
        name = (row[2])
        nombre_candidato.append(name)
        
#Counting votes and winner
from collections import Counter 
  
def winner(input): 
  
     # convert list of candidates into dictionary 
     votes = Counter(input) 
       
     # create another dictionary and it's key will 
     # be count of votes values will be name of  
     # candidates 
     dict = {} 
  
     for value in votes.values(): 
  
          # initialize empty list to each key to  
          # insert candidate names having same  
          # number of votes  
          dict[value] = [] 
  
     for (key,value) in votes.items(): 
          dict[value].append(key)
          
  
     # sort keys in descending order to get maximum  
     # value of votes 
     primero = sorted(dict.keys(),reverse=True)[0] 
     porc_primero = (primero / total_votes)*100
     segundo = sorted(dict.keys(),reverse=True)[1] 
     porc_segundo = (segundo/total_votes)*100
     tercero = sorted(dict.keys(),reverse=True)[2]
     porc_tercero =(tercero / total_votes)*100
     cuarto = sorted(dict.keys(),reverse=True)[3]
     porc_cuarto = (cuarto/total_votes)*100  
     print(primero)
     print(f'{dict[primero]}')
     print(porc_primero)
     print(segundo)
     print(f'{dict[segundo]}')
     print(porc_segundo)
     print(tercero)
     print(f'{dict[tercero]}')
     print(porc_tercero)
     print(cuarto)
     print(porc_cuarto)
     print(f'{dict[cuarto]}')

winner(nombre_candidato) 

print("  	Election Results")
print("---------------------------------------")
print(f"Total Votes:  {str(total_votes)}")
print("---------------------------------------")



#print ('%.2f'%a) 
