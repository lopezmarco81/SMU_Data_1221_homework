#Importing dependencies
import csv

#File path's 
csvpath = "PyPoll/Resources/election_data.csv"

#Counting total votes starting at zero
totalVotes = 0

#Initializing a set - unique list
candidates = set()

#Opening and Reading file
with open(csvpath, "r") as file:

    csvreader = csv.reader(file, delimiter=',')
    
    csvheader = next(csvreader)
    
    print(csvheader)
    print()
    
  #Iterating ("Looping") through the rows - Not printing the rows because it is massive
    for row in csvreader:
     # print(row)

#Adding a one to each row of total votes
      totalVotes += 1
#Adjoining Index 2 (Candidates Column) the unique list to the set
      candidates.add(row[2])

#Printouts
print(totalVotes)
print(candidates)