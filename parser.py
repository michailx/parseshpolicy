from datetime import datetime
from sys import exit
import re

# Read input file

fr = open('./input_file/PM.txt', 'r')
input_string = fr.read()
fr.close()

# Parse input file (variable input_string)
input_string = input_string.replace('\r', '')  # Remove /r at the end of each line
lines = input_string.split('\n')

table = []
table_head = ['timestamp']
table_row = []

i = 0
# Note to self --> print(repr(string)) prints the raw string including all special chars like \n
for line in lines:
    line = line.strip()  # Remove beginning and trailing white spaces on each line
    if line == "":
        # Empty line
        continue
    elif re.match('^..:..:..\.', line) is not None:
        # Timestamp
        line = line[:8]

        table_row = []
        table_row.append(line)

        # Save previous sample
        if i == 1:
            table.append(table_head)
            table.append(table_row)
        elif i > 1:
            table.append(table_row)

        # Next sample
        i += 1
    elif re.match('^30 second offered rate [0123456789]* bps', line) is not None:
        # Rate
        line = line[23:]
        line = line.split(' ')[0]  # Need to improve this
        table_row.append(line)
    elif line[:11] == 'Class-map: ':
        # Save class names. I only need to do this on the first sample, as it will be the same for all future samples.
        if i == 1:
            line = line[11:]
            line = line.split(' ')[0]  # Need to improve this
            table_head.append(line)
        elif i > 1:
            # Disregard
            continue
    else:
        # Disregard
        continue
    #print(repr(line))


# Create CSV file

file_name = datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
fw = open('./output_file/'+file_name+'.csv', 'w')
for row in table:
    csv = ','.join(row)+'\n'
    fw.write(csv)
    print csv
    csv = ''
fw.close()