import csv, sys

if len(sys.argv) != 2:
    print("Please pass a csv data input as an argument.")
    exit()

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    first_line = true
    for row in csv_reader:
        print(row)