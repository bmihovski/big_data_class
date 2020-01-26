#!/usr/bin/env python3

from sys import stdin
from json import loads

for line in stdin:
    line = line.strip()
    j = loads(line)
    print(f"{j['user_id']}\t{line}")
