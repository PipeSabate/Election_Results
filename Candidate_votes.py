import csv
import os 

file_to_load = os.path.join('contenido','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes= {}
winning_candidate = " "
Winning_count = 0
Winning_percentage = 0

with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data) 
    print(file_reader)
    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1 
        candidate_name= row[2]
        if candidate_name not in candidate_options:
             candidate_options.append(candidate_name)
             candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage= float(votes) / float(total_votes) * 100
    if (votes > Winning_count) and (vote_percentage > Winning_percentage ):
        Winning_count = votes
        Winning_percentage = vote_percentage
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:1f}% ({votes:,})\n")


    winning_candidate_sumarry=(
    f"--------------\n"
    f"Winner: {winning_candidate}\n"
    F"winning vote Count: {Winning_count:,}\n"
    F"Winning Percentage: {Winning_percentage:1f}\n"
     f"--------------\n"
    )
    print(winning_candidate_sumarry)

