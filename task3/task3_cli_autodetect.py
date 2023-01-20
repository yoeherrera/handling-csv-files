# Import needed modules
from __future__ import unicode_literals
import sys
import getopt
import csv
from task3 import csv_normalizer_custom

# Use Sniffer to find the delimiter reading small portion of the csv file
def get_delimiter(file_path, bytes = 4096):
    sniffer = csv.Sniffer()
    data = open(file_path, "r").read(bytes)
    print(data)
    delimiter = sniffer.sniff(data).delimiter
    return delimiter

def usage():
    """
    Show help for the CLI program
    """
    print("python task3_cli.py -f --input_file <input_file> -d --delimiter <delimiter> -q --quotechar <quote> ")

# Default values for delimiter and the quotechar
input_file = None
delimiter = '|' # default delimiter
quotechar = '"' # default quotechar
args = None
try:
    opts, args = getopt.getopt(sys.argv[1:], "h:f:d:q:", ["help","input_file=", "delimiter=","quotechar="])
except:
    print("Error! Please insert input_file (str)")
    usage()
    sys.exit(2)

else:
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-f", "--input_file="):
            input_file = arg
            output_file = 'normalized_' + input_file
            if output_file:
                print(f"{output_file} already exists, {input_file} rows will be transformed and added")
        elif opt in ("-d", "--delimiter"):
            delimiter = arg
        elif opt in ("-q", "--quotechar"):
            quotechar = arg

    if input_file and delimiter and quotechar:
        csv_normalizer_custom(input_file,delimiter,quotechar)

    elif input_file and not(delimiter):
        delimiter = get_delimiter(input_file)

    else:
        print("Error! Please insert input_file (str)")
