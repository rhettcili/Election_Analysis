
from itertools import count

# counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})


# # my_votes = int(input("How many votes did you get in the election? "))

# # total_votes = int(input("What is the total votes in the election? "))

# # percentage_votes = (my_votes / total_votes) * 100

# # print("I received " + str(percentage_votes)+"% of the total votes.")

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # To do: perform analysis.

# # Close the file.
# election_data.close()

# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)


import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
     
