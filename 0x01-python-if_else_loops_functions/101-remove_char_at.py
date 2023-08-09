#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    if len(str) == 0:
        return str
    for i in range(len(str)):
        if i != n:
            newstr = newstr + str[i]
    return newstr
            
