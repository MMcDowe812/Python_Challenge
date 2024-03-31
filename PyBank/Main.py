import csv
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# Start Here
# Read CSV File

Finance_file_Path="PyBank\Resources\Finance_data.csv"
    #Renamed file due to \b causing an error.
total_Months = 0

# open the file
with open(Finance_file_Path) as Finance_Path:
    csv_file=csv.reader(Finance_Path)
    next(csv_file)  #Skips a row in the file (first row = header row)
    # Read a row in the file
for row in csv_file:
    print(row)

# Print to screen

# Print to File

# End Here