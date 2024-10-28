import re

def correct_spelling(text, corrections):
    print("")
    for mispelled, correct in corrections.items():
        pattern = re.compile(rf"\b{mispelled}\b")
        corrected = pattern.sub(correct,text)

    print(corrected)
correction_dict = {
    "yoghurt":"yogurt",
    "sandwhich":"sandwich",

}

raw_text = input("Enter some text to be corrected: ")

correct_spelling(raw_text, correction_dict)