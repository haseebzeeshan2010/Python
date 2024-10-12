import re

text = "Sample text, 199.99"
pattern = r"\d"

match = re.search(pattern, text)

findall = re.findall(pattern,text)

if match:
    print("match found")
else:
    print("no match found")

print(findall)