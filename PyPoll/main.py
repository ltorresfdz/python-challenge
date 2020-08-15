# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

total_votes = 0
name = []
nombre_candidato =[]
votes={}
porc_primero=0
porc_pri = 0
porc_segundo=0
porc_seg=0
porc_tercero=0
porc_ter=0
porc_cuarto=0
porc_cuar=0
primero =0
segundo =0
tercero =0
cuarto =0
nombres=[]
names=[]
votitos=[]

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
     candidate = {} 
  
     for value in votes.values(): 
  
          # initialize empty list to each key to insert candidate names having same  
          # number of votes  
          candidate[value] = [] 
  
     for (key,value) in votes.items(): 
          candidate[value].append(key)
       # sort keys in descending order to get maximum  value of votes 
     primero = sorted(candidate.keys(),reverse=True)[0] 
     porc_primero = (primero / total_votes)*100
     segundo = sorted(candidate.keys(),reverse=True)[1] 
     porc_segundo = (segundo/total_votes)*100
     tercero = sorted(candidate.keys(),reverse=True)[2]
     porc_tercero =(tercero / total_votes)*100
     cuarto = sorted(candidate.keys(),reverse=True)[3]
     porc_cuarto = (cuarto/total_votes)*100  


        
     print(f'{candidate[primero]}')
     print("{0:.3f}".format(porc_primero)) 
     porc_pri = "{0:.3f}".format(porc_primero)
     print(primero)
     print(f'{candidate[segundo]}')
     print("{0:.3f}".format(porc_segundo))
     porc_seg ="{0:.3f}".format(porc_segundo)
     print(segundo)
     print(f'{candidate[tercero]}')
     print("{0:.3f}".format(porc_tercero))
     porc_ter ="{0:.3f}".format(porc_tercero)
     print(tercero)
     print(f'{candidate[cuarto]}')
     print("{0:.3f}".format(porc_cuarto))
     porc_cuar ="{0:.3f}".format(porc_cuarto)
     print(cuarto)

winner(nombre_candidato)  

 


print("  	Election Results")
print("---------------------------------------")
print(f"Total Votes:  {str(total_votes)}")
print("---------------------------------------")
print(f"Khan: {str(porc_primero)}  %  ( {str(primero)})")
print(f"Correy: {str(porc_segundo)}  %  ( {str(segundo)})")
print(f"Li: {str(porc_tercero)}  %  ( {str(tercero)})")
print(f"O'Tooley: {str(porc_cuarto)}  %  ( {str(cuarto)})")


output1_file = os.path.join("..", "Resources", "resultados_votos.txt")
with open(output1_file, "w") as f:
    f.write("  	Election Results")
    f.write("\n")
    f.write("---------------------------------------")
    f.write("\n")
    f.write(f"Total Votes:  {str(total_votes)}")
    f.write("\n")
    f.write(f"Khan: {str(porc_primero)}  %  ( {str(primero)})")
    f.write("\n")
    f.write(f"Correy: {str(porc_segundo)}  %  ( {str(segundo)})")
    f.write("\n")
    f.write(f"Li: {str(porc_tercero)}  %  ( {str(tercero)})")
    f.write("\n")
    f.write(f"O'Tooley: {str(porc_cuarto)}  %  ( {str(cuarto)})")



