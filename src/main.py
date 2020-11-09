import argparse
import sys
## init parser
PARSER_DOCSTRING = """
Welcome to NCryptBack.
The one stop shop for all your encrypted backup needs.

"""


parser = argparse.ArgumentParser(description=PARSER_DOCSTRING)
parser.add_argument("-i", "--inputdir", help="The Input Directory")
parser.add_argument("-f", "--file", help="An Input File to Encrypt")
parser.add_argument("-o", "--out", help="The output file")

args = parser.parse_args()

# after recieving the arguments, they must be parsed
if args.inputdir or args.file:
    # to make sure that we have either one before continuing
    if args.inputdir:
        # dir is type 0, file is type 1
        INPUT = (0, args.inputdir)
    else:
        INPUT = (1, args.file)
else:
    sys.exit()



# testing code
print(INPUT)
