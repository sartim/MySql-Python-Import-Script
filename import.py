# This package is for reading data and formatting information from older Excel
import xlrd

# Interface for MySQL Database
import MySQLdb

#Open the workbook and define the worksheet name and file name like .csv, .xls, .xlsx
book = xlrd.open_workbook("users.xlsx")
sheet = book.sheet_by_name("source")
# sheet = book.sheet_by_index(0)

# Establish a MySQl connection
database = MySQLdb.connect (host="localhost", user="root", db = "pharma_db")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO users (username, password, email, firstname, middlename, lastname) VALUES (%s, %s, %s, %s, %s, %s)"""

# Create a ForLoop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range (1, sheet.nrows):
		username = sheet.cell(r,0).value
		password = sheet.cell(r,1).value
		email = sheet.cell(r,2).value
		firstname = sheet.cell(r,3).value
		middlename = sheet.cell(r,4).value
		lastname = sheet.cell(r,5).value

		# Assign values from each row
		values = (username, password, email, firstname, middlename, lastname)

		# Execute sql Query
		cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ("")
print ("All Done! Bye, for now.")
print ("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("Imported " + columns + " columns and " + "rows to MySQL!")

    


