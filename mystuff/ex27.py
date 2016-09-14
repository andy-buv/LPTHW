print
print """ Tables of Logic"""

print
print "\"NOT\"	  |  TRUE?"
print "not False | ", not False		# True
print "not True  | ", not True 		# False

print
print "\"OR\"	       |  TRUE?"
print "True or False  | ", True or False 	# True
print "True or True   | ", True or True 	# True
print "False or True  | ", False or True 	# True
print "False or False | ", False or False 	# False

print
print "\"AND\"		|  TRUE?"
print "True and False  | ", True and False 	# False
print "True and True   | ", True and True 	# True
print "False and True  | ", False and True 	# False
print "False and False | ",	False and False 	# False

print
print "\"NOT OR\"		|  TRUE?"
print "not (True or False)	| ", not (True or False) 	# False
print "not (True or True)	| ", not (True or True) 	# False
print "not (False or True)	| ", not (False or True) 	# False
print "not (False or False)	| ", not (False or False) 	# True

print
print "\"NOT AND\"  		|  TRUE?"
print "not (True and False)	| ", not (True and False) 	# True
print "not (True and True)	| ", not (True and True) 	# False
print "not (False and True)	| ", not (False and True) 	# True
print "not (False and False)	| ", not (False and False) 	# True

print
print "\"!=\"	|  TRUE?"
print "1 != 0 	| ", 1 != 0 	# True
print "1 != 1	| ", 1 != 1 	# False
print "0 != 1	| ", 0 != 1 	# True
print "0 != 0	| ", 0 != 0 	# False

print
print "\"==\"	|  TRUE?"
print "1 == 0	| ", 1 == 0 	# False
print "1 == 1	| ", 1 == 1		# True
print "0 == 1	| ", 0 == 1		# False
print "0 == 0	| ", 0 == 0		# True