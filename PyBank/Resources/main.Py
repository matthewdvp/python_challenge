import csv

months = []
profit_loss = []
profit_loss_change = []

with open('Resources/budget_data.csv') as budgetfile:

    budgetreader = csv.reader(budgetfile, delimiter=',')
    budgetheader = next(budgetreader)

    for row in budgetreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

total = sum(profit_loss)

for i in range(len(profit_loss)-1):
    profit_loss_change.append(profit_loss[i+1]-profit_loss[i])

total_change = sum(profit_loss_change)

average_change = round(total_change/len(profit_loss_change),2)

increase = max(profit_loss_change)
decrease = min(profit_loss_change)

increase_month = months[profit_loss_change.index(increase)+1]
decrease_month = months[profit_loss_change.index(decrease)+1]

print("\n")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_month} ${increase}")
print(f"Greatest Decrease in Profits: {decrease_month} ${decrease}")
print("----------------------------")

with open('analysis/results.txt', 'w') as results_file:

    results_file.write("Financial Analysis\n")
    results_file.write("----------------------------\n")
    results_file.write(f"Total Months: {len(months)}\n")
    results_file.write(f"Total: ${total}\n")
    results_file.write(f"Average Change: ${average_change}\n")
    results_file.write(f"Greatest Increase

