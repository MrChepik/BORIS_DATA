#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import yaml




birthdays = {}
		


# with open('birthday_list.yaml') as f:
	# birthdays = yaml.safe_load(f)
	
		
			
def birthday_list(args):
	
	while True:
		print('Enter a name (or press any key to quit)')
		name = input()
		if name == '':
			break
		elif name in args:
			print(args[name] + 'The date of birth is: ' + name)
		else:
			print("I don`t have date of birth for: " + name + ' in database')
			print('What is a date of birth? - ' + name)
			bday = input()
			args[name] = bday
			print('Birthday_list database is updated!')

def write_to_file(filename, args):
	with open(filename, 'a') as f:
		yaml.dump(args, f)
		


if __name__ == '__main__':
	birthday_list(birthdays)
	write_to_file('birthday_list.yaml', birthdays)
	
		
