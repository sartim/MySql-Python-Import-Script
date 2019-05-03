"""
Execute command using argument parser
"""

import sys
import argparse

from core import connection, importer


def get_arguments(argv):
    """
    Get arguments using ArgumentParser
    :param argv:
    :return args:
    """
    parser = argparse.ArgumentParser(description='CSV, XLS, XLSX data set migration to MySQL database')
    parser.add_argument('-t', '--type', help='The dataset type. Spreadsheet or csv')
    parser.add_argument('-f', '--file', help='The dataset file to use')
    parser.add_argument('-s', '--sheet', help='The sheet name to use')
    parser.add_argument('-H', '--host', help='The host name to use')
    parser.add_argument('-U', '--user', help='The username to use')
    parser.add_argument('-P', '--password', help='The password to use')
    parser.add_argument('-D', '--database', help='The database name to use')
    args = parser.parse_args()
    return args


def main(args):
    print("\nImporting...")

    # Variables #
    type = args.type
    file = args.file
    sheet = args.sheet
    host = args.host
    user = args.user
    password = args.password
    database = args.database

    db = connection.connect(user, password, host, database)
    if type == 'spreadsheet':
        if sheet:
            importer.run_spreadsheet_import(sheet, file, db)
        else:
            print("Missing sheet name!! Importing data from first index on spreadsheet")
            importer.run_spreadsheet_import(sheet, file, db)
    elif type == 'csv':
        importer.run_csv_import(file, db)



if __name__ == '__main__':
    arguments = get_arguments(sys.argv)

    if sys.version_info < (3, 0):
        input = raw_input

    proceed = input("Importing data from dataset {}\nProceed (yes/no)? ".format(arguments.file))
    valid = ["yes", "y", "no", "n"]
    while True:
        if proceed.lower() in valid:
            if proceed.lower() == "yes" or proceed.lower() == "y":
                main(arguments)
                print("Done!")
                break
            else:
                print("Goodbye!")
                break
        else:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').")
            proceed = input("\nProceed (yes/no)? ")
