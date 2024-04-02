

import csv

file_path = 'PyBank\Resources\Finance_data.csv'
total_months=0
total_change=0
previous_month_profit_loss = 1088983
changes_list = []
# read file
with open(file_path) as Finance_Path:
    csv_file = csv.reader(Finance_Path)
    next(csv_file)  #Skips a row in the file (first row = header row)
    for row in csv_file:
        total_months+=1
        if total_months>1:
            date = row[0]
            Current_month_profit_loss = int(row[1])
            change = Current_month_profit_loss - previous_month_profit_loss
            changes_list.append(change)
            total_change += change 
            previous_month_profit_loss = Current_month_profit_loss       
            max_change = max(changes_list)
            min_change = min(changes_list)
            

average = total_change/len(changes_list)
       

   


print("Financial Analysis")
print('----------------------------')
print(f'Total Months: {total_months}')
#print(f'Total: ${total_sum}')
print(f'Average Change: ${round(average,2)}')
for date in changes_list:
    great = max_change
print(f'Greatest Increase in Profits: {date} ${max_change}')
print(f'Greatest Decrease in Profits: {date} $({min_change})')