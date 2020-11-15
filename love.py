# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# print('\n'.join([''.join([('Love'[(x-y) % len('Love')]if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')for x in range(-30, 30)])for y in range(30, -30, -1)]))
import time
words = input('Please input the words you want to say!:')
for item in words.split():
    print('\n'.join([''.join([(item[(x-y) % len(item)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(12, -12, -1)]))
    print('\t\t\t\t\t\t')
    time.sleep(1.5)