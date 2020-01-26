#!/usr/bin/env python3

from sys import stdin

current_word = None
current_count = 0
word = None

for line in stdin:
    line.strip()

    # parse input from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number so ignore this line
        continue

    # this works because all data was sorted first
    if current_word:
        print(f"{current_word}\t{current_count}")
    current_word = word
    current_count = count

# print last word
if current_word == word:
    print(f"{current_word}\t{current_count}")
