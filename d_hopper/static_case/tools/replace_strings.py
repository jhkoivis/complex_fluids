
import sys


if __name__ == '__main__':
	
	fn = sys.argv[1]
	
	line_to_replace = sys.argv[2]
	
	replacement_line = sys.argv[3]

	infile = open(fn, 'r')
	data = infile.readlines()
	infile.close()

	outfile = open(fn, 'w')

	for line in data:
		if line_to_replace in line:
			outfile.write(replacement_line + '\n')
		else:
			outfile.write(line)


	print(fn)
	print(line_to_replace)
	print(replacement_line)


