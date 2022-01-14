#Importing dependencies
import csv

#File path's 
csvpath = "PyPoll/Resources/election_data.csv"

totalVotes = 0

#Creating the entire list of contenders
contender = set()

#Creating a dictionary structure.
# Per Alexander's comment, this requires for you to know your data before setting this up
# contender_dict = {
#     "Khan": 0,
#     "Correy": 0,
#     "Li": 0,
#     "O'Tooley":0
# }
#Per Alexander, you can create an open dictionary to include any new candidates
contender_dict = {}


#Opening and Reading file
with open(csvpath, "r") as file:
    csvreader = csv.reader(file, delimiter=',')
    
    csvheader = next(csvreader)
    
    print(csvheader)
    #print()
    
  #Iterating ("Looping") through the rows  
    for row in csvreader:
        #print(row)
        
        totalVotes += 1
        
        #Adding Index 2
        contender.add(row[2])

    #Per Alexander's suggestion use the simplified instead of the Ifs' statements   
        contender_dict[row[2]] +=1

    # if row[2] == "Khan":
    #     contender_dict["Khan"] +=1

    # elif row[2] == "Correy":
    #     contender_dict["Correy"] +=1
    
    # elif   row[2] == "Li":
    #     contender_dict["Li"] +=1
    
    # else:  row[2] == "O'Tooley"
    # contender_dict["O'Tooley"] +=1   
    # 
    if row[2] in contender_dict.keys():
      contender_dict[row[2]] += 1
    else:
        contender_dict[row[2]]

        
#Print outs
print(totalVotes)
print(contender)