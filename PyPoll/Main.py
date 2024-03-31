#
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

### Start Here
# create variables
import csv
Election_file_path ="PyPoll\Resources\election_data.csv"
total_votes = 0

# open the file
with open(Election_file_path) as Election_File:
    csv_file = csv.reader(Election_File)
    next(csv_file)  #Skips a row in the file (first row = header row)
    # Read a row in the file
    for row in csv_file:
        # Add to total votes
        total_votes += 1
        
# Add to total votes
# Print results to screen
        
# Print results to file
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')



### End Here





#Example
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------