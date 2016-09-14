tabby_cat = "\tI'm tabbed in." #\t tabs
persian_cat = "I'm split\non a line." #\n new line
backslash_cat = "I'm \\ a \\ cat." #\\ \backslash

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s" % i,
		
		# %r is debugging %s is displaying