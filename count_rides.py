import sys
import csv

if len(sys.argv) != 3:
    print("Usage: python {} <input_file_name.csv> <output_file_name.csv>".format(sys.argv[0]))
    sys.exit()

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

customer_ride_counts = {}

with open(input_file_name) as in_file:
    csv_reader = csv.reader(in_file, delimiter=',')
    line_num = 0
    for row in csv_reader:
        if line_num == 0:
            print("Counting customer rides")
        else:
            if row[7] in customer_ride_counts:
                customer_ride_counts[row[7]] += 1
            else:
                customer_ride_counts[row[7]] = 1
        line_num += 1
    print("Processed {} rows".format(line_num))

with open(output_file_name, 'w') as out_file:
    csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["customer_id", "rides"])
    for customer_id in customer_ride_counts:
        csv_writer.writerow([customer_id, customer_ride_counts[customer_id]])

print("DONE")
