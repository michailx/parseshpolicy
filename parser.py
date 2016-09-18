from datetime import datetime
import re

# Read input file

fr = open('./input_file/PM.txt', 'r')
input_string = fr.read()
fr.close()

# Parse input file (variable input_string)
input_string = input_string.replace('\r', '')  # Remove /r at the end of each line
lines = input_string.split('\n')

# Note to self --> print(repr(string)) prints the raw string including all special chars like \n
for line in lines:
    line = line.strip()  # Remove beginning and trailing white spaces on each line
    if line == "":
        # Empty line
        continue
    elif re.match('^..:..:..\.', line) is not None:
        # Timestamp
        line = line[:8]
    elif re.match('^30 second offered rate [0123456789]* bps', line) is not None:
        # Rate
        line = line[23:]
        line = line.split(' ')[0]  # Need to improve this
    else:
        # Disregard
        continue
    print(repr(line))



# Create CVS file

file_name = datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
fw = open('./output_file/'+file_name+'.csv', 'w')
fw.write('timestamp, total_input_traffic_bps, class-default, b1, b2, b3, rt2, rt, nc\n')
fw.write('08:30:04, 45000, 0000, 0000, 40000, 1000, 0000, 0000, 4000\n')
fw.close()