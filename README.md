# Election Analysis

## Project Overview

A Colorado Board of Election employee has given the following tasks to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the voter turnout for each county.
7. Calculate the percentage of votes from each county out of the total count.
8. Detemine the county with the highest turnout.

## Resources

- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.60.2

## Summary

Using the code attached to this report, an analysis of the election shows that:

-There were 369,711 votes cast in this congressional election.  
-The candidates were:  
  -Charles Casper Stockham  
  -Diana DeGette  
  -Raymon Anthony Doane  
-The total candidate resultes were:  
  -Charles Casper Stockham received 23.0% of the votes and 85,213 total votes.  
  -Diana DeGette received 73.8% of the votes and 272,892 total votes.  
  -Raymon Anthony Doane received 3.1% of the votes and 11,606 total votes.  
-The voter turn out per county was:  
  -Jefferson County had a 10.5% turnout which is a total of 38,855 voters.  
  -Denver County had a 82.8% turnout which is a total of 306,055 voters.  
  -Arapahoe County had a 6.7% turnout which is a total of 24,801 voters.  
-The county with the highest voting turnout was:  
  -Denver County, which had a 82.8% turnout and a total of 306,055 voters.  
-The winner of the election was:  
  -Diana DeGette who received 73.8% of the votes and 272,892 total votes.  
  
A printed summary can be found in the following text file:
[election_analysis.txt](https://github.com/brefrank/election-analysis/files/7281163/election_analysis.txt)

  
## Overview

The purpose of this election audit analysis was to use raw data from [election_results.csv](https://github.com/brefrank/election-analysis/files/7281151/election_results.csv) to calculate accurate results for the election. With these calculations, the audit team can compare the original election results with the computer calculated results to ensure accuracy. 

## Summary

Because the module attached is pulling directly from this election's data, it can be assumed that running this code will always output accurate results. With that knowledge, this code attached could easily be manipulated to process future elections as well in a fast and accurate way. To do so, the input and output file paths will need to be edited to include the file needing analysis and a new file to write results in. 

  For example, if the next election results were saved in a folder called "Election_Results" and the file was named "School_Board_Election.csv", the input code would looks like   this:

    file_to_load = os.path.join("Election_Results", "School_Board_Election.csv")

  If we wanted our output written to a file within an analysis folder, the output code would be as follows:
    
    file_to_save = os.path.join("Analysis", "School_Board_Election.txt")

The script used for this data could also be formatted to include more header columns. Just follow the same format already written to create additional analysis and you will be good to go.
