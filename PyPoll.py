#the data we need to retrieve
# 1. the total number of votes cast
# 2. A complete list of the candidates who receive dvotes
# 3. The percentage of botes each candidate won
# 4. The total number of votes each candidate won
# 5. the winner of the election based on popular vote. 

#    Resources\election_results.csv

import csv
import os

#Assign a variable for the file to load and the path. 


# Alternate Method
# file_to_load = 'Resources\election_results.csv'

# #open the election results and read the file. 
# with open(file_to_load) as election_data:


#     #To do: perform analysis
#     print(election_data)

#close the file. 
#election_data.close()

# #Assing a variable to the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#Open the election results and read the file. 
with open(file_to_load) as election_data:
#     #Print the file object. 
#     print(election_data)

    #To do: read and analyse the data here. 
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print each row in the CSV file/ 
    # for row in file_reader:
    #     print(row)

    #Print the header row. 
    headers = next(file_reader)
    print(headers)



# Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# outfile.write("Hello World")

# with open(file_to_save,"w") as txt_file:
#     # Write some data to the file. 
#     # txt_file.write("Arapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson")
#     # txt_file.write("Arapahoe\nDenver\nJefferson")
#     txt_file.write("Counties in the Election")
#     txt_file.write("\n----------------")
#     txt_file.write("\nArapahoe\nDenver\nJefferson")



# Close the file
# outfile.close

# open(file_to_save,"w")











