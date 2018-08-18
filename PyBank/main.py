import os
import csv

resourcefile = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(resourcefile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

    #Print Header
    print("Financial Analysis")
    print("----------------------------")

    #The total number of months included in the dataset
    details = list(csvreader)
    rowcount = len(details)

    print("Total Months: " + str(rowcount))