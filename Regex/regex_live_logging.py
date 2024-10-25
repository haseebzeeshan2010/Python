import re
import time
import random


def get_live_logging_data():
    log_levels = ["INFO", "WARNING", "ERROR"]
    log_level = random.choice(log_levels)
    return f"[{log_level}] This is a sample log message."

def filter_errors(log_line):
    pattern = r"\[(ERROR)]"

    match = re.search(pattern, log_line)
    if match:
        print("Error found:", log_line)


while True:
    line = get_live_logging_data()
    filter_errors(line)
    time.sleep(1)