

import csv

file_path = 'PyBank\Resources\Finance_data.csv'
total_months=0
total_change=0
total_sum = 0
previous_month_profit_loss = 1088983
month=[]
changes_list = []
finance = []
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
            month.append(date)
            total_change += change 
            previous_month_profit_loss = Current_month_profit_loss       
            max_change = max(changes_list)
            min_change = min(changes_list)
            if change == max_change:
                great_date = date
            if change == min_change:
                least_date = date
                

    



# calculate total Sum/ read file again
with open(file_path) as Finance_Path:
    csv_file = csv.reader(Finance_Path)
    next(csv_file)  #Skips a row in the file (first row = header row)
    for row in csv_file:
        date = row[0]
        money = int(row[1])
        if money not in finance:
            finance.append(money)
            total = sum(finance)
       

           
            
 # calculate average          
average = total_change/len(changes_list)
       

   

#print results to screen
print("Financial Analysis")
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${round(average,2)}')
print(f'Greatest Increase in Profits: {great_date} ${max_change}')
print(f'Greatest Decrease in Profits: {least_date} $({min_change})')


#print results to analysis file
file_path_out = "PyBank\Analysis\Finance_data.txt"
with open(file_path_out, 'w') as file_out:
    file_out.write("Financial Analysis\n")
    file_out.write('----------------------------\n')
    file_out.write(f'Total Months: {total_months}\n')
    file_out.write(f'Total: ${total}\n')
    file_out.write(f'Average Change: ${round(average,2)}\n')
    file_out.write(f'Greatest Increase in Profits: {great_date} ${max_change}\n')
    file_out.write(f'Greatest Decrease in Profits: {least_date} $({min_change})\n')