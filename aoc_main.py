## Updated to new environment
################################# Day 1 #################################
## Fuel required to launch a given module is based on its mass. Specifically, to find the fuel
## required for a module, take its mass, divide by three, round down, and subtract 2.
## Import needed libraries
import Advent_of_Code_2019.aoc_fuel_functions as aoc_fuel_functions

## Load fuel data
module_data = aoc_fuel_functions.load_module_data('module_inputs.txt')

## Call calculate_fuel function
fuel_needed = aoc_fuel_functions.calculate_fuel_for_modules(module_data)

## Print required fuel
print("Required Fuel for Modules: {0}".format(sum(fuel_needed)))

## What is the sum of the fuel requirements for all of the modules on your spacecraft when
## also taking into account the mass of the added fuel? (Calculate the fuel requirements
## for each module separately, then add them all up at the end.)
fuel_needed = aoc_fuel_functions.calculate_fuel_for_modules_all(module_data)

## Print new required fuel value
print("Required Fuel after accounting for weight of fuel: {0}".format(sum(fuel_needed)))

################################# Day 2 #################################
## An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking
## at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode
## indicates what to do; for example, 99 means that the program is finished and should immediately halt.
# Encountering an unknown opcode means something went wrong.
## Import needed libraries
import Advent_of_Code_2019.aoc_computer_functions as aoc_computer_functions

## Load up gravity program
gravity_program = aoc_computer_functions.load_gravity_program('gravity_program.txt')

## Run program
problem_code = aoc_computer_functions.run_gravity_program(gravity_program)

## Find the input noun and verb that cause the program to produce the output 19690720. What is 100 *
## noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)
