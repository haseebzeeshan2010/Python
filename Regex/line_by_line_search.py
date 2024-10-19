import re

with open("sample.txt", "r") as f:
    for line in f:
        match = re.search("sample", line)
        if match:
            print("Found a match in line:", line)
            break