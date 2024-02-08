
'''
saves and load files
'''

filename = "new_colleagues.csv"
list_of_colleagues=[]

def load_file(filename):
    #load file with colleague names
    my_file = open(filename, "r")
    #separate on ENTER + store names in list_of_colleagues
    list_of_colleagues = my_file.read().splitlines()
    print(list_of_colleagues)
    #close file
    my_file.close()

    return list_of_colleagues

load_file(filename)