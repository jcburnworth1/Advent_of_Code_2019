## Day 1 Problems
## Import libraries
import os
from math import floor

## Function to load data
def load_module_data(file_name):
    directory = os.getcwd()
    files_available = os.listdir(directory + '/Advent_of_Code_2019/Day_1/')

    ## If file we need exists - Read each line into a separate item in a list
    if files_available.__contains__ (file_name):
        ## Read in the data for parsing
        with open(directory + '/Advent_of_Code_2019/Day_1/' + file_name) as file:
            module_data = file.readlines()
    else:
        print("File does not exists")

    ## Text to integers
    module_data = [int(module) for module in module_data]

    return module_data

## Function to calculate fuel requirements
def calculate_fuel_for_modules(module_mass_list):
    ## Initialize fuel_needed to zero
    fuel_needed = []

    ## Loop over list and add each value to fuel_needed
    for mass in module_mass_list:
        fuel_needed.append(floor((mass / 3) - 2))

    return fuel_needed

## Function to calculate fuel requirements including fuel
def calculate_fuel_for_modules_all(module_mass_list):
    ## Initialize fuel_needed to zero
    fuel_needed_all = []
    remainder = float('inf')

    ## Loop over list and add each value to fuel_needed including
    for mass in module_mass_list:

        ## Intial fuel for a given modules mass
        remainder = floor((int(mass) / 3) - 2)
        fuel_needed_all.append(remainder)

        while remainder > 0:

            ## Capture fuel needed for given value
            remainder = floor((int(remainder) / 3) - 2)

            if remainder > 0:
                fuel_needed_all.append(remainder)

    return fuel_needed_all