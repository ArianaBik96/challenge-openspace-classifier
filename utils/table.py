from file_utils import load_file
import random


class Seat:
    def __init__(self, occupant: str):
        self.free = True
        self.occupant = occupant

    # SEATS FUNCTIONS
    def set_occupant(self, name: str):
        # if seat is free ==> add name to occupant and delete from list
        # seat is not free anymore ==> free = False
        if self.free:
            self.occupant = name
            self.free = False
        else:
            print("This seat is already taken")

    def remove_ocupant(self):
        # add name back into the list and reset occupant
        # seat is available ==> free = True
        list_colleagues.append()
        self.occupant = ""
        self.free = True


class Table:
    def __init__(self):
        self.capacity = 4
        self.seats = []  # Initialize an empty list for each table
        for _ in range(self.capacity):
            new_seat = Seat("")  # Create a new Seat instance
            self.seats.append(new_seat)

    # TABLE FUNCTIONS
    def has_free_spot(self) -> bool:
        # capacity is higher than 0 ==> there is a free spot
        return self.capacity > 0

    def assign_seat(self, name):
        if len(name) <= self.capacity:
            for i in range(len(name)):
                self.seats[i].set_occupant(name[i])
        else:
            print("Not enough seats to assign all occupants.")

    def left_capacity(self) -> str:
        str_table_capacity = "This table has " + str(self.capacity) + " free spots"  # REPLACE !!!
        return str_table_capacity


# Get list_of_colleagues from file_utils and shuffle
filename = "new_colleagues.csv"
list_colleagues = load_file(filename)
random.shuffle(list_colleagues)
print(list_colleagues)

tables = []
# Initialize 6 tables with 4 seats each
for table in range(6):
    tables.append(Table())  # Append a new Table instance to the tables list


for i, table in enumerate(tables):
    print(f"Table {i + 1}:")
    for j, seat in enumerate(table.seats):
        if not seat.free:
            print(f"  Seat {j + 1}: {seat.occupant}")
        else:
            print(f"  Seat {j + 1}: Empty")

# Get list_of_colleagues from file_utils
print("Original list_colleagues:", list_colleagues)

# Shuffle the list and print the shuffled list
random.shuffle(list_colleagues)
print("Shuffled list_colleagues:", list_colleagues)

