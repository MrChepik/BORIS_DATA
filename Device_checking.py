#!/usr/bin/env python3
#-*-decode: utf-8 -*-

show_version = '*0    CISCO881-SEC-K9    FTX000038X'
show_version = show_version.strip()
fields = show_version.split()
model = fields[1]
serial_number = fields[2]

vendor = 'cisco' in model.lower()
model_881 = '881' in model

print('Checking, if model contains cisco: {}'.format(vendor))
print('Checking, if model contains 881: {}'.format(model_881))

print('Device model: {}'.format(model))
print('Device serial number: {}'.format(serial_number))
