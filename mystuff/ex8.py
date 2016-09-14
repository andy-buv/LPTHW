# Assigns formatter with 'raw data' values
formatter = "%r %r %r %r"

# Prints 1 2 3 4
print formatter % (1,2,3,4)
# Prints one two three four
print formatter % ("one", "two", "three", "four") # forgot to put " after "four
# Prints True False False True
print formatter % (True, False, False, True)
# Prints '%r %r %r %r' four times
print formatter % (formatter, formatter, formatter, formatter)
# Prints strings on one line .'
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
