"""
Runs import for both new & old spreadsheets formats and csv files
"""

import csv
import xlrd


def run_spreadsheet_import(sheet_name, dataset, db):
    """
    Reads excel spreadsheet and inserts data to the database instance
    :param sheet_name:
    :param dataset_path:
    :param db:
    :return:
    """
    try:
        # Open the workbook and define the worksheet name and file name like .csv, .xls, .xlsx
        book = xlrd.open_workbook(dataset)

        # Check for sheet name parsed
        if sheet_name:
            sheet = book.sheet_by_name(sheet_name)  # Use when you have a predefined sheet name
        else:
            sheet = book.sheet_by_index(0)  # Use when you have don't require to use the sheet name

        # Get the cursor, which is used to traverse the database, line by line
        cursor = db.cursor()

        # Create the INSERT INTO sql query
        query = """
          INSERT INTO users (username, password, email, first_name, middle_name, last_name) 
          VALUES (%s, %s, %s, %s, %s, %s)
        """

        # Create a ForLoop to iterate through each row in the XLS file, starting at row 2 to skip the headers
        for r in range(1, sheet.nrows):
            username = sheet.cell(r, 0).value
            password = sheet.cell(r, 1).value
            email = sheet.cell(r, 2).value
            first_name = sheet.cell(r, 3).value
            middle_name = sheet.cell(r, 4).value
            last_name = sheet.cell(r, 5).value

            # Assign values from each row
            values = (username, password, email, first_name, middle_name, last_name)

            # Execute sql Query
            cursor.execute(query, values)

        # Close the cursor
        cursor.close()

        # Commit the transaction
        db.commit()

        # Close the database connection
        db.close()

        # Print results
        print("")
        print("All Done! Bye, for now.")
        print("")
        columns = str(sheet.ncols)
        rows = str(sheet.nrows)
        print("Imported " + columns + " columns and " + "rows to MySQL!")
    except Exception as e:
        print(e)


def run_csv_import(dataset, db):
    # Get the cursor, which is used to traverse the database, line by line
    cursor = db.cursor()

    # Get the headers from csv
    with open(dataset, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = list(csv_reader)[0]

    # Open csv file and write data to db instance
    with open(dataset, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        args = ",".join(repr(e) for e in [{} for v in headers])
        next(csv_reader)
        for row in csv_reader:
            query = """
                      INSERT INTO users ({})
                      VALUES ({})
                    """.format(args, args)
            values=['%s' for v in range(len(headers))]
            query = query.format(*headers, *values)

            # Execute sql Query
            cursor.execute(query, [row[v] for v in range(len(headers))])

        # Close the cursor
        cursor.close()

        # Commit the transaction
        db.commit()

        # Close the database connection
        db.close()
