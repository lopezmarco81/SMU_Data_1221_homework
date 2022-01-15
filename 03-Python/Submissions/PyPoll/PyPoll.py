#Importing dependencies
import csv

#File path's 
csvpath = "PyPoll/Resources/election_data.csv"

totalVotes = 0
contenders = 0

#Creating the entire list of contenders
contenders = set()
contenders2 = []


#Creating a dictionary structure.
# Per Alexander's comment, this requires for you to know your data before setting this up
# contender_dict = {
#     "Khan": 0,
#     "Correy": 0,
#     "Li": 0,
#     "O'Tooley":0
# }
#Per Alexander, you can create an open dictionary to include any new candidates
contenders_dict = {}


#Opening and Reading file
with open(csvpath, "r") as file:
    csvreader = csv.reader(file, delimiter=',')
    
    csvheader = next(csvreader)
    
    print(csvheader)
    print()
    
  #Iterating ("Looping") through the rows  
    for row in csvreader:

  #Not printing the rows because it is massive
        #print(row)
        
        totalVotes += 1
        
        #Adding Index 2
        contenders.add(row[2])

        if row[2] not in contenders2:
            contenders2.append(row[2])

    #Per Alexander's suggestion use the simplified instead of the Ifs' statements   
        #contender_dict[row[2]] +=1

    # if row[2] == "Khan":
    #     contender_dict["Khan"] += 1

    # elif row[2] == "Correy":
    #     contender_dict["Correy"] += 1
    
    # elif   row[2] == "Li":
    #     contender_dict["Li"] += 1
    
    # else:  row[2] == "O'Tooley"
    # contender_dict["O'Tooley"] += 1   
    
    if row[2] in contenders_dict.keys():
      contenders_dict[row[2]] += 1
    #Initializing in the dictionary with one vote
    else:
        contenders_dict[row[2]] = 1

        
#Print outs
print(totalVotes)
print(contenders)
print(contenders_dict)
print()

#Print out of Summary Table

max_cont = max(contenders_dict, key=contenders_dict.get)
max_votes = contenders_dict[max_cont]


#Print out the Summary Table
summary = f"""Poll Results
----------------------------
Total Votes: {totalVotes}
----------------------------\n"""
for person in contender_dict.keys():
    prcnt =  100*{contender_dict[person] / totalVotes}
    summary += f"{person}: {round(prcnt, 2)}% ({contender_dict[person]})\n"

summary += f"""---------------------------
-----------------------
 {max_cont}:  Elected
 --------------------------
 """

print(summary)

#Writes the text file
with open("PyPoll_summary.txt", "w") as file:
    file.write(summary)

#Sources:
#Maximum value in dictiorary - https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
#Dividing each dictionary value by total value - https://stackoverflow.com/questions/30964577/divide-each-python-dictionary-value-by-total-value/30964739
#Resolving End of Line (EOL) Syntax Error - http://net-informations.com/python/err/eol.htm