#!/usr/bin/env python3
#-*-decode: utf-8 -*-

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

#Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:
#
#             IP ADDR          MAC ADDRESS
#-------------------- --------------------
#        10.220.88.29       5254.abbe.5b7b
#        10.220.88.30       5254.ab71.e119
#        10.220.88.32       5254.abc7.26aa
#
#
#Two columns, 20 characters wide, data right aligned, a header column.

fields1 = mac1.split()
ip_addr1 = fields1[1]
mac1 = fields1[3]

fields2 = mac2.split()
ip_addr2 = fields2[1]
mac2 = fields2[3]

fields3 = mac3.split()
ip_addr3 = fields3[1]
mac3 = fields3[3]

print('{:>20}{:>20}'.format('IP-Address', 'MAC-Address'))
print('-'*70)
print('{:>20}{:>20}'.format(ip_addr1, mac1))
print('{:>20}{:>20}'.format(ip_addr2, mac2))
print('{:>20}{:>20}'.format(ip_addr3, mac3))
