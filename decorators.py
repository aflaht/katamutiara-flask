# -*- coding: utf-8 -*-
"""
Created on Friday 12/10/2021, 3:14:46 PM

@author: Aflah
"""


def check(func):
    def inside(a, b):
        if b == 0:
            print("Can't divide by 0")
            return
        func(a, b)
    return inside


@check
def div(a, b):
    return a / b


print(div(10, 0))
