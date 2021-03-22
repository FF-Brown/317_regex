# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:12:53 2021

@author: Nathan
"""


import re

lines = ["00:02:07	Prof Name:	I don’t how that happened. I typed morning.",
"00:10:48	Colon in message:	vague: something",
"00:17:44	Student Name:	Sorry I just got back to my desk. What was the warmup question (if there was one)",
"00:18:04	Hyphenated-Name:	What does ambiguous mean to you",
"00:19:09No Initial Whitespace:	uncertain",
"00:30:25	SingleWordName:	a little fast",
"00:38:33	Jane Doe:	same"]

x = 1

for line in lines:
    print(x, ".) ", line, sep="")
    x = x +1
    extracted = re.findall("^[0-9]{2}:[0-9]{2}:[0-9]{2}.*:[\s]*(.*)$", line)
    # Add try-catch here.
    print(extracted[0])
