#!/usr/bim/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        fc = None
    else:
        fc = sentence[0]
    return length, fc
