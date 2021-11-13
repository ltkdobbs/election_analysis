#What do we need to do?
# 1. Find out the total # of votes cast
# 2. Determine a complete list of candidates
# 3. Total number of votes for each candidate
# 4. Percentage of votes for each candidate
# 5. Election winner based on popular vote

#Add dependencies
import csv
import os

#Assign a variable to load the file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter:
total_votes = 0

#Initialize an empty list:
candidate_options = []

#Initialize an empty dictionary:
candidate_votes = {}

#Declare winning candidate and count tracker variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data
    file_reader = csv.reader(election_data)

    #Print the header row
    #headers = next(file_reader)
    #print(headers)

    #Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            #Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Calculate the vote percentage for each candidate.
#iterate through the candidate list.
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    #Calculate the percentage of votes.
    vote_percentage = (float(votes) / float(total_votes)) * 100

    #TO DO:
    # Print the candidate name, vote count, and % of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    #Determine if voters are greater than winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true set winning_count = votes and winning_percent = #vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #Set winning_candidate equal to candidate's name.
        winning_candidate = candidate_name
#TO DO:
# Print out winning candidate, vote count and percentage.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)