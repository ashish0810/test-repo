import sys
import csv
import time
import json
from point_in_polygon import point_in_polygon

if len(sys.argv) != 4:
    print("Usage: python {} <input_file_name.csv> <customer_ride_counts.csv> <output_file_name.csv>".format(sys.argv[0]))
    sys.exit()

input_file_name = sys.argv[1]
customer_ride_counts_file_name = sys.argv[2]
output_file_name = sys.argv[3]

out_file = open(output_file_name, 'w')

customer_ride_counts = {}

with open(customer_ride_counts_file_name) as customer_ride_counts_file:
    csv_reader = csv.reader(customer_ride_counts_file, delimiter=',')
    line_num = 0
    for row in csv_reader:
        if line_num == 0:
            # do nothing
            print("Loading the customer ride counts into memory")
        else:
            customer_ride_counts[row[0]] = row[1]
        line_num += 1
    print("Loaded {} customer ride counts".format(line_num-1))

with open(input_file_name) as in_file:
    csv_reader = csv.reader(in_file, delimiter=',')
    csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    line_num = 0
    for row in csv_reader:
        if line_num == 0:
            row.append("RIDE COUNT")
            csv_writer.writerow(row)
        else:
            row.append(customer_ride_counts[row[7]])
            csv_writer.writerow(row)
        line_num += 1
    print("Processed {} entries".format(line_num-1))

print("DONE")
