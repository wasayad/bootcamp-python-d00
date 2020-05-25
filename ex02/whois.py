import sys

argc = len(sys.argv)
if argc is not 2:
    print("Error number of arguement invalid.")
    exit()
toint = int(sys.argv[1])
if toint is 0:
    print("I'm Zero.")
elif (toint % 2) is 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
