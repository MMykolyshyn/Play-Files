#!/usr/bin/env python\
#----------------
#Name: UNDS_DiceRoller
#Author: Michael Mykolyshyn
#Date of creation: April 25, 2016
"""This script is desighned to take inputs from dice rolls, convert them into a series of postive and negative symbols that cancel eachother out, then display the balance of symbols."""
#----------------
#set varialbes phase

pos_list = []
neg_list = []
#----------------
#function definition phase

def intake(list):
	"""Will take user input between 1 and 12 and append it a list, list is then returned"""
	print("Please input dice roll values between 1 and 12. If a zero is inputted, the list will end.")
	dice_val = 1
	while int(dice_val) > 0:
		dice_val = input(": ")
		if int(dice_val) > 0 and int(dice_val) < 13:
			list.append(int(dice_val))
		elif int(dice_val) == 0:
			print("End list")
		elif int(dice_val) > 12:
			print("Value is to large to be attributed to a symbol set. Try again.")
	return list

def sy_trans(modifyer, list):
	"""Will take values in a string and associate them to a symbol-dice side, printing the results to a sym-varialbe, the sym-varialbe will be retunred.
	Modifyer is used to determine if postive or negaive symbolod will be used (0/1 choice), list refers to list of numbers previously generated, symbol refers to the varialbe where the symbol results will be stored."""
	symbol = ""
	dic_sym_pos ={1: "", 2: "s", 3: "b", 4: "sb", 5: "bb", 6: "ss", 7: "sbb", 8: "E", 9: "ssb", 10: "sss", 11: "ssbb", 12: "E"}
	dic_sym_neg ={1: "", 2: "f", 3: "d", 4: "fd", 5: "dd", 6: "ff", 7: "fdd", 8: "B", 9: "ffd", 10: "fff", 11: "ffdd", 12: "B"}
	for value in list:
		if modifyer == 0:
			symbol += dic_sym_pos[value]
		if modifyer == 1:
			symbol += dic_sym_neg[value]
	return symbol

def sym_count(string, symbol):
	"""This funtion will take a string and then count the number of times a symbol is within it, returning that value."""
	value = string.count(symbol)
	return value

def sym_comp(pos, neg):
	"""compaire postive and negative symbol values and retuns the result"""
	result = int(pos) - int(neg)
	return result

def display_results(tally, word_pos, word_neg):
	"""will take various positive and negative symbol tally's, and produce a print out for a postive, negative, or nutral scenario utalising various word inputs."""
	if tally > 0:
		print("There are {0} {1}".format(tally, word_pos))
	elif tally < 0:
		print("There are {0} {1}".format(abs(tally), word_neg))
	else:
		print("There are neither {0} or {1}'s".format(word_pos, word_neg))

#----------------
#Script operation Phase

#input values
print("\nPOSTIVE DICE")
intake(pos_list)
print("\nNEGATIVE DICE")
intake(neg_list)

#for positive symbol conversion
pos_sym = sy_trans(0, pos_list)

#for negitive symbol conversion
neg_sym = sy_trans(1, neg_list)

#count sybols and give values for each
s_num = sym_count(pos_sym, 's')
b_num = sym_count(pos_sym, 'b')
E_num = sym_count(pos_sym, 'E')

f_num = sym_count(neg_sym, 'f')
d_num = sym_count(neg_sym, 'd')
B_num = sym_count(neg_sym, 'B')

#Count the number of sybols in each variable
pass_fail = sym_comp(s_num, f_num)
beni_defi = sym_comp(b_num, d_num)
epic_bane = sym_comp(E_num, B_num)
print('#----')

#----------------
#The display stage

print("\n---Roll Results---\nPositive :")
print(pos_list)
print("Negative : ")
print(neg_list)

print("\n---Symbol Results---\nPositive :")
print(pos_sym)
print("Negative : ")
print(neg_sym)

print("\n---Passes, Benifits, Epics:---")
print(s_num, b_num, E_num)
print(f_num, d_num, B_num)
print("Totals:")
print(pass_fail, beni_defi, epic_bane, '\n')

display_results(pass_fail, 'pass', 'fail')
display_results(beni_defi, 'benifit', 'deficet')
display_results(epic_bane, 'epic', 'bane')
#----------------
#----------------
#----------------
#----------------
#----------------
#----------------
#----------------
#----------------
#----------------
