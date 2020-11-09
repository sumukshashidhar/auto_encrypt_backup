import argparse

## init parser
PARSER_DOCSTRING = "\
Welcome to NCryptBack. \n\
The one stop shop for all your encrypted backup needs.\n\
"
parser = argparse.ArgumentParser(description=PARSER_DOCSTRING)
parser.parse_args()
