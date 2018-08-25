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

    #The average change in "Profit/Losses" between months over the entire period
    # Find change per month
    diffmonths = 0
    avgchange = []
    avgmonths = 0
    sumchange = 0
    for i in range(rowcount):
        if i == 0:
            avgchange.append(0)
        else:
            diffmonths = (int(details[i][1]) - int(details[i-1][1]))
            avgchange.append(diffmonths)
            
    # Add the differences
    for i in range(rowcount):
        sumchange += int(avgchange[i])

    # Find the average
    avgmonths = sumchange/ int(rowcount -1)
    
    print("Average Change: $" + str(round(avgmonths,2)))

    #The greatest increase in profits (date and amount) over the entire period
    greatincvalue = max(avgchange)
    greatincindex = avgchange.index(greatincvalue)
    greatincmonth = details[greatincindex][0]

    print("Greatest Increase in Profits: " + greatincmonth + " ($" + str(greatincvalue) + ")")

    #The greatest decrease in losses (date and amount) over the entire period
    greatdecvalue = min(avgchange)
    greatdecindex = avgchange.index(greatdecvalue)
    greatdecmonth = details[greatdecindex][0]

    print("Greatest Decrease in Profits: " + greatdecmonth + " ($" + str(greatdecvalue) + ")")

    #Export a text file with the results
    
