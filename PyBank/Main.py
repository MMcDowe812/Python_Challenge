import csv
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# Start Here
# Read CSV File

file_Path="PyBank\Resources\Finance_data.csv"
    #Renamed file due to \b causing an error.
total_Months = 0
total_PL = 0
month=[]
prof_loss=[]
with open(file_Path) as Finance_Path:
    csv_file = csv.reader(Finance_Path)
    next(csv_file)  #Skips a row in the file (first row = header row)
    # Calculate the total months
    for row in csv_file:
        total_Months+=1
        date = row[0]
        money = row[1] 
        if money not in prof_loss:
            prof_loss.append(int(money))
            total_PL = sum(prof_loss)
            print(month)       
            
        
   


            
    
    # total profit and loss
    #for row in prof_loss:
        

    
        


# Print to screen
print("Financial Analysis")
print('-------------------------')
print(f'Total Months: {total_Months}')
print(f'Total: ${total_PL}')
#print(f'Average Change{}')
#print(f'Greatest Increase in Profits: {}')
#print(f'Greatest Decrease in profits: {}')

# Print to File



# Examples
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# End Here