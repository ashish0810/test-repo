import sys
import csv
import time
import json

if len(sys.argv) != 3:
    print("Usage: python {} <input_file_name.csv> <output_file_name.csv>".format(sys.argv[0]))
    sys.exit()

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

out_file = open(output_file_name, 'w')

with open(input_file_name) as in_file:
    csv_reader = csv.reader(in_file, delimiter=',')
    csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    line_num = 0
    for row in csv_reader:
        if line_num == 0:
            row.append("MONEY")
            csv_writer.writerow(row)
        else:
            rate = 0.25 if row[9] == "Scooter" else 0.20
            money = 1.0 + (float(row[8])*rate)
            row.append(money)
            csv_writer.writerow(row)
        line_num += 1
    print("Processed {} entries".format(line_num-1))

print("DONE")
