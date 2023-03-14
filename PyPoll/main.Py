import os
import csv

os.chdir(os.path.dirname(__file__))
ballotpath = os.path.join('Resources', 'election_data.csv')


ballot = []
candidates = []
votes = []
votes_percentage = []

with open(ballotpath) as ballotfile:

    ballotreader = csv.reader(ballotfile, delimiter=',')
    next(ballotreader)

    for row in ballotreader:
        ballot.append(row[2])

for i in ballot:

    if i not in candidates:
        candidates.append(i)
        votes.append(1)
    else:
        votes[candidates.index(i)] = votes[candidates.index(i)] + 1


for i in votes:

    votes_percentage.append(round(i/len(ballot)*100,3))


winner_index = 0
max = 0
for i in votes:
    if i > max:
        max = i
        winner_index = votes.index(i)


print("\n")
print("Election Results")
print("----------------------------")
print(f"Total Votes: {len(ballot)}")
print("----------------------------")

for i in range(len(votes)):
    print(f"{candidates[i]}: {votes_percentage[i]}% ({votes[i]})")


print("----------------------------")
print(f"Winner: {candidates[winner_index]}")
print("----------------------------")


results_path = os.path.join("analysis", "election_results.txt")

with open(results_path, 'w') as results_file:


    results_file.write("Election Results\n")
    results_file.write("----------------------------\n")
    results_file.write(f"Total Votes: {len(ballot)}\n")
    
    for x in range(len(votes)):
        results_file.write(f"{candidates[x]}: {votes_percentage[x]}% ({votes[x]})\n")
    
    results_file.write("----------------------------\n")
    results_file.write(f"Winner: {candidates[winner_index]}\n")
    results_file.write("----------------------------\n")
