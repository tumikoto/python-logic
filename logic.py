#!/usr/bin/python3.6

import os
import operator


def main():
    os.system("clear")
    opt_list = [accept_and_store,
                calculator,
                print_string,
                compare_nums,
                remove_str_letter,
                exit]
    while True:
        print("SELECT AN OPTION:\n")
        print("1\tAccept a string and store it.")
        print("2\tBasic calculator functions.")
        print("3\tPrint a string that was stored.")
        print("4\tCompare numbers and return largest.")
        print("5\tRemove a letter from a string.")
        print("\n6\tExit.")
        opt_choice = int(input("Selection: "))
        opt_choice -= 1
        opt_list[opt_choice]()

    return


def accept_and_store():
    os.system("clear")
    print("Accept a string and store it.")
    global saved_string
    saved_string = str(input("Type string to be saved: "))
    return


def calculator():
    os.system("clear")
    print("Basic calculator functions.")

    op_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}

    num1 = int(input("Enter first number: "))
    num_op = str(input("Enter operation symbol ( + - * / ): "))
    num2 = int(input("Enter second number number: "))
    print(op_dict[num_op](num1, num2))
    return


def print_string():
    os.system("clear")
    print("Print a string that was stored.")
    print(saved_string)
    return


def compare_nums():
    os.system("clear")
    print("Compare numbers and return largest.")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 > num2:
        print("The first number " + str(num1) + " is bigger.")
    elif num2 > num1:
        print("The second number " + str(num2) + " is bigger.")
    elif num1 == num2:
        print("These numbers are the same size! Both are " + str(num1) + ".")

    return


def remove_str_letter():
    os.system("clear")
    print("Remove a letter from a string.")
    str1 = str(input("Enter the string to remove a letter from: "))
    letter = str(input("Enter the letter to remove from the string: "))
    if letter not in str1:
        print("Letter is not in string! Cannot remove.")
        return
    str1_strip = ""
    for char in str1:
            if char != letter:
                str1_strip += char
    print(str1_strip)
    return


main()
