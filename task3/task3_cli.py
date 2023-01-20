# Import needed modules
import sys
import getopt
import csv
from task3 import csv_normalizer_custom

def usage():
    """
    Show help for the CLI program
    """
    print("python task3_cli.py -f --input_file <input_file> -d --delimiter <delimiter> -q --quote <quote> ")

input_file = None
delimiter = '|' # default delimiter
quote = '\"' # default quote
args = None
try:
    opts, args = getopt.getopt(sys.argv[1:], "h:f:d:q:", ["help","input_file=", "delimiter=","quote="])
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
        elif opt in ("-q", "--quote"):
            quote = arg

    if delimiter and input_file and quote:
        csv_normalizer_custom(input_file,delimiter,quote)

    else:
        print("Error! Please insert input_file (str)")
