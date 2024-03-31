
# create variables
import csv
Election_file_path ="PyPoll\Resources\election_data.csv"
total_votes = 0
candidates = []
Votes = []
# open the file
with open(Election_file_path) as Election_File:
    csv_file = csv.reader(Election_File)
    next(csv_file)  #Skips a row in the file (first row = header row)
    # Read a row in the file
    for row in csv_file:
        # Add to total votes
        total_votes += 1
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        if candidate not in candidates:
            # add to list if they haven't been added.
            candidates.append(candidate) 
            Votes.append(1) # add the first vote
        else: #assume candidate is in list
            Candidate_ID = candidates.index(candidate)
            Votes[Candidate_ID] += 1
            
# Done Reading the file
# Find the winner 
    winning_Can = ""
    winning_Can_Votes = 0
    for candidate in candidates:
        votes = Votes[candidates.index(candidate)]
        if votes>winning_Can_Votes:
            winning_Can = candidate
            winning_Can_Votes = votes
            
# Add to total votes
# Print results to screen
        
# Print results to file
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for candidate in candidates:
    votes = Votes[candidates.index(candidate)]
    print(f'{candidate}: {round((votes/total_votes) * 100,3)}% ({Votes[candidates.index(candidate)]})')

print('-------------------------')
print(f'Winner: {winning_Can}')
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