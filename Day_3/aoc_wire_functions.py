## Day 2 Problems
## Import libraries
import os
from matplotlib import pyplot as plt
import collections

## Function to load data
def load_wires():
    directory = "Advent_of_Code_2019/Day_3/"
    files_available = os.listdir(directory)

    ## If files we need exists - Read each line into a separate item in a list in seperate lists
    if files_available.__contains__('wire1.txt') & files_available.__contains__('wire2.txt'):
        ## Read in the data for parsing
        ## Wire 1
        with open(directory + 'wire1.txt') as file:
            wire1 = file.readlines()

        file.close()

        ## Wire 2
        with open(directory + 'wire2.txt') as file:
            wire2 = file.readlines()

        file.close()

        ## Clean characters from each
        wire1 = [line.rstrip() for line in wire1]
        wire2 = [line.rstrip() for line in wire2]

        return wire1, wire2

def create_wire_points(wire_directions):
    current_x = 0; current_y = 0;
    wire_points = [[current_x, current_y]]

    for wire in wire_directions:

        current_point = wire_points[-1]

        if wire[0] == 'R':
            wire_points.append([
                current_point[0] + int(wire[1:]),
                current_point[1]])
        elif wire[0] == 'L':
            wire_points.append([
                current_point[0] + -int(wire[1:]),
                current_point[1]])
        elif wire[0] == 'U':
            wire_points.append([
                current_point[0],
                current_point[1] + int(wire[1:])])
        elif wire[0 == 'D']:
            wire_points.append([
                current_point[0],
                current_point[1] + -int(wire[1:])])
        else:
            continue

    return wire_points

