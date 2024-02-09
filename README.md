# Challenge Openspace Classifier
This project aims to create a program that randomly assigns people to seats in an open space office setup. It provides a fun and interactive way for colleagues to get to know each other by changing seats daily. 

# Mission Objectives
The primary mission is to create an algorithm that randomly assigns people to seats in the open space.

# What does this project do?
Loads a list of colleagues from new_colleagues.csv

Randomly distributes people to seats in the open space.

Handles scenarios where there are more people than available seats.

Writes the tables with the assigned collaegues to sorted_tables.txt

# Available scripts
file_utils.py: Handles file operations, including loading colleagues from new_colleagues.

table.py: Defines the Seat and Table classes representing individual seats and tables.

openspace.py: Contains the Openspace class responsible for organizing colleagues and managing tables.

main.py: Entry point of the program, loads data, initializes the Openspace, and displays the seating arrangement.
Execution

# To run the program:

1 Ensure Python is installed on your system.

2 Navigate to the project directory.

3 Execute python main.py to see the seating arrangement.
