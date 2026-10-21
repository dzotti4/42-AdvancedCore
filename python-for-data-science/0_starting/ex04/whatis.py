import sys

if len(sys.argv) == 1:
    exit()

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    exit()

try:
    number = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    exit()

if number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
