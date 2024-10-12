import re

text = "Sample text"
pattern = "Sample"

match = re.search(pattern, text)

if match:
    print("match found")
else:
    print("no match found")