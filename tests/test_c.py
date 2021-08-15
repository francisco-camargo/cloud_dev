# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:23:04 2021

@author: camar
"""

import pytest

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
    
if __name__ == '__main__':
    pytest.main()