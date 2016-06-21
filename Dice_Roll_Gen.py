#!/usr/bin/env python
#----------------
#Name: Dice_Roll_Gen
#Author: Michael Mykolyshyn
#Date of creation: April 11, 2016
"""Purpose is to allow input of a number of an size of dice to then print a list of results"""
#----------------
from random import randrange
master_counter = 1 #used for the loop of the program

while master_counter == 1: #start a loop
    #Initalise Variables and moduals
    """Use randrage to create random numbers (to simulate dice rolls). dice_roll_dict is a dictionary used to hold dice size and ammounts. dice_values is used to old lists of dice roll results."""
    dice_roll_dict = {}
    dice_values = []

    #----------------
    #Define functions
    def dice_gen(dictionary):
        """Takes and imput for side and number and then makes 2 lists (OR A DICTIONARY) that lists/links dice sides to dice number. It will return the lists/Dictonary to Main."""
        """counter1 is used to keep looping through dice attribute intake. number_of_dice is used to both start and iput loop and determine dice size. side is used to mark dice size. number is used to makr dice ammount. side_num_dict is used to hold side and number in a dictionary input structure."""
        counter1 = 1
        number_of_dice = 1
        print("Please input the ammount and size of dice to be rolled. To end the input please select 0.")
        while counter1 == 1:
            print("----\nDice set #{}.".format(number_of_dice))
            side = input("Sides of the Dice:")
            number = input("Number of the Dice:")
            if int(side) > 0 and int(number) > 0:
                side_num_dict = {side: number}
                dictionary.update(side_num_dict)
                number_of_dice += 1
            else:
                counter1 = 0
        return dictionary

    def num_gen(dictionary, list):
        """takes input (lists or dictionary) and will create an operation that will generate numbers in that range (sides) a nuber of times (number) into a list to be displayed. This lists elemens will be inviduals list of each dice types outputs."""
        """element_list is a list used to hold values of dice resuts. count is used to loop through appending random dice rolls."""
        for side, number in dictionary.items():
            element_list = []
            element_list.append("For D{}:".format(side))
            count = int(number)
            while count > 0:
                element_list.append(randrange(1, int(side)+1))
                count -= 1
            list.append(element_list)
        return list

    def display_results(dictionary, list):
        """takes a dictionary and list input and prints them in an approriate format for this script."""
        print("----\nYou selected the folliwng dice:")
        for side, number in dictionary.items():
            print(number + "D" + side)
        print("----\nThey outputted the following values:")
        for output in list:
            print(output[0], output[1:])

    #----------------
    #Run script
    print("---Dice Roll Genderator---\nInput values for dice saides and numbers and have a list of rolls displayed for you!")
    dice_gen(dice_roll_dict)
    print(dice_roll_dict)
    num_gen(dice_roll_dict, dice_values)

    #----------------
    #Print results
    display_results(dice_roll_dict, dice_values)
    question = input("Another set of rolls? (n)")
    if question == 'n':
        master_counter = 0
#----------------
print('#----')
#----------------
#----------------
#----------------
#----------------
#----------------
#----------------
#----------------
#----------------
#----------------
#----------------
#----------------
