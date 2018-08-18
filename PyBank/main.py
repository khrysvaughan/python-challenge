import os
import csv

resourcefile = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(resourcefile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    #Print Header
    print("Financial Analysis")
    print("----------------------------")

    #The total number of months included in the dataset
    details = list(csvreader)
    rowcount = len(details)
 
    print("Total Months: " + str(rowcount))

    #The total net amount of "Profit/Losses" over the entire period
    netamount = 0
    for row in details:
        netamount += int(row[1])
        
    
    print("Total: $" + str(netamount))