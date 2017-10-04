
import sys
import numpy

if __name__ == '__main__':
	
	fn 		= sys.argv[1]
	diameter	= float(sys.argv[2])
	
	nparticles	= int(400000/numpy.power(diameter/1000.0, 3))

	line_to_replace_1 	= 'radius gaussian number'
	replacement_line_1 	= 'radius gaussian number %f %f' % (diameter/2.0e6, diameter/2.0e7)

	line_to_replace_2	= 'nparticles'
	replacement_line_2	= 'nparticles %d particlerate %d insert_every 1000 &' % (nparticles, nparticles)

	infile = open(fn, 'r')
	data = infile.readlines()
	infile.close()

	outfile = open(fn, 'w')

	for line in data:
		if line_to_replace_1 in line:
			outfile.write(replacement_line_1 + '\n')
		elif line_to_replace_2 in line:
			outfile.write(replacement_line_2 + '\n')
		else:
			outfile.write(line)


#	print(fn)
#	print(line_to_replace)
#	print(replacement_line)


