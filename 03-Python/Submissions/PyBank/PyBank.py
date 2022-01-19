#Python code - PyBank

import csv

csvpath = "PyBank\\Resources\\budget_data.csv"

#Initial Settings starting at zero
totalMonths = 0
totalGains = 0

#tracking the changes
deltas = []
deltaMonths = []
previousGains = 0

# rows = []

with open(csvpath, "r") as file:

    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

    print(csvheader)
    print()

    for row in csvreader:
        # rows.append(row)        

        totalMonths +=1
        totalGains += int(row[1])

        if totalMonths > 1:
            delta = int(row[1]) - previousGains
            deltas.append(delta)
            deltaMonths.append(row[0])

    #Update previous profits
    previousGains = int(row[1])

    print(row)

print(totalMonths)
print(totalGains)        
#Commenting these functions out for the new ones
# # print(deltas)
# print(len(deltas))
# print(sum(deltas) / len(deltas))
# print(max(deltas))
# print(min(deltas))
avg_delta = sum(deltas) / len(deltas)
max_delta = max(deltas)
min_delta = min(deltas)
print(max_delta)
print(min_delta)
print()

#This is for the Max Month
maxMonth_idx = deltas.index(max_delta)
maxMonth = deltaMonths[maxMonth_idx]

#This is for the Min Month
minMonth_idx = deltas.index(min_delta)
minMonth = deltaMonths[minMonth_idx]
print(maxMonth)
print(minMonth)
print()

#Print out the Summary Table
summary = f"""Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${totalGains}
Average  Change: ${avg_delta}
Greatest Increase in Profits: {maxMonth} (${max_delta})
Greatest Decrease in Profits: Sep-2013 (${min_delta})
        """
print(summary)

#Writes the text file
with open("PyBank_analysis.txt", "w") as file:
    file.write(summary)

#Sources:
#Maximum value in dictiorary - https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
#Dividing each dictionary value by total value - https://stackoverflow.com/questions/30964577/divide-each-python-dictionary-value-by-total-value/30964739
