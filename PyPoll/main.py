import os
import csv

resourcefile = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(resourcefile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    #Print Header
    print("Election Results")
    print("-------------------------")

    #Print Total Votes
    totalvotes = 0
    votes = list(csvreader)
    totalvotes = sum(1 for row in votes)
    print("Total Votes: " + str(totalvotes))
    print("-------------------------")

    # A complete list of candidates who received votes
    # The total number of votes each candidate won
    candidates = []
    votepercandidate = {}
    count = 0
    for i in range(int(totalvotes)):
        if votes[i][2] not in candidates:
            candidates.append(votes[i][2])
            votepercandidate[votes[i][2]] = 1
        elif votes[i][2] in votepercandidate:
            votepercandidate[votes[i][2]] += 1

    # The percentage of votes each candidate won
    # The winner of the election based on popular vote
    percentagevotes = []
    winner = 0
    winningcand = ""
    for cand,votes in votepercandidate.items():
        percentvote = votes/totalvotes
        if percentvote > winner:
            winningcand = cand
            winner = percentvote
        votepercandidate[cand] = [votes] + ["{:.3%}".format(percentvote)]

    for vote in votepercandidate:
        print(f"{vote}: {votepercandidate[vote][1]} ({votepercandidate[vote][0]})")

    print("-------------------------")
    print("Winner: " + winningcand)
    print("-------------------------")

    #Export a text file with the results
    filepath = "output/election_data_results.txt"
    with open(filepath, "w") as txtfile:
        txtfile.write("Election Results \n")
        txtfile.write("---------------------------- \n")
        txtfile.write("Total Votes: " + str(totalvotes) + "\n")
        txtfile.write("---------------------------- \n")
        for vote in votepercandidate:
            txtfile.write(vote + ": " + str(votepercandidate[vote][1] )+ " (" + str(votepercandidate[vote][0]) + ") \n")
        txtfile.write("---------------------------- \n")
        txtfile.write("Winner: " + winningcand + "\n")
        txtfile.write("---------------------------- \n")