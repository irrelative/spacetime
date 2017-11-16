""" Convert wiki index to csv for loading into mariadb """

import csv, sys

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
with open(sys.argv[1]) as f:
    for line in f:
        line = line.decode('utf-8')
        writer.writerow([s.encode('utf-8') for s in line.strip().split(':', 2)[1:]])
