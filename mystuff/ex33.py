from sys import argv

x = int(argv[1])
y = int(arg[2])
# Remember to cast an input as an integer as it is read in as a string
# I forgot this because I was not using the raw_input() method


def print_list_while(number, step):
	i = 0
	numbers = []
	while i < number:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + step
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


	print "The numbers: "

	for num in numbers:
		print num

def print_list_for(number, step):

	numbers =[]
	for i in range(0,number,step):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num


print_list_while(x,y)
print_list_for(x,y)