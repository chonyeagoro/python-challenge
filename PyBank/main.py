import csv
import os

#Set a path for the csv file 
pybank = "PyBank/Resources/budget_data.csv"

#initialize variables 
total_months = 0
total_profit = 0 
profit_changes = []
total_change = 0
prev_loss = 0 
greatest_increase = ["", 0]
greatest_decrease = ["", 90]

#open and read csv file 
with open(pybank) as bank_file:

    #Store the dat in the csv_reader variable
    csv_reader = csv.reader(bank_file, delimiter=',')

    # Skip the header so we can go through the actual values
    header = next(csv_reader)
    #set values in header row
    first_row = next(csv_reader)
    total_months += 1
    total_change += int(first_row[1])
    prev_loss = int(first_row[1])
    total_profit += int(first_row[1])

    #create loop
    for row in csv_reader:
        # count the number of months
        total_months += 1
        # count the net total amount of "Profits/Losses"
        total_profit += int(row[1])

        # count the change in "Profits/Losses"
        profit_change = int(row[1]) - prev_loss

        # add profit change to list 
        profit_changes.append(profit_change)


        # reset prev_profit to the current profit  
        prev_loss = int(row[1])

#Finding the average of the changes in "Profit/Losses"
        avg_changes = sum(profit_changes) / len(profit_changes)
        avg = round(avg_changes, 2)

    # Find the greatest increase in profits (date and amount) over the entire period
        if profit_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_change
    
    # Find the greatest decrease in profits (date and amount) over the entire period
        if profit_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_change

#Print results
output = (f"Financial Analysis\n"
          f"----------------------------\n"
          f"Total Months: {total_months}\n"
          f"Total: ${total_profit}\n"
          f"Average Change: ${avg:.2f}\n"
          f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
          f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(avg))
print("Greatest Increase in Profits: " + str(greatest_increase[0])+ " (" + str(greatest_increase[1]) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

# output.to_csv('/Users/sybilonyeagoro/Documents/python-challenge/PyBank/analysis/Bank.txt', header=None, index=None, sep=' ')
file_to_output = "/Users/sybilonyeagoro/Documents/python-challenge/PyBank/analysis/Bank.txt"
with open(file_to_output, "w") as txt_file:
     txt_file.write(output)
