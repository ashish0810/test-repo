import sys
import csv
import time
import json
from point_in_polygon import point_in_polygon

if len(sys.argv) != 4:
    print("Usage: python {} <input_file_name.csv> <campus_boundaries.csv> <output_file_name.csv>".format(sys.argv[0]))
    sys.exit()

input_file_name = sys.argv[1]
campus_boundaries_file_name = sys.argv[2]
output_file_name = sys.argv[3]

out_file = open(output_file_name, 'w')

boundaries = []

with open(campus_boundaries_file_name) as campus_boundaries_file:
    csv_reader = csv.reader(campus_boundaries_file, delimiter=',')
    line_num = 0
    for row in csv_reader:
        if line_num == 0:
            # do nothing
            print("Loading the boundaries into memory")
        else:
            boundaries.append([float(row[1]), float(row[2])])
        line_num += 1
    print("Loaded {} boundary points".format(line_num-1))

with open(input_file_name) as in_file:
    csv_reader = csv.reader(in_file, delimiter=',')
    csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    line_num = 0
    start_on_campus = 0
    end_on_campus = 0
    start_on_end_on = 0
    start_on_end_off = 0
    start_off_end_on = 0
    start_off_end_off = 0
    for row in csv_reader:
        if line_num == 0:
            row.append("START INSIDE")
            row.append("END INSIDE")
            csv_writer.writerow(row)
        else:
            start_inside = point_in_polygon(boundaries, [float(row[12]), float(row[13])])
            end_inside = point_in_polygon(boundaries, [float(row[14]), float(row[15])])
            if start_inside:
                start_on_campus += 1
                if end_inside:
                    end_on_campus += 1
                    start_on_end_on += 1
                else:
                    start_on_end_off += 1
            else:
                if end_inside:
                    end_on_campus += 1
                    start_off_end_on += 1
                else:
                    start_off_end_off += 1
            row.append(start_inside)
            row.append(end_inside)
            csv_writer.writerow(row)
        line_num += 1
    print("Processed {} entries".format(line_num-1))
    print("Start locations:\n\t{} on campus\n\t{} off campus".format(start_on_campus, line_num-start_on_campus-1))
    print("End locations:\n\t{} on campus\n\t{} off campus".format(end_on_campus, line_num-end_on_campus-1))
    print("Start on campus, End on campus:   {}".format(start_on_end_on))
    print("Start on campus, End off campus:  {}".format(start_on_end_off))
    print("Start off campus, End on campus:  {}".format(start_off_end_on))
    print("Start off campus, End off campus: {}".format(start_off_end_off))

print("DONE")
