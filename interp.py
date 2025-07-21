import sys

def ev(s):
    print(s)

ev(open(sys.argv[1]).read()) #open file and reads it into a string passing to ev
