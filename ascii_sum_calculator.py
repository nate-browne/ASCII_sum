#!/usr/bin/env python2.7
# Author: Nate Browne
# Version: 1.7
# Date: 24 June 2017
# Last Edited: 24 July 2017
# File: ascii_sum_calculator.py
# Contact: natebrowne@outlook.com

"""
PROGRAM DESCRIPTION:
This program uses the hashing formulas provided in CSE 12 at UCSD with Gary
Gillespie for the HashTable assignment (hw6). Finds the ASCII sum, initial
location in the table, increment, and probe sequence for a user entered string
with a user entered table size.
"""

def find_ASCII(s):
"""
Calculates the ASCII sum of the given string
param: s is the string to calculate
return: the ASCII sum
"""

    return sum(map(ord, s))

def find_init(a_sum, table_size):
"""
Finds the initial hash location of the ASCII sum by modding the sum by the size
of the table.
param: a_sum is the ASCII sum of the string to find location for
param: table_size is the size of the table
return: the initial location
"""

    return a_sum % table_size

def find_incr(a_sum, table_size):
"""
Finds the incrementor used in finding the probe sequence by modding the sum by
the size of the table minus one and adding one to that total.
param: a_sum is the ASCII sum of the string to find the increment for
param: table_size is the size of the table
return: the increment value
"""

    return (a_sum % (table_size - 1)) + 1

def find_probe_sequence(init, incr, table_size):
"""
Finds the probe sequence and saves it into a list. Every value besides the first
is found by adding the previous answer plus the increment total and modding that
sum by the table size.
param: init the number found from init
param: incr the number found from incr
param: table_size is the size of the table
return: a list containing the probe sequence
"""

    # Use this variable later to figure out how many times to loop
    # Start at 2 because the table size will already be a minimum of 2
    count = 2

    # Create list and append the first number
    answer = []
    answer.append(init)

    # Calculate the second number and append it
    to_append = (init + incr) % table_size
    answer.append(to_append)

    # Use this while loop to figure out the rest of the probe sequence
    while count < table_size:

        # Figure out the next number in the sequence and assign it
        to_append = next_num = (to_append + incr) % table_size

        # Add the number to the list and increment the count up by 1
        answer.append(next_num)
        count += 1

    return answer

def get_table_size():
"""
Function used once in main to get the desired size of the table from the user.
Table size has to be at least 2 so that calculations aren't negative or do not
involve dividing by zero.
return: the size of the table desired by the user for use in the rest of the
program
"""

    try:

        # Grab the table size
        table_size = int(input("Enter a table size (prime numbers please!): "))

        # Error check to make sure the table size at least of size 2
        if table_size < 2:

            # Report error back to user
            print 'ERROR: Table size %d out of range!' % (table_size)

            # Send error back to calling function to be sorted out
            raise EOFError

    # Handle case of user entering in non-numeric input
    except (NameError):

        # Report error back to user
        print 'ERROR: Invalid entry. Use a positive prime number please!'

        # Send error back to calling function to be sorted out
        raise EOFError

    return table_size

def get_string():
"""
Function called in the while loop used to grab the string the user wants to
find the information for.
return: the user-entered string
"""

    # Grab the user's string to convert
    usr_str = raw_input("Enter a string to find the ASCII sum of ('q' to quit):"
                        " ")

    # Exit condition for user entering 'q'
    if usr_str.upper() == 'Q':

        # Throw an exception to end execution of the while loop in main
        raise KeyboardInterrupt
    else:

        return usr_str

def main():
"""
Main function of program. Runs an infinite loop and delegates towards other
functions
"""
    print

    try:

        # Get the user's table size
        table_size = get_table_size()

        # Start the infinite loop
        while True:

            # Get the user's string to convert
            s = get_string()

            # Calcuate the sum, initial value, increment, and probe sequence
            # from the user's entered string
            a_sum = find_ASCII(s)
            init = find_init(a_sum, table_size)
            incr = find_incr(a_sum, table_size)
            sequence = find_probe_sequence(init, incr, table_size)

            # Display the results
            print
            print '*' * 55
            print "The ASCII sum for %s is: %d." % (repr(s), a_sum)
            print "The initial CSE 12 HashTable spot for %s is: %d." % (repr(s),
                                                                        init)
            print "The incrementor for %s is: %d." % (repr(s), incr)
            print "The probe sequence for %s is: %s." % (repr(s),
                                                         repr(sequence))
            print '*' * 55
            print

    # Catch the two types of errors thrown in the program
    except (EOFError, KeyboardInterrupt):

        print "\nExiting...\n"

# standard boilerplate to run the main function
if __name__ == '__main__':
    main()
