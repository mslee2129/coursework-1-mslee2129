# Coursework 1

## Technical information
### Repository URL
[https://github.com/ucl-comp0035/coursework-1-mslee2129]

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.

If the marker cannot execute your coursework they can't grade it!

## Selection of project methodology
### Methodology (or combination) selected
CRISP-DM
### Selection criteria and justification of selection
Criteria:
- Level of volatility in the requirements
- Availability of documentation/support
- Flexibility of structure and timeframe
- Size of the project team

Justification: For this project, I wanted to focus more on the data science aspect of the project, and CRISP-DM is known 
as one of the most popular data science methodologies. This would mean that it would have plenty of documentation and 
support available to assist me throughout the project. Out of the many data science methodologies, I chose CRISP-DM since 
it is a methodology that allows for the most flexibility, as it is a methodology that combines features of the waterfall 
and agile methods.

## Definition of the business need
### Problem definition
Doing business: Different countries offer different environments for a business to thrive, and it is often difficult to 
identify what countries offer the most potential growth of a business. If a company chooses poorly when moving to another
country, it may result in severe financial losses. It is essential for a business to choose to expand to a country that 
would maximise its revenue. Given a set of 205 indicators and how a country scores in those indicators across the years,
recommendations will be made on the next steps to take for a business.

### Target audience
See Persona.pdf
### Questions to be answered using the dataset
1. Which countries rank the highest in the 'ease of doing business' criteria?
2. Which countries have the most business-friendly tax regulations?
### Suggested web app

## Data preparation and exploration
### Data preparation

[Data Preparation](data_preparation.py)
In the data_preparation.py file, I have written code that would clean the data from the DBData.csv file. This was done
mostly for two purposes: to filter out certain values in the 'Country Name' column that were not included in the 
DBCountry.csv file (values such as Beijing, Delhi, etc.), and to filter out the indicators that won't be used in the
project. I have also decided to leave only the recent data points (2016 onwards) since the availability of some 
values prior is inconsistent. Once the cleaning was finished, I exported the dataframe as a csv file called 
DBData_clean.csv

### Prepared data set
DBData.csv
DBCountry.csv

### Data exploration
For the data exploration phase, I have decided to visualise the data using bar charts, as the most useful data points 
in the dataset are the rankings (of ease of business, paying taxes). These two values are also what would be most helpful
in answering the questions identified above. Graphs of the two values is saved as 'rank_ease_of_doing_business.png' and
'rank_paying_taxes.png', respectively. For more detail, the create_line function can be used to plot line graphs
for individual countries across the years. The function requires a country code, which is available in the DBCountry.csv
file. An example is given as AFG.png.
[Data Exploration]()


## Weekly progress reports
### Report 1
What I did in the last week:
In the previous week I've set up my GitHub account and installed PyCharm to set up my development environment. After the
PBL session, I have also taken a look at the different development methodologies and have shortlisted a few methods I 
would like to implement into my project. I have also taken a look at my dataset I would use in my project to familiarise 
myself with the process.

What I plan to do in the next week:
In the next week I would like to specify which methodology I would use in my project, and focus on the business aspect 
of the project, including target audience and defining the problem.

Issues blocking my progress (state ‘None’ if there are no issues):
There are no problems I have encountered yet.

### Report 2
What I did in the last week:
In the past week I have developed my problem statement that is specific to the dataset I will be using by following the
template provided in the PBL session. I have also started on creating a persona, which will act as my target audience 
moving forward. I have also started committing changes to my GitHub repository.

What I plan to do in the next week:
In the next week I will iron out my persona, since I will need to add more details such as his values and goals, then 
upload these files to my GitHub repository. I will then read up on the content regarding data ethics for the next week.

Issues blocking my progress (state ‘None’ if there are no issues):
I have not encountered any problems yet.

### Report 3
What I did in the last week:
In the past week I was able to finish up writing my persona, as well as get started on observing my dataset. I have 
followed the PBL materials to familiarise myself with the Pandas library to begin analysing my dataset and test out the
different functions.

What I plan to do in the next week:
In the next week, I will continue to work on my dataset using the Pandas library to see if there are any irregularities
that may cause an error and start cleaning the dataset.

Issues blocking my progress (state ‘None’ if there are no issues):
There are currently no issues I have encountered.

### Report 4
What I did in the last week:
In the past week I was able to follow along with the data exploration process, which involved cleaning more of the data 
and starting to visualise some of the data that are relevant to the project. I have worked more with dataframes and the
pandas library, as well as trying out some other libraries such as matplotlib.

What I plan to do in the next week:
In the next week I should be able to finish up the project, since the deadline is on the 10th of November. I will 
achieve this by adding more code to my files and committing them on GitHub.

Issues blocking my progress (state ‘None’ if there are no issues):
I have not committed some of my work to GitHub as I prefer to work locally and make sure there are no error before, 
which may have hindered my progress a little bit. However, this was not too much of a problem.

## References
Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
used to using in your course.
