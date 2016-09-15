from datetime import datetime

fr = open('./input_file/PM.txt', 'r')
input_string = fr.read()
fr.close()
# do something with variable text

file_name = datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
fw = open('./output_file/'+file_name+'.csv', 'w')
fw.write('timestamp, total_input_traffic_bps, class-default, b1, b2, b3, rt2, rt, nc\n')
fw.write('08:30:04, 45000, 0000, 0000, 40000, 1000, 0000, 0000, 4000\n')
fw.close()