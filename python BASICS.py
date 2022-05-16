# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# split word
x = 5
y = 4
print(x+y)


#### python workshop

# input
user_input = input('enter a value: ')

# exercise: paint cost of circular walls
print('Please enter the radius in metre: ')
paint_input = input()
paint_input = int(paint_input)
a = (paint_input**paint_input*3.14/10)*15
print(a)

# if statement
if x>y:
    print('x is greater than y') #if - elif - else
    
# logical operators

# loop statement***

# while, continue (in R called 'next' ???)

# exercise: leap year
# solution 1
year = input()
year = float(year)
if isinstance(year / 4, str) == True:
    if isinstance(year / 100, str) == True:
        print(year, 'is a leap year')
    elif isinstance(year / 100, str) == False:
        print(year, 'is not a leap year')
elif isinstance(year / 100, str) == False:
    print(year, 'is not a leap year')
    
# solution 2
# % shows remainder of a calculation 
for year in range(2000, 2010):
    if year%4==0 and year%100!=0 or year%400==0:
        print(year, 'is a leap year')
    else:
        print(year, 'is not a leap year')
        
# solution 3
year = int(2000)
while year < 2101:
    if year%4==0 and year%100!=0 or year%400==0:
        print(year, 'is a leap year')
        year = year + 1
    else:
        year = year + 1  # how to add break?

# Python Data Types
# fewer data types than those in R
# sequence data: [list], tuple, 
ls = list((1, 2, 3, 4)) #sequence to list #(1,2,3,4) is a sequence
# 0-indexed / index must be integers / allows to count backwards
len()
ls2 = list(range(1, 11, 2))
ls3 = list(range(0, -11, 2))
1 in ls2
1 not in ls2
ls22 = ls2 * 2
del ls2[0]
del ls2[1:2]
del ls2['3'] #couldn't delet a specific item  #find the index of it first

# append
# libraries
import pandas as pd
sort() 
ls2.sort
# lists are comparable

# Tuple: immutable lists
# more efficient because no need to change/update the sequence
tuple1 = ('a',)
tuple2 = tuple(('a',))
# 'modify' a tuple
tuple3 = (('5','10','15'))
tuple4 = tuple(('1',)) + tuple3[1:3]
for (i, j) in [(1,2), (3,4)]:
# tuple has 'no methods'

# String (also immutable)
# supports 'methods'
value = ls #share one memory
value = list(ls) #deep copy
