# Bidding Strategies - Final Project - Intro to AI

Done by: 
1) Matan Yerushalmi 
2) Linoy Palas 
3) Gil Zada 
4) Omer Liberman 

from the Hebrew University.

Github link to source code - https://github.com/OmerLiberman/Intro-to-AI---Final-Project---Bidding-Strategies

## Code Files and Descriptions ##

### Main.py ###
In this file we can control the entire situation (constants).
Means that here we run the entire program, change constants, etc.

### AllCourses.py ###
This file includes the list of all the _courses in school
There is a default list of _courses which includes 8 well known _courses
or you can upload new _courses from a file text is called "AllCourses.txt"

### Balance.py ###
This file includes methods which intends to find balance point.
Means that - finding a case where the satisfaction rate of all strategies
is (approximately) equal.
That is what we may consider "optimal" distribution.

### CourseList.py ###
This file includes the _courses list each student has.
It has a functionality to return a random list or a default set list.
Each student has a field of this class which stated which _courses the student took.

### ExcelExporter.py ###
This file includes the methods which makes analytics.

### Graphs.py ###
In this file the graphs are created.
It first creates the text file and then convers it to excel file.
Then, insert the data to Pandas DataFrame.
And then we use the library matplotlib.pyplot to create beautiful graphs.

### Matcher.py ###
This class makes the assignment of students to classes.

### Runner.py ###
This file produces a file which includes all the situations.

### Satisfaction.py ###
This file includes the satisfaction measurer of each student has.
Satisfaction measurer receives the pre-assignments preferences of student
and the assignments of the student to _courses, and : EVALUATE the student's satisfaction level.

### Strategy.py ###
This file includes the _points_distribution each student has.
Strategy is defined by a function, then defined to distribution of
all the points student can distribute over the _courses.

### Student.py ###
This file includes the class of single student.
Each student has:
1) list of _courses (coursesList.py)
2) points distribution between the _courses (_points_distribution.py)
3) satisfaction function which indicated the level of satisfaction (satisfaction.py)
4) _courses and scores (dictionary)


