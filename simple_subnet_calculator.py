#!/usr/bin/env python3
#-*-decode:'utf-8'-*-

IP = input('Please enter your IP-address / subnet mask:  ')
print('*'*60)
IP = IP.split('/')
	
IP_oct = IP[0].split('.')
IP_oct = [int(i) for i in IP_oct] 
print('*'*60)
print('INT') 
print('Network: \n{:^15}{:^15}{:^15}{:^15}'.format(IP_oct[0], IP_oct[1], IP_oct[2], IP_oct[3]))
print('*'*60)
print('BIN')
print('{:^15}{:^15}{:^15}{:^15}'.format(bin(IP_oct[0]), bin(IP_oct[1]), bin(IP_oct[2]), bin(IP_oct[3])))
print('*'*60)
print('HEX')
print('{:^15}{:^15}{:^15}{:^15}'.format(hex(IP_oct[0]), hex(IP_oct[1]), hex(IP_oct[2]), hex(IP_oct[3])))		

prefix = [sum(bin(int(bit)).count('1') for bit in IP[1].split('.'))]
#print(prefix)
mask = IP[1].split('.')
mask = [int(a) for a in mask]
print('*'*60)
print('Subnet calculating')
print('Subnetmask prefix: {} '.format(prefix))
print('*'*60)
print('INT')
print('Subnetmask: \n{:^15}{:^15}{:^15}{:^15}'.format(mask[0], mask[1], mask[2], mask[3]))
print('*'*60)
print('BIN')
print('{:^15}{:^15}{:^15}{:^15}'.format(bin(mask[0]), bin(mask[1]), bin(mask[2]), bin(mask[3])))
print('*'*60)
print('HEX')
print('{:^15}{:^15}{:^15}{:^15}'.format(hex(mask[0]), hex(mask[1]), hex(mask[2]), hex(mask[3])))
 
