#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from getpass import getpass
import netmiko
import time
from concurrent.futures import ThreadPoolExecutor
import logging
from itertools import repeat
import yaml





# tftp_server = '192.168.1.12'
# tftp_folder = 'TFTP-FTP'
# tftp_filename = 'sw2_new_backup'

logging.getLogger('paramiko').setLevel(logging.WARNING)
logging.basicConfig(level = logging.INFO)

def device_backup(devices, command):
	logging.info(f'Connect to: {devices["ip"]}')
	
	with netmiko.ConnectHandler(**devices) as ssh:
		ssh.enable()
		return ssh.send_command(command)
		
	
if __name__ == '__main__':
	with open('devices.yaml') as f:
		devices = yaml.safe_load(f)
		
	with ThreadPoolExecutor(max_workers=5) as executor:
		result = executor.map(device_backup, devices, repeat('sh clock'))
		for device, output in zip(devices, result):
			print(device['ip'], output)
			
	with open('parse_result.txt', 'a') as f:
		data = f.write(output)
		


