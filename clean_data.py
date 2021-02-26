import sys
import csv
import time
import json

if len(sys.argv) != 4:
    print("Usage: python {} <input_file_name.csv> <output_file_name.csv> <output_file_name_2.csv>".format(sys.argv[0]))
    sys.exit()

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
output_file_name_2 = sys.argv[3]

out_file = open(output_file_name, 'w')
out_file_2 = open(output_file_name_2, 'w')

with open(input_file_name) as in_file:
    csv_reader = csv.reader(in_file, delimiter=',')
    csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer_2 = csv.writer(out_file_2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    line_num = 0
    kept_entry_count = 0
    for row in csv_reader:
        if line_num == 0:
            print('Column names are {}'.format(','.join(row)))
            csv_writer.writerow(row)
            csv_writer_2.writerow(row)
        else:
            path = json.loads(row[10])
            path_len = len(path["coordinates"])
            print("Index: {}\tDistance: {}\tMinutes: {}\tLenth of path: {}".format(row[0], row[5], row[8], path_len), end="\t")
            keep = path_len > 1 and int(row[8]) < 180 and int(row[8]) > 0 and float(row[5]) < 50
            if keep:
                csv_writer.writerow(row)
                kept_entry_count += 1
                print("KEPT")
            else:
                csv_writer_2.writerow(row)
                print("DELETED")
        line_num += 1
    print("Kept {} entries out of {}".format(kept_entry_count, line_num-1))

print("DONE")
