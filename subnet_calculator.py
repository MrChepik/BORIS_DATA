#!/usr/bin/env python3
#-*-coding:'utf-8'-*-

import random
import sys

def subnet_calc():
	
	try:
		while True:
			#input ip address as IP-address
			input_ip = input('\nEnter your IP-address:  ')
			
			
			#validate ip-address
			octet_ip = input_ip.split('.')
			for i in octet_ip:
				int_octet_ip = int(i)
			
			if (len(int_octet_ip) == 4) and \
					(int_octet_ip[0] != 127) and \
					(int_octet_ip[0] != 169) and  \
					(0 <= int_octet_ip[1] <= 255) and \
					(0 <= int_octet_ip[2] <= 255) and \
					(0 <= int_octet_ip[3] <= 255):
				break
			
			else:
				print('Invalid IP, try again \n')
				continue
				
			#Predefine possible subnet masks
			masks =[0/ 128, 192, 224, 240, 248, 252, 254, 255]
			while True:
				#Take subnet mask as input
				input_subnet = input('\nEnter your subnet mask:  ')
				
				#Validate the subnet mask
				for m in input_subnet.split('.'):
					octet_subnet = int(m)
					print(octet_subnet)
				if (len(octet_subnet) == 4) and \
						(octet_subnet[0] == 255) and \
						(octet_subnet[1] in masks) and \
						(octet_subnet[2] in masks) and \
						(octet_subnet[3] in masks) and \
						(octet_subnet[0] >= octet_subnet[1] >= octet_subnet[2] >= octet_subnet[3]):
					break
				else:
					print('Invalid subnet mask. Try again. \n')
					continue
		     #Converting IP and masks to binary
		     
			ip_in_binary = []
		     #Convert each IP octet into binary
		     
			for i in int_octet_ip:
				ip_in_bin_octet = bin(i).split('b')[1]
			 
			 #make each bin octet of 8 bit by padding zeros
			 
			for i in range(0, len(ip_in_bin_octet)):
				if len(ip_in_bin_octet[i]) < 8:
					padded_bin = ip_in_bin_octet[i].zfill(8)
					ip_in_binary.append(padded_bin)
				else:
					ip_in_binary.append(ip_in_bin_octet[i])
			#join the binary octets
			ip_bin_mask = "".join(ip_in_binary)
			
			print(ip_bin_mask)
			
			sub_in_bin = []
			
			#convert each subnet octet to binary
			for i in octet_subnet:
				sub_bin_octet = bin(i).split('b')[1]
				
			#make each bin octet of 8 bit by padding zeros
			for i in sub_bin_octet:
				if len(i) < 8:
					sub_padded = i.zfill(8)
					sub_in_bin.append(sub_padded)
				else:
					sub_in_bin.append(i)
			sub_bin_mask = "".join(sub_in_bin)
			
			#calculating numbers of hosts
			no_zeros = sub_bin_mask.count('0')
			no_ones = 32 - no_zeros
			no_hosts = abs(2 ** no_zeros - 2)
			
			#calculating wildcard mask
			wild_mask = []
			for i in octet_subnet:
				wild_bit = 255 -i
				wild_mask.append(wild_bit)
			for i in wilf_mask:
				wildcard = ".".join(str(i))
				
			#calculating the network and broadcast address
			network_add_bin = ip_bin_mask[:no_ones] + '0' * no_zeros
			broadcast_add_bin = ip_bin_mask[:no_ones] + '1' * no_zeros
			
			network_add_bin_octet= []
			broadcast_bin_octet = []
			
			[network_add_bin_octet.append(i) for i in [network_add_bin[j:j+8]
                                                   for j in range(0, len(network_add_bin), 8)]]
		[broadcast_bin_octet.append(i) for i in [broadcast_add_bin[j:j+8]
                                              for j in range(0,len(broadcast_add_bin),8)]]

		network_add_dec_final = ".".join([str(int(i,2)) for i in network_add_bin_octet])
		broadcast_add_dec_final = ".".join([str(int(i,2)) for i in broadcast_bin_octet])

        # Calculate the host IP range
		first_ip_host = network_add_bin_octet[0:3] + [(bin(int(network_add_bin_octet[3],2)+1).split("b")[1].zfill(8))]
		first_ip = ".".join([str(int(i,2)) for i in first_ip_host])

		last_ip_host = broadcast_bin_octet[0:3] + [bin(int(broadcast_bin_octet[3],2) - 1).split("b")[1].zfill(8)]
		last_ip = ".".join([str(int(i,2)) for i in last_ip_host])
        
		print('\nEntered IP-address is:  {}'.format(input_ip))
		print('\nEntered subnet mask is: {}'.format(input_subnet))
		print('\Calculated number of hosts per subnet is: {}'.format(str(no_hosts)))
		print('\nCalculated numbers of masks bits is: {}'.format(str(no_ones)))
		print('\nCalculated Wildcard mask is: {}'.format(wildcard))
		print('\nThe Network address is: {}'.format(network_add_dec_final))
		print('\nThe Broadcast address is: {}'.format(broadcast_add_dec_final))
		print('\nIP-address range is: {0} - {1}'.format(first_ip, last_ip))
		print('\nMaximum numbers of subnets is: {}'.format(str(2**abs(24 - no_ones))))
		#list_ip = []
	except KeyboardInterrupt:
		print('Interrupted by the User, exiting')
	except ValueError:
		print('Seem to have entered an incorrect value, exiting')


if __name__ == '__main__':
	subnet_calc()
	
		 
        
        
     
