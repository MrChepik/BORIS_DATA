#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''

command = 'sh ip int br'

import getpass
import textfsm
from netmiko import ConnectHandler

user = input('Username: ')
password = getpass.getpass()


device_ip = ['157.230.176.111']

def connect_to_device(device_ip, command):
	for ip in device_ip:
		print('Connect to device: {}'.format(ip))
		device_params = {
				'device_type':'linux',
				'ip':ip,
				'username':user,
				'password':password
				}
		with ConnectHandler(**device_params) as ssh:
			ssh.enable()
			
			parse_result = ssh.send_command(command)
	return parse_result
			
if __name__ == '__main__':
	command = 'apt update'
	parse_result = connect_to_device(device_ip, command)
	print(parse_result)

