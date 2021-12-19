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
and agile methods. It also allows for a number of team members to work on various aspects of the project at the same time,
making it an efficient way to organise and distribute tasks. Also, given my experience with data analysis, there would be
aspects of this methodology that would be familiar to me, which is an added benefit. The shortcomings of using CRISP-DM
in this project, however, could be that it lacks some detail that other methodologies do not, and this may lead to some
oversight or lack of clarity when it comes to the finer details of the project. The fact that it is a data science 
methodology may also be a weakness, since it may overlook the software engineering aspects such as deployment of their models.

## Definition of the business need
### Problem definition
Doing business: Different countries offer different environments for a business to thrive, and it is often difficult to 
identify what countries offer the most potential growth of a business. If a company chooses poorly when moving to another
country, it may result in severe financial losses. It is essential for a business to choose to expand to a country that 
would maximise its revenue. This can be especially relevant to newly expanding companies that want minimise the risk of
failing in their new enterprise. Given a set of 205 indicators and how a country scores in those indicators across the 
years, recommendations will be made on the next steps to take for a business. 

### Target audience
See [Persona.pdf](Persona.pdf)
### Questions to be answered using the dataset
1. Which countries rank the highest in the 'ease of doing business' criteria?
2. Which countries have the most business-friendly tax regulations?

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

# Coursework 2

Most students will use the same repository for coursework 2. You may use this file to present the results of that
coursework if you wish. Alternatively you can use video or audio to provide the explanations instead of writing them.

## Requirements definition and analysis
The term 'requirements' is used in the broader sense, user stories and/or use cases may be used.
### Requirements elicitation and prioritisation methods
For this coursework, I have decided to use user stories to specify the requirements. This includes the 'As a, I want, 
so that' format, so that I could capture the target audience and their needs. There are a total of 4 different user 
groups: CEO, Data Scientist, Marketing Staff, and General Public. The requirements have been given a priority using the
MoSCoW method, which classifies the requirements in 4 tiers of 'Must have', 'Should have', 'Could have', and 'Won't have
for now'. The requirements and their priorities have been sorted in a table to make it easier to comprehend.
### Documented and prioritised requirements
Link to the full list of documented and prioritised requirements.

See [Requirements](requirements/Requirements%20Elicitation.pdf)

## Design
### Structure and flow of the interface
See [Wireframe](design/Wireframe.pdf)

For the initial design of the app, I decided to create a wireframe to help visualise the requirements set in my
Requirements Elicitation. This wireframe was designed using Figma, an online designing software. Some requirements
(i.e. those with lower priority) have not all been included in the wireframe. I have decided to design the app for 
desktop use, since my target audience would mostly be office workers who use a computer more than their phones for
work. The screen size for the wireframe was therefore set as 1080x768.
### Architecture design
See [UML Class Diagram](design/UML%20Diagram.pdf)

See [Routes, Views, Controller Functions](design/RoutesViewsControllers.pdf)

The architecture has been designed using UML diagrams via LucidChart. UML diagrams are an efficient way to visualise
classes, their attributes and methods, and their relations to other classes. The class diagram includes notations of 
data types, inheritance, and multiplicity to further specify the roles and relations of the different classes created.
The routes, views, and controller functions of the architecture is specified in a separate document, with each route 
having an associated view (using the wireframes created) and controller functions.
### Relational database design
See [Relational Database Design](design/Relatonal%20Database%20Design.pdf)

The relational database has been designed using an entity relationship diagram (ERD) via LucidChart. The ERD holds
information on the entity, keys, fields, and data types, which are all key components of a database. The relationship
between entities is visualised using the Crows Foot style.


## Testing
### Choice of unit testing library
pytest
### Tests
The tests should be in a separate and appropriately named file/directory.

[Test Files](tests)
### Test results
Provide evidence that the tests have been run and the results of the tests (e.g. screenshot).

See [User Test](User%20Test.png)
### Continuous integration (optional)
Consider using GitHub Actions (or other) to establish a continuous integration pipeline. If you do so then please 
provide a link to the .yml and a screenshot of the results of a workflow run.

[.yml file](.github/workflows/python-app.yml)

[Workflow](Continuous%20Integration.png)
