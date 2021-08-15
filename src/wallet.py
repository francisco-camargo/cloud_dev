# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:10:48 2021

@author: camar
"""

# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount