# This package is for reading data and formatting information which supports old Excel format
import xlrd


def run(sheet_name, dataset_path, db):
    """
    Reads data set and inserts data to the database instance
    :param sheet_name:
    :param dataset_path:
    :param db:
    :return:
    """
    try:
        # Open the workbook and define the worksheet name and file name like .csv, .xls, .xlsx
        book = xlrd.open_workbook(dataset_path)

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
