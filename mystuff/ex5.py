# Assigns 'name' with string 'Zed A. Shaw'
name = 'Zed A. Shaw'
# Assigns 'age" with integer 35 # comment
age = 35 # not a lie
# Assigns 'height' with integer 74 # comment in inches
height = 74 # inches
# Assigns 'weight' with integer 180 # comment in pounds
weight = 180 # lbs
# Assigns 'eyes' with string 'Blue'
eyes = 'Blue'
# Assigns 'teeth' with string 'White'
teeth = 'White'
# Assigns 'hair' with string 'Brown'
hair = 'Brown'

# Prints "Let's talk about %s." Inserting name value where %s is. 
print "Let's talk about %s." % name
# Prints "He's %d inches tall." Inserting height value where %d is. 
print "He's %d inches tall." % height
# Prints "He's %d pounds heavy." Inserting weight value where %d is. 
print "He's %d pounds heavy." % weight
# Prints "Actually that's not too heavy."
print "Actually that's not too heavy."
# Prints "He's got %s eyes and %s hair." Inserting eyes & hair values at %s respectively.
print "He's got %s eyes and %s hair." % (eyes, hair)
# Prints "His teeth are usually %s depending on the coffee." inserting teeth value at %s
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
# Prints ""If I add %d, %d, and %d I get %d." Inserting age, my_height, my_weight. And Summing
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)