#import the csv module for reading csv files
import csv

# create the path to the data as a variable
csvpath = r'PyPoll\Resources\election_data.csv'

# # reading the csv file using the csv module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # empty dictionary for candidates
    candidateDict = {}

    # starting counter for total number of votes
    totalVotes = 0
    
    for row in csvreader:

        # set the candidate name as votedFor
        votedFor = row[2]

        # if the candidate is already in the dictionary, add one to its value
        if votedFor in candidateDict:
            candidateDict[votedFor] += 1

        # otherwise, put the candidate into the dictionary
        else:
            candidateDict[votedFor] = 1
        
        # keep the total vote counter running
        totalVotes += 1

winner = max(candidateDict, key=candidateDict.get)

candidatePrintout = []

for cand in candidateDict:
    candidateString = cand + ': ' + str(round((candidateDict[cand]/totalVotes)*100,3)) +'% (' + str(candidateDict[cand]) + ')'
    candidatePrintout.append(candidateString)

printCandString = "\n".join(candidatePrintout)

printString = f"""Election Results
----------------------------
{printCandString}
----------------------------
Winner: {winner}
----------------------------"""

print(printString)

output_path = r'PyPoll\Analysis\election_results.txt'

with open(output_path, 'w') as textfile:
    textfile.write(printString)
