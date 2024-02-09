
from utils.openspace import Openspace
from utils.file_utils import load_file
import random


filename = "new_colleagues.csv" # Define the filename
list_colleagues = load_file(filename) # Load the list of colleagues from the file
random.shuffle(list_colleagues) # Shuffle the names in the list randomly


tables = [] # Initialize an empty list for tables
openspace = Openspace(tables, 6) # Initialize Openspace object with 6 tables
openspace.organize(list_colleagues) # Organize the colleagues into tables
openspace.display() # Display the arrangement of colleagues in tables
openspace.store("sorted_tables.txt", list_colleagues) # Store the arrangement of tables with occupants into a file