
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


# Print the results to file
out_file_path = "PyPoll\election_results.txt"
with open(out_file_path, 'w') as file_out:
    file_out.write('Election Results\n')
    file_out.write('-------------------------\n')
    file_out.write(f'Total Votes: {total_votes}\n')
    file_out.write('-------------------------\n')
    for candidate in candidates:
        votes = Votes[candidates.index(candidate)]
        file_out.write(f'{candidate}: {round((votes/total_votes) * 100,3)}% ({Votes[candidates.index(candidate)]})\n')
    file_out.write('-------------------------\n')
    file_out.write(f'Winner: {winning_Can}\n')
    file_out.write('-------------------------\n')

### End Here





