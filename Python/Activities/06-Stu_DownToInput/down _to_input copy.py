

#name of participants
name1 = input("Marco")
name2 = input("Kendrick")

#questioning how many months
code1 = input("How many months have you") + str(name1) + ("been coding?")
code2 = input("How many months have you") + str(name2) + ("been coding?")

#number of months
months1 = 28
months2 = 36

#total of months of both names added together
total = months1 + months2

#Output
print(f'{name1}+{name2}", they have been coding together for a total amount of" + {total}"."')