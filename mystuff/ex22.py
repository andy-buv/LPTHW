^ : caret character
.py : to save file a python file
""" : block comment : can also be used to print block text """
print : outputs code !Python 2
print() : same as above but is a function in Python3!
#  : single line comment
+ : concatenates strings
"string example" : enclose strings with " " (double quotes) or ' ' (single quotes). 
_ : underscore character

PEMDAS aka BODMAS : Paranthesis, Exponents, Multiplication, Division, Addition, Subtraction.
, : when outputing multiple instances
+ : addition
/ : division 
* : multiplication
% : modulo
- : subtraction
1 : integer representation of 1
1.0 : floating point representation of 1
< : is less than conditional
<= : is less than or equal conditional
> : is greater than conditional
>= : is greater than or equal conditional
== : is equal to conditional

True : boolean value
False : boolean value

= : assign variable
%s : format string
%d : format digit
%r : format raw
% (variable_one, variable_two) : 

, : use comma to keep code on the same line

round() : rounds floating numbers
\n : ASCII linefeed (LF)
\ : escape character
\t : Horizontal Tab (TAB)
\\ : backslash
\' : Single-quote (')
\" : Double-quote (")
\a : ASCII bell (BEL)
\b : ASCII backspace (BS)
\f : ASCII formfeed (FF)
\N{name} : Character named name in the Unicode database (Unicode only)
\r : Carriage Return (CR)
\uxxxx : Character with 16-bit hex value (Unicode only)
\Uxxxxxxxx : Character with 32-bit hex value xxxxxxxx (Unicode only)
\v : ASCII vertical tab (VT)
\ooo : Character with octal value ooo
\xhh : Character with hex value hh

raw_input([prompt]) : allows user input with a customizable prompt ! Python 2
input([prompt]) : Python 3
u'35' : unicode 35
pydoc : for quick documentation on Python from terminal. Note not within Python

import : used for importing modules e.g. import math
from sys import argv : imports argument value moduel from the 'sys' package. All arguments are imported as strings
script, user_name = argv : assigns variables 'script' and 'user_name' with incoming arguments

txt = open(filename) : Assigns 'txt' with the opened file object
text.read() : reads content of file object
text.close() : closes the file object, it is import to do this.
text.readline() : reads just one line of a text file
text.truncate() : empties the file.
text.write('stuff') : writes "stuff" to the file

CTRL-C (^C) : hitting CTRL-C within Python will terminate the program. Aka Keyboard Interrupt
open(filename, 'w') : open takes different parameters depending on what you want to do with it,
'w', 'w+', 'r+', 'a', 'a+'.

In the terminal:
	$ echo "this is a test file." > test.txt : writes "this is a test file." to the file test.txt
	$ cat test.txt : displays contents of test.txt in terminal
	$ man cat : opens manual for terminal on page for cat : concatentates and print files

len() : returns the length of a string
def : keyword to 'define' a function in Python
def say_my_name(argument): : an example of a function defined with parameter argument
def some_function(*args): : *args takes multiple arguments and stores them in a list

file.seek(0) : moves to new file position
+= : is an augmented assignment that will evaluate and add to a variable

return : set variables to be a value from a function

