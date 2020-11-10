import argparse
import sys
import os
# init parser
PARSER_DOCSTRING = """
Welcome to NCryptBack.
The one stop shop for all your encrypted backup needs.
"""


def remove_old_zip(PATH):
    """Takes in a path to the generated old zip file and deletes
    after encryption is complete

    Args:
        PATH (string): path to the old zip file
    """
    remove_old_zip = f'rm {PATH}.zip'
    os.system(remove_old_zip)


def decrypt(PATH):
    """Decrypts a .zip.aes file if given a password to do so

    Args:
        PATH (string): path to the .zip.aes file
    """
    decrypt_cmd = f'openssl aes-256-cbc -d -in {PATH} -out {PATH[:-4]}'
    os.system(decrypt_cmd)
    remove_encrypted_cmd = f'rm {PATH}'
    os.system(remove_encrypted_cmd)


def encrypt(PATH):
    """Encrypts a .zip file to a .zip.aes file with a password

    Args:
        PATH (string): path to the .zip file
    """
    encrypt_string_cmd = f'openssl aes-256-cbc -in {PATH[:-1]}.zip\
                        -out {PATH}.zip.aes'
    os.system(encrypt_string_cmd)


def zipper(INPUT):
    """Given a directory or a file, zips it

    Args:
        INPUT (string): path to the directory
    """
    if INPUT[0] == 0:
        # means that we're dealing with a folder
        zip_cmd = f'zip -r {INPUT[1][:-1]}.zip {INPUT[1]}'

    elif INPUT[0] == 1:
        zip_cmd = f'zip {INPUT[1]}.zip {INPUT[1]}'

    os.system(zip_cmd)



def encryptor_class


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=PARSER_DOCSTRING)
    parser.add_argument("-i", "--inputdir", help="The Input Directory")
    parser.add_argument("-f", "--file", help="An Input File to Encrypt")
    parser.add_argument("-o", "--out", help="The output file")
    parser.add_argument("-d", "--decrypt", help="Path to encrypted file")
    args = parser.parse_args()

    # after recieving the arguments, they must be parsed
    if args.inputdir or args.file:
        # to make sure that we have either one before continuing
        if args.inputdir:
            # dir is type 0, file is type 1
            INPUT = (0, args.inputdir)
        else:
            INPUT = (1, args.file)

        zipper(INPUT)
    else:
        if args.decrypt:
            decrypt(args.decrypt)
        else:

            print("NCrypt needs args to run")
            sys.exit()
