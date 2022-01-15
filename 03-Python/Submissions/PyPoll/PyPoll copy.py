#Importing dependencies
import csv

#File path's 
csvpath = "PyPoll/Resources/election_data.csv"

#Counting total votes starting at zero
totalVotes = 0

#Initializing a set - unique list
candidates = set()

#creating a dictionary data structure
candidate_dict = {
      "Correy": 0,
      "Li": 0,
      "O'Tooley": 0,
      "Khan": 0
}

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

#Adjoining Index 2 (Candidates Column) as a unique list to the set
      candidates.add(row[2])

#Per Alexander's suggestion, this is assuming the candidate is the in the list      
      candidate_dict[row[2]] += 1

#Printouts
print(totalVotes)
print(candidates)
print(candidate_dict)