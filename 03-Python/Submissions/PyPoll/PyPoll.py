#PyPoll Code

#Loading the file
import csv

csvpath = "PyPoll/Resources/election_data.csv"

#Initial Settings starting at zero
totalVotes = 0

#Opening and reading the file
with open(csvpath, "r") as file:

    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

    print(csvheader)
    print()

for row in csvheader:
    #print(row)
    
    totalVotes += 1
print(totalVotes)