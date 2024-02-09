# Import with relative imports so main.py stays clean
from .table import Table  
from .file_utils import load_file
import random
import os

class Openspace:
    # Initialize Openspace with tables and the number of tables
    def __init__(self, tables, number_of_tables):
        self.tables = tables
        self.number_of_tables = number_of_tables

    def organize(self, names):        
        if len(names) > self.number_of_tables * 4:
            print("The room is too small for these many colleagues")
        else:
            for num_tables in range(self.number_of_tables):
                new_table = Table()  # Create a new Table instance
                names_for_this_table = []  # Initialize list to hold names for the table

                # Assign names to seats in the table
                for cap in range(new_table.capacity):
                    if names: # Check if there are names left in the list
                        names_for_this_table.append(names.pop(0)) # Extract and remove the first name from the list
                
                new_table.assign_seat(names_for_this_table)
                self.tables.append(new_table)  # Append the instance to the tables list  

            
    

    def display(self):
        # Display the arrangement of colleagues in tables
        # Iterate over each table in the Openspace
        for i, table in enumerate(self.tables):
            print(f"Table {i + 1}:") # Print the table number
            # Iterate over each seat in the table
            for j, seat in enumerate(table.seats):
                # Check if the seat is occupied or empty and print accordingly
                if not seat.free:
                    print(f"  Seat {j + 1}: {seat.occupant}")
                else:
                    print(f"  Seat {j + 1}: Empty")
            # Check if there are any free spots on the table and print accordingly
            if table.has_free_spot():
                print(table.left_capacity())
            else:
                print("There are no empty seats")


    def store(self, filename, names):
    # Store the arrangement of tables with occupants into a file
    # Open the file for writing (creates the file if it doesn't exist, overwrites it if it does)
        with open(filename, "w") as my_file:
            if len(names) > self.number_of_tables * 4:
                my_file.write("The room is too small for these many colleagues\n")
            else:
                # Iterate over each table in the Openspace
                for i, table in enumerate(self.tables):
                    # Write the table header to the file
                    my_file.write(f"Table {i + 1}:\n")  # Include newline character

                    # Iterate over each seat in the table
                    for j, seat in enumerate(table.seats):
                        # Check if the seat is occupied or empty and write accordingly
                        if not seat.free:
                            my_file.write(f"  Seat {j + 1}: {seat.occupant}\n")  # Include newline character
                        else:
                            my_file.write(f"  Seat {j + 1}: Empty\n")  # Include newline character    

                    # Check if there are any free spots on the table and write accordingly
                    if table.has_free_spot():
                        my_file.write(table.left_capacity())
                    else:
                        my_file.write("There are no empty seats")

                    # Add new lines between tables for clarity
                    my_file.write(f"\n\n")

