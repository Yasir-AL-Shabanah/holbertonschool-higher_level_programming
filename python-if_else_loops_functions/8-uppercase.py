#!/usr/bin/python3

def uppercase(s):
    res = ""
    for ch in s:
        if 97 <= ord(ch) <= 122:
            res += chr(ord(ch) - 32)
        else:
            res += ch
    print(res)
