# Import needed modules
import sys
import getopt
import csv
from faker import Faker # a module for generating synthetic data
from datetime import datetime
from task2 import csv_generator # module for generating csv files

fake = Faker() 
# fake.profile() creates data of a person with the following fields:
# job, company, ssn, residence, current_location, blood_group, website, username, name, sex, address, mail, birthdate

def usage():
    """
    Show help for the CLI program
    """
    print("python task2_cli.py --number_of_rows <number_of_rows> --csv_file <csv_file>")

# Initialize the two variables
number_of_rows = None
csv_file = None

args = None
try:
    opts, args = getopt.getopt(sys.argv[1:], "h:n:f:", ["help","number_of_rows=","csvfile="])
except:
    print("Error! Please insert both number_of_rows (integer) and csv_file (str)")
    usage()
    sys.exit(2)

else:
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-n", "--number_of_rows"):
            number_of_rows = int(arg)
        elif opt in ("-f", "--csv_file="):
            csv_file = arg + '.csv'
            if csv_file:
                print(f"{csv_file} already exists, {number_of_rows} rows will be added")

    if number_of_rows and csv_file:
        csv_generator(number_of_rows,csv_file)

    else:
        print("Error! Please insert both number_of_rows (integer) and csv_file (str)")
