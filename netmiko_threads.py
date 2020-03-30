#!/usr/bin/env python3
#-*- coding:utf-8-*-

import netmiko
import yaml
from concurrent.futures import ThreadPoolExecutor
import logging
from itertools import repeat

logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
        level=logging.INFO)

def send_show(device, command):
    logging.info(f'Connect to {device["ip"]}')
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        return ssh.send_command(command)

with open('devices.yaml') as f:
	devices = yaml.safe_load(f)


with ThreadPoolExecutor(max_workers=3) as executor:
#    result = executor.map(send_show, devices, ['sh clock']*len(devices))
    
    result = executor.map(send_show, devices, repeat('sh clock'))
    for device, output in zip(devices, result):
        print(device['ip'], output)

