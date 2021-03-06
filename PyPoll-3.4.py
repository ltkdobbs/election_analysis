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

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data
    filereader = csv.reader(election_data)
    #Print the header row
    headers = next(filereader)
    print(headers)
    #Print each row in the CSV file
    # for row in readfile:
    #     print(row)