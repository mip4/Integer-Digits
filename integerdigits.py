#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 03:13:31 2017

@author: mip
"""

x = int(input('enter a positive integer: '))
if x<10:
    print('')
    print('this is a one digit integer')
elif x<100:
    print('')
    print('this is a two digit integer')
else:
    print('')
    print('this is a big integer!')