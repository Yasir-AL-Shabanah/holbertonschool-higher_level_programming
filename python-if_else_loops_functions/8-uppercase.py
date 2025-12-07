#!/usr/bin/python3
def uppercase(str):
    res = ""
    for ch in str:                  # حلقة واحدة فقط
        if 97 <= ord(ch) <= 122:    # a..z
            res += chr(ord(ch) - 32)
        else:
            res += ch
    print("{:s}".format(res))       # استخدام string format كما يطلب المصحح
