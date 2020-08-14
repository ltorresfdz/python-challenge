# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

num_meses = 0
total_profit_loss = 0
x=0
y=0
fechas = []
gan_per = []
diff_list = [] 

csvpath = os.path.join("..", "Resources","Homework3_PyBank_Resources_budget_data.csv")
# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        num_meses= num_meses + 1
        total_profit_loss += float( row[1])
        fechas.append(row[0])
        gan_per.append(float(row[1]))        

total_profit_loss =round(total_profit_loss)
# Calculating difference list 
for x, y in zip(gan_per[0:], gan_per[1:]): 
   diff_list.append(y-x) 
   
      
# printing difference list 
#print ("difference list: ", str(diff_list)) 


# Function that returns the arithmetic average for a list of numbers

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

Promedio_cambio = average(diff_list)
Promedio_cambio = round(Promedio_cambio,2)
Maximo_cambio = 0
Minimo_cambio = 0
Posicion_mayor = 0
Posicion_menor = 0

for cambio in range(0,len(diff_list)):
    if diff_list[cambio]> Maximo_cambio:
            Maximo_cambio = diff_list[cambio]
            Posicion_mayor = cambio + 1

for cambio in range(0,len(diff_list)):
    if diff_list[cambio]< Minimo_cambio:
            Minimo_cambio = diff_list[cambio]
            Posicion_menor = cambio + 1

Maximo_cambio = round(Maximo_cambio)
Minimo_cambio = round(Minimo_cambio)

print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months:  {str(num_meses)}")
print(f"Total: ${str(total_profit_loss)}")
print(f"Average  Change: $ {str(Promedio_cambio)}")
print(f"Greatest Increase in Profits: {str(fechas[Posicion_mayor])}  (${str(Maximo_cambio)})")
print(f"Greatest Decrease in Profits : {str(fechas[Posicion_menor])}  (${str(Minimo_cambio)})")

linea1 = "Total Months:  str(num_meses)"

output1_file = os.path.join("..", "Resources", "resultados.txt")
with open(output1_file, "w") as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("---------------------------------------")
    f.write("\n")
    f.write(f"Total Months:  {str(num_meses)}")
    f.write("\n")
    f.write(f"Total: ${str(total_profit_loss)}")
    f.write("\n")
    f.write(f"Average  Change: $ {str(Promedio_cambio)}")
    f.write("\n")
    f.write(f"Greatest Increase in Profits: {str(fechas[Posicion_mayor])}  (${str(Maximo_cambio)})")
    f.write("\n")
    f.write(f"Greatest Decrease in Profits : {str(fechas[Posicion_menor])}  (${str(Minimo_cambio)})")



Archivo_resultado = zip(fechas, gan_per)   
# Set variable for output file
output_file = os.path.join("..", "Resources", "resultados.csv")
#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Date", "Increase/Decrease"])
    # Write in zipped rows
    writer.writerows(Archivo_resultado)





   
 