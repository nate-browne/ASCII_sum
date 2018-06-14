# The CSE 12 ASCII Sum Calculator

### Description

This program is a short script used for calculating hashes according to the
formula used in CSE 12 with Gary Gillespie for the Hashtable assignment.

The program allows for the user to enter in a table size of 2 or larger, then
uses that given table size to calculate the correct values for strings entered
in. The program finishes execution when EOF is typed (CTRL + D), when a
KeyboardInterrupt signal is sent (CTRL + C), or if the user types q when
prompted for a name to calculate.

### Usage

This script can be invoked from the terminal in a UNIX system using either `python
ascii_sum_calculator.py` or by saying `./ascii_sum_calculator.py`

If the program isn't working properly, use the UNIX command `chmod` to give all
users execute permissions: `chmod ugo+x ascii_sum_calculator.py`

(Unfortunately, I'm not too sure how to get it working in a Windows environment.
Perhaps one could open up a python interpreter and run it directly? If you use
Windows, please let me know!)

The table size can be inputted in octal, hexadecimal, or in decimal,
and the program will convert it to decimal without errors (so all you who like
to use hex are good to go).

### Contact

Authored by Nate Browne, contact me at `natebrowne@outlook.com` with suggestions,
bugs, etc.
