
infile = open('input.txt', 'r')
# out = open('output.txt', 'w')

lines = infile.readlines()

sum = 0

for index, line in enumerate(lines):
	helper = ''
	for c in line:
		if c.isdigit():
			helper += c 
		if len(helper) == 1:
			helper = helper * 2
	# only use first and last digit
	helper = helper[0] + helper[-1]

	print(helper)
	sum += int(helper)
	# out.write(f'{helper} \n')

print(sum)	


infile.close()
# out.close()
