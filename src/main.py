# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:23:04 2021

@author: camar
"""


def my_string():
    return 'foo'


def my_sum(a,b):
    return a + b


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()


def main():
    print('Hello World.')
    x = 'a'
    y = 'b'


if __name__ == "__main__":
    main()