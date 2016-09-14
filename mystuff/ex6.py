# Assigns x with "Stringed sentence" inserting 10 into %d
x = "There are %d types of people." % 10
# Assigns binary the string binary
binary = "binary"
# Assigns do_not the String don't
do_not = "don't"
# Assigns y with "Stringed sentence" inserting the stringed values of binary and do_not.
y = "Those who know %s and those who %s." % (binary, do_not) # insert string count 1 & 2
# Prints x
print x
# Prints y
print y

# Prints string 'I said: ' inserting string x. count 3
print "I said: %r." % x
# Prints string 'I also said: ' inserting string y. count 4
print "I also said: '%s'." % y

# Assigns hilarious with boolean value False
hilarious = False
# Assigns joke_evaluation with string leaving a place to insert a value
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints joke_evaluation inserting value for hilarious
print joke_evaluation % hilarious

# Assigns w with string
w = "This is the left side of... "
# Assigns e with string
e = "a string with a right side."

# Prints String w followed by string e
print w + e