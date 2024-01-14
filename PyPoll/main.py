import csv

#Set a path for the csv file 
pypoll = "PyPoll/Resources/election_data.csv"

#initialize variables 
total_votes = 0
candidates_votes = {}

#open and read csv file 
with open(pypoll, 'r') as vote_file:
    csv_reader = csv.reader(vote_file, delimiter=',')
    next(csv_reader)

    #create loop
    for row in csv_reader:
        #The total number of Voters
        total_votes += 1

        #Storing the name of the candidates
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidates_votes:
            #Then add it to the dictionary of candidates and initialize vote count
            candidates_votes[candidate_name] = 0

        # Add a vote to the candidate's vot count
        candidates_votes[candidate_name] += 1

# Determine the winner by looping through the counts
winner = max(candidates_votes, key=candidates_votes.get)
winning_count = candidates_votes[winner]


#Print Results 
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
# Print each candidate's voter count and percentage
for candidate, votes in candidates_votes.items():
    vote_percentage = votes / total_votes * 100
    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})"
    print(voter_output)
# Print the winning candidate
print("-------------------------")
print(winner)
print("-------------------------")