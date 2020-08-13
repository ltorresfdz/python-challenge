# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join("..", "Resources","Homework3_PyBank_Resources_budget_data.csv")


# Lists to store data
Changes = []
num_meses = 0
# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
         num_meses= num_meses + 1
print(num_meses)




# Function that returns the arithmetic average for a list of numbers
#def average(numbers):
    #length = len(numbers)
    #total = 0.0
    #for number in numbers:
    #    total += number
    #return total / length


# Test your function with the following:
#print(average([1, 5, 9]))
#print(average(range(11)))



# with open(udemy_csv, encoding='utf-8') as csvfile:
#with open(udemy_csv,encoding='utf-8') as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    #for row in csvreader:
        # Add title
        #title.append(row[1])

        # Add price
        #price.append(row[4])

                # Determine percent of review left to 2 decimal places
        #percent = round(int(row[6]) / int(row[5]), 2)
        #review_percent.append(percent)



# Specify the file to write to
#output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    #csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
print("si funciono")


# Set variable for output file
#output_file = os.path.join("web_final.csv")

#  Open the output file
#with open(output_file, "w") as datafile:
    #writer = csv.writer(datafile)

    # Write the header row
    #writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     #"Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    #writer.writerows(cleaned_csv)



   
    # Print out the wrestler's name and their percentage stats
    #print(f"Stats for {name}")
    #print(f"WIN PERCENT: {str(win_percent)}")
    #print(f"LOSS PERCENT: {str(loss_percent)}")
    #print(f"DRAW PERCENT: {str(draw_percent)}")
    #print(f"{name} is a {type_of_wrestler}")