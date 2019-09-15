#!/usr/bin/env python3
# -*- coding: utf-8 -*-


subnetmask = input('Enter your subnet mask to calculate it  ')

prefix = int(subnetmask)
prefix = '1' * prefix + '0' * (32 - prefix)

mask = []
mask.append(prefix[:8])
mask.append(prefix[8:16])
mask.append(prefix[16:24])
mask.append(prefix[24:32])
mask = [int(m,2) for m in mask]

print('Mask: \n {:<10}{:<10}{:<10}{:<10}'.format(mask[0],mask[1],mask[2],mask[3]))
print('Mask: \n {:08b}{:08b}{:08b}{:08b}'.format(mask[0],mask[1],mask[2],mask[3]))
print('Mask: \n {:02x}{:02x}{:02x}{:02x}'.format(mask[0],mask[1],mask[2],mask[3]))


