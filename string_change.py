#!/usr/bin/env python3
#-*-coding:utf-8-*-

import re
from pprint import pprint
import os

file = input('Please enter filename: ')
 
def output_change(file): 
	with open(file) as f: 
		output = f.read() 
    output1 = re.compile(r'Ethernet') 
    output = output1.sub(r'FastEthernet', output) 
    with open(file, 'w') as g: 
		g.write(output) 
    ...:                           

print(output_change(file))
