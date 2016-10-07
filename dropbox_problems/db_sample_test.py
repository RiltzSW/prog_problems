#!/bin/python

import sys
import os
import itertools

# note this is an array of strings like
# ["12", "21"]
# answer ["1112", "1211"]
def say_what_you_see(input_strings):
    output_strings = []
    for num_string in input_strings:
        x = [[len(list(a)), b] for b , a in itertools.groupby(num_string)]
        result = ''
        for y in x:
            result += str(y[0]) + str(y[1])
        output_strings.append(result)
    return output_strings

x = ['1211', '21']
print(say_what_you_see(x))
