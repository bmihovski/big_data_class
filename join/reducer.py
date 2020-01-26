#!/usr/bin/env python3

from sys import stdin
from json import loads

def print_user(j):
    if 'user_id' not in j:
        return
    print(f"{j['user_id']}\t{j.get('name', '')}\t{j.get('fruit', '')}")

current_user_id = None
current_data = {}

for line in stdin:
    line = line.strip()

    user_id, j = line.split("\t", 1)

    if current_user_id != user_id:
        # print data for current user and reset
        print_user(current_data)
        current_data = {}
        current_user_id = user_id
        j = loads(j)
        for k, v in j.items():
            current_data[k] = v

# print the last user
print_user(current_data)
