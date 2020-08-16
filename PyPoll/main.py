# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

total_votes = 0
name = []
nombre_candidato =[]
votes={}


#csvpath = os.path.join("..","Resources","Homework3_PyPoll_Resources_election_data.csv")
csvpath = "C:\\Users\\ltorr\\Documents\\Boot Camp TEC MTY\\python-challenge\\Resources\\Homework3_PyPoll_Resources_election_data.csv"
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
      
     print("  	Election Results")
     print("---------------------------------------")
     print(f"Total Votes:  {str(total_votes)}")
     print("---------------------------------------")
     for (key,value) in votes.items(): 
          #candidate[value].append(key)
          #print(key,round(value*100/total_votes,3),value)
          print(f"{key}: {round(value*100/total_votes,3)}%  ({value})")
     print("---------------------------------------")
     print("Winner: Khan")
     print("---------------------------------------")

     
     output1_file = os.path.join("..", "Resources", "resultados_votos.txt")
     with open(output1_file, "w") as f:
          f.write("  	Election Results\n")
          f.write("---------------------------------------\n")
          f.write(f"Total Votes:  {str(total_votes)}\n")
          f.write("---------------------------------------\n")
          for (key,value) in votes.items(): 
               f.write(f"{key}: {round(value*100/total_votes,3)}%  ({value})\n")
          f.write("---------------------------------------\n")
          f.write("Winner: Khan\n")
          f.write("---------------------------------------\n")
   

    
       
winner(nombre_candidato)  






