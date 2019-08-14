# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:31:40 2018

@author: spanier
"""

def shiftL(num, shift):
    N= num[shift:100]
    for i in range(shift):
        N+="0"
    print(N)
    return

def shiftR(num, shift):
    N= num[0:len(num)-shift]
    for i in range(shift):
        N="0"+N
    print(N)
    return

def shiftCR(num, shift):
    N= num[0:len(num)-shift]
    M= num[len(num)-shift:100]
    shifted= M+N
    print(shifted)
    return

def shiftCL(num, shift):
    N= num[shift:100]
    M= num[0:shift]
    shifted= N+M
    print(shifted)
    return