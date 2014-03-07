#!/usr/bin/env python

import string

def sandwich(before,after,s):
    front = s.find(before) + len(before)
    s = s[front:]
    back = s.find(after)
    return s[:back]
