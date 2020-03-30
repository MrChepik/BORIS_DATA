#1/usr/bin/env python3
# -*- coding: utf-8 -*-  

ip_addr = input('Please enter an IP address: ')

octets = ip_addr.split('.')

print(octets)

print('{:^15}{:^15}{:^15}{:^15}'.format('octet_1', 'octet_2', 'octet_3', 'octet_4'))

print('-'*60)

print('{:^15}{:^15}{:^15}{:^15}'.format(*octets))
print('{:^15}{:^15}{:^15}{:^15}'.format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))
print('{:^15}{:^15}{:^15}{:^15}'.format(hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))
print('-'* 60)
