# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture()
def empty_wallet():
    """Returns a Wallet instance with zero balance"""
    return Wallet()


@pytest.fixture()
def wallet(empty_wallet):
    """Returns a Wallet with a balnce of 20"""
    return Wallet(20)


# def test_default_initial_amount():
#    wallet = Wallet()
#    assert wallet.balance == 0

def test_empty_wallet(empty_wallet):
    assert empty_wallet.balance == 0


# def test_setting_initial_amount():
#    wallet = Wallet(100)
#    assert wallet.balance == 100

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    # wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    # wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)


# test paremeterizations ...
@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
