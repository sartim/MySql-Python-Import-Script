import sys
import argparse

from mysql_ import connection, importer


def get_arguments(argv):
    parser = argparse.ArgumentParser(description='CSV, XLS, XLSX data set migration to MySQL database')
    parser.add_argument('-t', '--type', help='The dataset type. Example CSV, XLS, XLSX')
    parser.add_argument('-d', '--dataset', help='The dataset file to use')
    parser.add_argument('-s', '--sheet', help='The sheet name to use')
    args = parser.parse_args()
    return args


def main(args):
    print("\nImporting...")

    # Variables #
    type = args.type
    dataset = args.dataset
    sheet = args.sheet

    db = connection.connect()
    if type == 'spreadsheet':
        if sheet:
            importer.run(sheet, dataset, db)
        else:
            print("Missing sheet name!! Importing data from first index on spreadsheet")
            importer.run(sheet, dataset, db)


if __name__ == '__main__':
    arguments = get_arguments(sys.argv)

    if sys.version_info < (3, 0):
        input = raw_input

    proceed = input("Importing data from dataset {}\nProceed (yes/no)? ".format(arguments.dataset))
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
