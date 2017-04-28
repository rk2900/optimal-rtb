import os
import sys

def get_header(folder, postfix):
	files = os.listdir(folder)
	header = "prop\tclks\tbids\timps\tbudget\tspend\talgo\tpara\trevenue\troi\tcampaign"
	for f in files:
		if not f.endswith(postfix):
			continue
		file_path = os.path.join(folder, f)
		fi = open(file_path)
		lines = fi.read().split('\n')
		if len(lines) < 2:
			continue
		header = lines[0]; break
	return header



postfix = ".best.perf.tsv"

if len(sys.argv) < 3:
	print "python aggregate.py result_folder postfix(.best.perf.tsv)"
	exit(-1)

folder = sys.argv[1]
postfix = sys.argv[2]

files = os.listdir(folder)
fo = open(folder + '/integration.txt', 'w')
header = get_header(folder, postfix)
fo.write(header + '\n')

for f in files:
	if not f.endswith(postfix):
		continue
	file_path = os.path.join(folder, f)
	fi = open(file_path)
	lines = fi.read().split('\n')
	if len(lines) < 2:
		continue
	num = 0
	for line in lines:
		if num > 0 and len(line) > 0:
			fo.write(line + '\n')
		num += 1
	fi.close()

fo.close()