import sys
import csv

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
            csv_writer.writerow(["idx", "long", "lat", "start", "year", "type"])
        else:
            csv_writer.writerow([row[0], row[12], row[13], "start", row[2][0:7], row[9]])
            csv_writer.writerow([row[0], row[14], row[15], "end", row[2][0:7], row[9]])
        line_num += 1
    print("Processed {} rows".format(line_num))

print("DONE")
