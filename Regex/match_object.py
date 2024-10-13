#Match always has boolean value of true or false

#Has methods to return information about match

#string() returns original string that was provided to be matched

#group() is a method that returns the string that was found

#groups() is a method that returns the tuble to find all groups that were found

#start() returns the starting index of the matched string

#end() returns the ending index of the matched string

#span() returns a tuple containing the starting and ending position of the matched strings within a tuple

import re


pattern = r"(\d{3})-(\d{3}-\d{4})" # Matches phone number in format XXX-XXX-XXXX
text = "My phone number is 575-454-2323"


match = re.search(pattern, text) # returns true or false

if match:
    print(f"Matched phone number: {match.group()}")
    print(f"Area code: {match.group(1)}")
    print(f"Phone number: {match.group(2)}")
    print(f"Start position: {match.start()}")
    print(f"End position: {match.end()}")
else:
    print("no match found")

