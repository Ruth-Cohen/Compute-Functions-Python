# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:08:37 2018

@author: spanier
"""

def triangle ():
    a= float(input("enter size for a: "))
    b= float(input("enter size for b: "))
    c= float(input("enter size for c: "))
    if (a+b>c and a+c>b and c+b>a):
        print("they are correct triangle sides lengths")
        return True
    else:
        print("they are in error")
        return False
    
print(triangle())