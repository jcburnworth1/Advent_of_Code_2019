## Day 2 Problems
## Import libraries
import os

## Function to load data
def load_gravity_program(file_name):
    directory = os.getcwd()
    files_available = os.listdir(directory + '/Advent_of_Code_2019/Day_2/')

    ## If file we need exists - Read each line into a separate item in a list
    if files_available.__contains__ (file_name):
        ## Read in the data for parsing
        with open(directory + '/Advent_of_Code_2019/Day_2/' + file_name) as file:
            gravity_program = file.readlines()
    else:
        print("File does not exists")

    ## Text to integers
    gravity_program = [int(item) for item in gravity_program]

    return gravity_program

## Function to run the gravity program
def run_gravity_program(gravity_program_list, initial_value_1=12, initial_value_2=2):
    ## Update position 1 & 2 bases on problem ask
    gravity_program_list[1] = initial_value_1
    gravity_program_list[2] = initial_value_2

    ##### Variables to process the program #####
    ## Starting Indexes - Will update during while loop
    opcode_index = 0; value_1_index = 1; value_2_index = 2; update_position_index = 3

    ## Index values - Will be used to get program value and update appropriate indexes
    opcode_value = gravity_program_list[opcode_index]; value_1 = gravity_program_list[value_1_index]
    value_2 = gravity_program_list[value_2_index]; update_position = gravity_program_list[update_position_index]

    ## Loop until 99 causes program termination
    while opcode_value != 99:
        ## opcode of 1 means addition
        if opcode_value == 1:
            gravity_program_list[update_position] = gravity_program_list[value_1] + gravity_program_list[value_2]
        ## opcode of 2 means multiplication
        elif opcode_value == 2:
            gravity_program_list[update_position] = gravity_program_list[value_1] * gravity_program_list[value_2]
        ## opcode of 99 means terminate
        elif opcode_value == 99:
            break

        ## Increment all indexes by 4 for the next code grouping
        opcode_index += 4; value_1_index += 4; value_2_index += 4; update_position_index += 4

        ## Get new index values
        opcode_value = gravity_program_list[opcode_index]; value_1 = gravity_program_list[value_1_index];
        value_2 = gravity_program_list[value_2_index]; update_position = gravity_program_list[update_position_index]

    code = gravity_program_list[0]
    return code

## Function to execute gravity assist
def execute_gravity_assist(gravity_program_list):
    ## Generate lists of values from 0-99
    noun_possibilities = list(range(100))
    verb_possibilities = list(range(100))

    for noun in noun_possibilities:
        print("Noun: {0}".format(noun))

        for verb in verb_possibilities:
            print("Verb: {0}".format(verb))

            ## Copy list so we can recreate with each iteration
            gravity_program_list_copy = gravity_program_list.copy()

            ## Call run_gravity_program
            code = run_gravity_program(gravity_program_list_copy, initial_value_1=noun, initial_value_2=verb)

            ## Print values
            print("####################")
            print("Noun: {0}".format(noun))
            print("Verb: {0}".format(verb))
            print("Code: {0}".format(code))
            print("####################")

            ## Check if code aligns to desired output
            if code == 19690720:
                print("########## Match Found ##########")
                print("Noun: {0}".format(noun))
                print("Verb: {0}".format(verb))
                print("Code: {0}".format(code))
                print("Noun * Verb Value: {0}".format(100 * noun + verb))
                print("#################################")
                return noun, verb, 100 * noun + verb
