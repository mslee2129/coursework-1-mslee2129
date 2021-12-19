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

