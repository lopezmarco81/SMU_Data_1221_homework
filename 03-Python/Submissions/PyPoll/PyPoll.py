#Importing dependencies
import csv

#File path's 
csvpath = "PyPoll/Resources/election_data.csv"

#Counting total votes starting at zero
totalVotes = 0

#creating a dictionary data structure
candidate_dict2 = {
"Khan": 0,
"Correy": 0,
"Li": 0,
"O'Tooley":0
}

#Opening and Reading file
with open(csvpath, "r") as file:

    csvreader = csv.reader(file, delimiter=',')
    
    csvheader = next(csvreader)
    
    print(csvheader)
    print()
    
  #Iterating ("Looping") through the rows - Not printing the rows because it is massive (3.5m)
    for row in csvreader:
     # print(row)

#Adding one vote to each row of total votes
      totalVotes += 1

#If candidate does not exist in list
      if row[2] not in candidate_dict2:
            candidate_dict2.append(row[2])

#Per Alexander's suggestion, this is assuming the candidate is the in the list      
      candidate_dict2[row[2]] += 1

#If candidate exists, add 1 to value
      if row[2] in candidate_dict2.keys():
            candidate_dict2[row[2]] += 1
      else:
            candidate_dict2[row[2]] = 1

#Printouts
print(totalVotes)
print()
print(candidate_dict2)
print()

#Getting key with maximum value in dictionary
max_cand = max(candidate_dict2, key=candidate_dict2.get)
max_votes = candidate_dict2[max_cand]

#Summary printout


summary = f"""Poll Results
--------------------------
Total Votes: {totalVotes}
--------------------------\n"""

for person in candidate_dict2.keys():
    prcnt = 100*(candidate_dict2[person] / totalVotes)
    summary += f"{person}: {round(prcnt,2)}% ({candidate_dict2[person]})\n"

summary += f"""--------------------------------------
    Elected:  {max_cand}
--------------------------------------
    """

print(summary)

#write to file
with open("PyPoll_Analysis.txt", "w") as file:
      file.write(summary)