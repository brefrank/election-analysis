# The data we need to retrieve
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# 1. The total number of votes cast
total_votes = 0
# 2. A complete list of candidates who recieved votes
candidate_options = []
# 3. Declare the empty dictionary.
candidate_votes = {}
# Open the election results and read the file.
# 4. Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options: 
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes)*100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
