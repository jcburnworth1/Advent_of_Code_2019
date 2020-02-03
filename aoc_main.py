## Updated to new environment
################################# Day 1 #################################
## Fuel required to launch a given module is based on its mass. Specifically, to find the fuel
## required for a module, take its mass, divide by three, round down, and subtract 2.
## Import needed libraries
import Advent_of_Code_2019.Day_1.aoc_fuel_functions as aoc_fuel_functions

## Load fuel data
module_data = aoc_fuel_functions.load_module_data('module_inputs.txt')

## Call calculate_fuel function
fuel_needed = aoc_fuel_functions.calculate_fuel_for_modules(module_data)

## Print required fuel
print("Required Fuel for Modules: {0}".format(sum(fuel_needed)))

## What is the sum of the fuel requirements for all of the modules on your spacecraft when
## also taking into account the mass of the added fuel? (Calculate the fuel requirements
## for each module separately, then add them all up at the end.)
fuel_needed_all = aoc_fuel_functions.calculate_fuel_for_modules_all(module_data)

## Print new required fuel value
print("Required Fuel after accounting for weight of fuel: {0}".format(sum(fuel_needed_all)))

################################# Day 2 #################################
## An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking
## at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode
## indicates what to do; for example, 99 means that the program is finished and should immediately halt.
# Encountering an unknown opcode means something went wrong.
## Import needed libraries
import Advent_of_Code_2019.Day_2.aoc_computer_functions as aoc_computer_functions

## Load up gravity program
gravity_program = aoc_computer_functions.load_gravity_program('gravity_program.txt')

## Run program
code = aoc_computer_functions.run_gravity_program(gravity_program)

## Print code that restores gravity
print("Gravity Restored: {0}".format(code))

## Find the input noun (address 1) and verb (address 2) that cause the program to produce the output 19690720.
## What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)
## Values can be between 0 - 99 for both addresses
## Load up gravity program
gravity_program = aoc_computer_functions.load_gravity_program('gravity_program.txt')

## Run program - Brute force method
noun,verb, result = aoc_computer_functions.execute_gravity_assist(gravity_program)

################################# Day 3 #################################
# ...........
# .+-----+...
# .|.....|...
# .|..+--X-+.
# .|..|..|.|.
# .|.-X--+.|.
# .|..|....|.
# .|.......|.
# .o-------+.
# ...........
# These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

# Here are a few more examples:
# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
# What is the Manhattan distance from the central port to the closest intersection?
## Import needed libraries
import Advent_of_Code_2019.Day_3.aoc_wire_functions as aoc_wire_functions

## Load up the wire data
wire1, wire2 = aoc_wire_functions.load_wires()