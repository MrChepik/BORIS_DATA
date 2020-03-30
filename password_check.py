#!/usr/bin/env python3
# -*- coding: utf-8 -*-




def password_check():
	
	min_lenghth = 8
	
	if len(password) < min_lenghth:
		print('Password is too short')
		return False
	elif username in password:
		print('Password contain Username')
		return False
	else:
		print(f'Password for {username} is correct')
		return True
		


username = input('Enter your name:  ')
password = input('Enter your password:  ')

password_check()
