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

import pytest

# Pytest Fixtures
@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return wallet.Wallet()

@pytest.fixture
def not_empty_wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return wallet.Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(not_empty_wallet):
    assert not_empty_wallet.balance == 20

def test_wallet_add_cash(not_empty_wallet):
    not_empty_wallet.add_cash(80)
    assert not_empty_wallet.balance == 100

def test_wallet_spend_cash(not_empty_wallet):
    not_empty_wallet.spend_cash(10)
    assert not_empty_wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(wallet.InsufficientAmount):
        empty_wallet.spend_cash(100)


# Parametrized test functions
@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20,  2, 18),
    (100, 2, 98),
    (400, 0,400)
])
def test_transactions(earned, spent, expected):
    my_wallet = wallet.Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
        
if __name__ == '__main__':
    pytest.main()