#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def displayInventory(args):
	inv = 0
	for k,v in args.items():
		print(str(v) + ':' + k)
		inv += v
	print('Total numbers of items: ' + str(inv))
	
def addToInv (args, additems):
	for i in additems:
		args.setdefault(i, 0)
		args[i] += 1
	return args
	
the_adv_kit = {'rope': 2, 'sword': 1, 'golden coin': 42, 'silver coin': 110}
dragonLoot = ['sword', 'kristall', 'ruby', 'golden coin', 'golden coin', 'golden coin', 'golden coin',
				'golden coin', 'silver coin', 'silver coin', 'silver coin', 'silver coin', 'sword', 'sword', 'sword', 'sword', 
				'kristall', 'ruby','ruby','ruby','ruby', 'copper coin', 'copper coin', 'copper coin', 'copper coin']


if __name__ == '__main__':
	displayInventory(the_adv_kit)
	the_adv_kit = addToInv(the_adv_kit, dragonLoot)
	displayInventory(the_adv_kit)

	
	
