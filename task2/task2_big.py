# Import needed modules
import sys
import getopt
import csv
from faker import Faker # a module for generating synthetic data
from datetime import datetime

fake = Faker() 
# fake.profile() creates data of a person with the following fields:
# job, company, ssn, residence, current_location, blood_group, website, username, name, sex, address, mail, birthdate

# Chunksize
outsize = 1024 * 1024 * 1024 # 1GB

def csv_generator(number_of_rows, csv_file):
    '''
    Returns the csv file called cvsfile with number of rows number_of_rows
    generated randomly by using the module faker  
    '''
    t0 = datetime.now()

    print(f"Creating csvfile {csv_file} ...")

    size = 0
    while size < outsize:
        csv_file_header = list(fake.profile().keys())
        writer.writerow(csv_file_header)
        for _ in range(1, number_of_rows):
            new_row = fake.profile().values()
            writer.writerow(new_row)
            size += len(new_row)

    t1 = datetime.now()
    print(f'{csvfile.name} was successfully created with {number_of_rows} rows!')
    t1 = datetime.now()
    print(f'Time elapsed {t1 - t0}.')
    print(f'Size of {csvfile.name} is {sys.getsizeof(csvfile)}.')
