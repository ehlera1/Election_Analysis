#the data we need to retrieve
# 1. the total number of votes cast
# 2. A complete list of the candidates who receive dvotes
# 3. The percentage of botes each candidate won
# 4. The total number of votes each candidate won
# 5. the winner of the election based on popular vote. 

#    Resources\election_results.csv


# Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path. 
# Alternate Method
# file_to_load = 'Resources\election_results.csv'
# #open the election results and read the file. 
# with open(file_to_load) as election_data:
#To do: perform analysis
#print(election_data)
#close the file. 
#election_data.close()

# #Assing a variable to the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Track the winning candidate, vote count, and percentage. 
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file. 
with open(file_to_load) as election_data:
#     #Print the file object. 
#     print(election_data)

    #To do: read and analyse the data here. 
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)



    # read the header row.  
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file. 
    for row in file_reader:
        # print(row)
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #Add the candidate name to the candidate list/ 
        # candidate_options.append(candidate_name)

        # If the candidate doesn not match any existing candidate,
        # add the candidate list. 
        if candidate_name not in candidate_options:
            # Add it to the list of candidates. 
            candidate_options.append(candidate_name)

            #2 Begin trackng that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1
        
# Save the results to our text file. 
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
    
    # After printing the final vote count to the terminal save the finale vote count to the txt file.
    txt_file.write(election_results)

    # Retrieve vote count and percentage. 
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidat's voter count and percentage to the terminal. 

        print(candidate_results)

        # Save the candidate results to our text file. 
        txt_file.write(candidate_results)


        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
        
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


    

    # #Determine the percentage of votes for each candidate by looping through the counts. 
    # #1. Iterate through the candidate list. 
    # for candidate_name in candidate_votes:
    #     #2. Retrieve vote count of a candidate. 
        # votes = candidate_votes[candidate_name]
    #     #3. Calculate the percentage of votes. 
        # vote_percentage = float(votes)/float(total_votes) * 100
    #     #4 Print the cadidate name and percentage of votes. 
    #     # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #     # Determine winning vote count and candidate
    #     #1 Determine if the votes are greater than the winning count. 
    #     if (votes > winning_count) and (vote_percentage > winning_percentage):
    #         #2 If true then set winning_count = votes and winning_percent = vote_percentage.
    #         winning_count = votes 
    #         winning_percentage = vote_percentage
    #         #3 Set the winning_candidate equal to the candidate's name
    #         winning_candidate = candidate_name

         #Declare candidate_results 
        # candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage to the terminal. 
        # print(candidate_results)

        #Save the candidate results to our text file. 
        # txt_file.write(candidate_results)


    # Winning_candidate_summary = (
    #     f"-------------------------\n"
    #     f"Winner: {winning_candidate}\n"
    #     f"Winning Vote Count: {winning_count:,}\n"
    #     f"Winning Percentage: {winning_percentage:.1f}%\n"
    #     f"-------------------------\n")

    # # print(Winning_candidate_summary)








    # #Print the total votes
    # # print(total_votes)
    # # print(candidate_options)
    # # print(candidate_votes)





    # # Using the with statement open the file as a text file.
    # # outfile = open(file_to_save, "w")
    # # outfile.write("Hello World")

    # # with open(file_to_save,"w") as txt_file:
    # #     # Write some data to the file. 
    # #     # txt_file.write("Arapahoe, ")
    # #     # txt_file.write("Denver, ")
    # #     # txt_file.write("Jefferson")
    # #     # txt_file.write("Arapahoe\nDenver\nJefferson")
    # #     txt_file.write("Counties in the Election")
    # #     txt_file.write("\n----------------")
    # #     txt_file.write("\nArapahoe\nDenver\nJefferson")



    # # Close the file
    # # outfile.close

    # # open(file_to_save,"w")











