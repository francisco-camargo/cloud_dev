# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:09:44 2021

@author: camar
"""

import sys
if '..' not in sys.path:
    sys.path.append('..')

from src import wallet

# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# combine pytest fixtures and parametrized test functions
import pytest

@pytest.fixture
def my_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return wallet.Wallet()

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20,  2, 18),
    (100, 2, 98),
    (400, 0,400)
])
def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
        
if __name__ == '__main__':
    pytest.main()