# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local 
congressional election. 


1. Calculate the total number of votes cast.
2. Get a complete list of the candidates who received votes.
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Sofware: Python 3.7.6, Visual Studio Code, 1.61.0


## Summary

The analysis of the elction show that; 
 - There were 368,711 votes cast in the election
 - The candidates were: 
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
 - The candidate results were: 
    - Charles Casper Stockham received 23% of the vote and 85,213 votes. 
    - Diana Degette received 73.8% of the vote and 272,892 votes.  
    - Raymon Anthony Doane received 3.1% of the vote and 11,608 votes.
 The winner of the election was:
    - In a landslide vicotry Diana Degette received 73.8% of the vote and 85,213 votes to secure her seat in congress. 



## Challenge Overview

In order to have some secondary informaiton and ensure the election results were acurate the election commision asked that we check a few other data points. The data points we looked at were the voter turnout for each county,
the percnetage of votes from each county out of the total count, as well as the county with the highest total voter turnout. 

- The purpose of gathering the data at the county level is to have a secondary audit to the evalute and compare the candidate results, ensuring that the election was accurate. 

## Challenge Summary 

The results of the challenge: 

- There were 369,711 votes in the three counties that represent this congressional district.  
- There are three counties in the district and the breakdown of votes by county is as follows: 
	- Denver county had 306,055 voters which represented approximately 82.8% of the total voters in the district. 
	- Jefferson county had 38,855 voters to represent approximately 10.5% of the total voters in the district. 
	- Arapahoe county representing the smallest number of voters had 24,801 voters for 6.7% of the total voters in the district.
- Based on the above breakdown, Denver clearly had the largest number of votes.

- Using the elections_results.csv file provided to us by the election commission we were able to use the VS Code and Python to distill the results in to something that is easily readable.
  The results of this script were printed to the terminal window as shown in the image below as well as writen to a text file that is saved to the analysis folder titled as "election_analysis.txt"

![election_analyis_terminal_output](https://user-images.githubusercontent.com/90698381/136874073-af982fb7-2c30-44f8-8116-5c7bd440676e.png)

- The Python script that we created to evaluate this congressional district could easily be used on other districts to distill a large data set or other election results into easily understood and meaningful results.  
	- Assuming that the results are provided in the csv file format, all the variables could be easily adjusted to process other files. 
	- The loop structures, variables, and other algorithms can be easily applied to create similar outputs. 
	- To build off what we already done, we could show the relationship of the votes for each candidate by county. 
	- If the total population was known for each county we could also show the percentage of voter turnout by county or district as well.
