# Dependencies
import os
import pandas as pd
# Name of the CSV file
csv_file = "../Resources/election_data.csv"
election_df = pd.read_csv(csv_file)
election_df.head()
# The total number of votes cast
vote_count = election_df["Voter ID"].count()
vote_count
# A complete list of candidates who received votes
candidates = election_df["Candidate"].unique().tolist()
candidates
# The percentage of votes each candidate won
total_vote = election_df["Candidate"].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
total_vote
# The total number of votes each candidate won
candidates_votes = election_df["Candidate"].value_counts()
candidates_votes
# The winner of the election based on popular vote.
popular_candidate = candidates_votes.idxmax()
popular_candidate
print("Election Results")
print("-------------------")
print(f"Total Votes: {vote_count}")
print("-------------------")
print(total_vote.to_string(header=None))
print("-------------------")
print(f"Winner:{popular_candidate}")
# Export Script to Local
output_path = os.path.join("election_report.txt")