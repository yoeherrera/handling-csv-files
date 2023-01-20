# Import modules needed
import csv

# Convert pipeline-delimited CSV files to comma-delimited files

def csv_normalizer(input_file):
	output_file = 'normalized_' + input_file
	print(f"Normalizing {input_file} to comma-delimited file {output_file}")
	with open(input_file) as original_csv_file:
		# newline='' is used to prevent extra newlines when using Python 3 on Windows
		with open(output_file, 'w', newline='') as normalized_csv_file:
			reader = csv.DictReader(original_csv_file, delimiter='|')
			writer = csv.DictWriter(normalized_csv_file, reader.fieldnames, delimiter=',')
			writer.writeheader()
			writer.writerows(reader)
	print("Conversion complete.")