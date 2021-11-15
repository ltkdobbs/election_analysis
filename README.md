# **Analysis – Election Audit**
## **Background Breakdown**
The Client’s (Colorado Board of Elections; Represented by Tom and Seth) goal was to automate the vote counting process using a programming script; Python was specifically recommended for use in the audit.

Our goal was to create a script which would run through pre-collected data and determine the congressional winner based on the popular vote. Supplementary analysis covering voter turnout and candidate popularity was also requested. Using this data, we hope to expand the scope of future analysis – specifically regards to other, larger, elections.

## Results:
1. The total number of votes collected was 369,711. (See Image 1.1 at the end)
   - Jefferson County collected 38,855 votes**, which was 10.5% of the total votes.
   - Denver County collected 306,055 votes, which was 82.8% of the total votes.
   - Arapahoe County collected 24,801 votes, which was 6.7% of the total votes.
2. The largest voter turnout was in Denver County.
3. Diana DeGette was the winner of the congressional election with 73.8% (272,892) of the votes. (See Image 1.2 at the end)
   - Candidate Charles Casper Stockham received 85,213 votes, totaling 23.0%.
   - Candidate Diana DeGette received 272,892 votes, totaling 73.8%.
   - Candidate Raymon Anthony Doane received 11,606, totaling 3.1%.

## Summary
Overall, the script is pretty flexible – most of the data collected is broad enough in scale and definition that as long as the format of the csv is followed (the County as the second value and the Candidate Name as the third value in the header), then the script should run properly. It will sort through those two columns and collect the unique values, then loop through and count them.

The easiest way I can imagine altering the script to be even more flexible is to replace the sections which specifically link to the columns with a [find] statement. With some tweaking, it should be possible to loop through the header row to search for specific values, such as “Candidate Name”, and set that as the value for the [candidate_name] variable. It’s a bit advanced for my skillset, so the tweaking would take time, but it is doable.

Image 1.1 Vote Breakdown by County
![Total Votes Pie Chart](https://github.com/ltkdobbs/election_analysis/blob/main/Resources/Total%20Votes%20Pie%20Chart.png)

Image 1.2 Vote Breakdown by Candidate
![Candidate Votes Pie Chart](https://github.com/ltkdobbs/election_analysis/blob/main/Resources/Candidate%20Votes%20Pie%20Chart.png)
