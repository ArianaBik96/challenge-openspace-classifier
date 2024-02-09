class Seat:
    def __init__(self, occupant: str):
        # Initialize a seat with an occupant (or empty string if unoccupied) and set it as free
        self.free = True
        self.occupant = occupant

    # SEATS FUNCTIONS
        # Function to set an occupant to the seat
    def set_occupant(self, name: str):
        # If the seat is free, assign the occupant and mark the seat as occupied
        if self.free:
            self.occupant = name
            self.free = False
        else:
            # If the seat is already taken, print a message
            print("This seat is already taken")
    
    # Function to remove an occupant from the seat
    def remove_occupant(self):
        # If the seat is occupied, remove the occupant and mark the seat as free
        if not self.free:
            self.occupant = ""
            self.free = True
        else:  # If the seat is already empty, print a message
            print("This seat is already empty")


class Table:
    def __init__(self):
        # Initialize a table with a capacity of 4 and create empty seats
        self.capacity = 4
        self.seats = []  # Initialize an empty list for each table
        for cap in range(self.capacity):
            # Iterate over the range of the table's capacity to create seats
            new_seat = Seat("")  # Create a new Seat instance
            self.seats.append(new_seat)

    # TABLE FUNCTIONS
            # Function to check if the table has a free spot
    def has_free_spot(self) -> bool:
        # Check if any seat in the table is free
        for seat in self.seats:
            if not seat.free:
                self.capacity -1

         # If the capacity is reduced to 0, there are no free spots
        if self.capacity == 0:
            return True
        else:
            return False
    # Function to assign seats to occupants
    def assign_seat(self, names):
        for i in range(len(names)):
             self.seats[i].set_occupant(names[i])

    # Function to get the number of free spots on the table
    def left_capacity(self) -> str:
        # Return a string indicating the number of free spots on the table
        str_table_capacity = "This table has " + str(self.capacity) + " free spots"
        return str_table_capacity