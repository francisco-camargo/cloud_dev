# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:23:04 2021

@author: camar
"""

# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

import sys
if '..' not in sys.path:
    sys.path.append('..')

from src import main

import pytest

def test_capital_case():
    assert main.capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        main.capital_case(9)
        
if __name__ == '__main__':
    pytest.main()