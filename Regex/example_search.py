import re

text = "Lorem ipsum odor amet, consectetuer adipiscing elit. 0, 1,sd"
pattern = r"\d"

match = re.search(pattern, text) # returns true or false

findall = re.findall(pattern,text) # returns all instances as an array

subn = re.subn(r'\b\w{4}\b', '****', text) # returns substituted string and number of replaced parts

split = re.split(pattern, text) # returns split string at every occurance of the pattern

split3 = re.split(pattern, text, 3) # returns split string at every occurance of the pattern but only 3 times


#Compiling a regex function so it is more efficient if used repeatedly
compileregex = re.compile(pattern)

compilefind = compileregex.findall(text)


if match:
    print("match found")
else:
    print("no match found")

print(findall)
print(subn)
print(split)
print(split3)
print(compilefind)