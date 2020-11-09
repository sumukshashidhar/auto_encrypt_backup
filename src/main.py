import argparse

## init parser
PARSER_DOCSTRING = """
Welcome to NCryptBack.
The one stop shop for all your encrypted backup needs.

"""


parser = argparse.ArgumentParser(description=PARSER_DOCSTRING)
parser.parse_args()
parser.add_argument("-i", "--inputdir", help="The Input Directory")
parser.add_argument("-f", "--file", help="An Input File to Encrypt")
parser.add_argument("-o", "--out", help="The output file")
