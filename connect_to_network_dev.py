#!/usr/bin/env python3
#-*- coding: 'utf-8' -*-

import getpass
import re
from netmiko import ConnectHandler



devices_ip = []
user = input('Username: ')
password = getpass.getpass()
#enable_pass = getpass.getpass(prompt='Enter enable password: ')

#create list of ip-address from file
def ip_list (filename):
	with open(filename) as f:
		for line in f:
			line.rstrip().split()
			result = []
			result.append(line)
			devices_ip = str(result[0])
			devices_ip = devices_ip.split(',')
	return(devices_ip)





#connect to network devices with devices_ip list
def connect_to_network(devices_ip):
	for ip in devices_ip:
		print('Connection to device {}'.format(ip))
		# device_params = {
				# 'device_type': 'cisco_ios',
				# 'ip': ip,
				# 'username': user,
				# 'password': password,
				# 'secret': enable_pass
		# }
		device_params = {
				'device_type': 'cisco_ios',
				'ip': ip,
				'username': user,
				'password': password
		}
		with ConnectHandler(**device_params) as ssh:
			ssh.enable()
			
			parse_result = ssh.send_command('terminal length 0', use_textfsm = True)
			parse_result = ssh.send_command('sh run', use_textfsm = True)
			
		with open('sw2_config', 'a+') as f:
			data = f.write(parse_result)
			
	return parse_result

#write obtained data to file
# def write_to_file(filename):
	# with open(filename, 'w') as f:
		# data = f.write(parse_result)
	# return(data)

if __name__ == '__main__':
	
	devices_ip = ip_list('IP_list.txt')
	parse_result = connect_to_network(devices_ip)
	#result = write_to_file('sh_version.txt')

			
    
	

