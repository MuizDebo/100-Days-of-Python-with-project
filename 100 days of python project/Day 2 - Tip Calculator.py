#Welcome Message
print("Welcome to the tip calculator")

#Enter total bill
bill = float(input("What is the total bill?\n"))

#Enter tip percentage
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15\n"))

#Enter number of people to split bill
people = int(input("How many people are splitting the bill?\n"))

#Calculate pay
pay = bill + (1 + tip_percent)

#Calculating the amount each person gets
total_pay = pay/people

#Printing to 2 decimal places
print(round(total_pay, 2))



