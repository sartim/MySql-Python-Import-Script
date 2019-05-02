# MySql-Python-Import-Script
This is a python script for importing data to MySql database using .csv, .xls, or xlsx. It requires MySQLdb interface for python and xlrd package for reading data and formatting information from older Excel files.

## Setup

**Requirements**
 
* [python 2+](https://www.python.org)
* [virtualenv](https://virtualenv.pypa.io/en/latest/)
* [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html)
* [xlrd](https://xlrd.readthedocs.io/en/latest/)

**Setup**

    $ virtualenv <envname> -p python3
    $ source <envname>/bin/activate
    $ pip install -r requirements.txt

**Add dotenv to project root**

You should create a .env file on the project root. You can get this on the repo url https://github.com/hivisasapro/hivisasa-stage-dotenv

**Running script**

    $ python import.py -t XLSX -d data/users.xlsx -s source
    
###### arguments
    
_-t (type)_
    
spreadsheet, csv

_-d (dataset)_

Path to dataset

_-s (sheet name)_

Used if the dataset type in use is a spreadsheet