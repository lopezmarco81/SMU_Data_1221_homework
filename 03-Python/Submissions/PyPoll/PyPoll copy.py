#Importing dependencies
import csv

#File path's 
csvpath = "PyPoll/Resources/election_data.csv"


#Opening and Reading file
with open(csvpath, "r") as file:
    csvreader = csv.reader(file, delimiter=',')
    
    csvheader = next(csvreader)
    
    print(csvheader)
    print()
    
  #Iterating ("Looping") through the rows  
    for row in csvreader:
  #Not printing the rows because it is massive
        print(row)