from sys import *

if len(argv)<2:
    exit("Too few arguments")
for arg in argv[1:]:
    print("hello, my name is",arg)
