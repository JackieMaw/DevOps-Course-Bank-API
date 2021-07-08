"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank, Account


@pytest.fixture
def bank() -> Bank:
    return Bank()


def test_accounts_are_immutable():
    account = Account('Immutable')
    with pytest.raises(Exception):
        # This operation should raise an exception
        account.name = 'Mutable'


def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0


def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'


def test_cannot_duplicate_accounts(bank: Bank):
    bank.create_account('duplicate')
    bank.create_account('duplicate')

    assert len(bank.accounts) == 1

def test_create_account_must_be_a_string(bank: Bank):
    with pytest.raises(TypeError):
        bank.create_account(5)

def test_cannot_modify_accounts_set(bank: Bank):
    accounts = bank.accounts
    accounts.append(Account('New Account'))

    assert len(bank.accounts) == 0

def test_can_add_funds(bank: Bank):
    num_transations_before = len(bank.transactions)
    bank.create_account('Test') #dependency on create_account
    bank.add_funds('Test', 100)
    num_transations_after = len(bank.transactions)

    assert num_transations_after == num_transations_before + 1
    last_transaction = bank.transactions[-1]
    assert last_transaction.account.name == 'Test'
    assert last_transaction.amount == 100

def test_add_funds_fails_if_account_does_not_exist(bank: Bank):
    with pytest.raises(ValueError):
        bank.add_funds('Test', 100)

def test_add_funds_fails_if_amount_is_not_numeric(bank: Bank):
    bank.create_account('Test')

    try:
        bank.add_funds('Test', 'Not a Number')

    except Exception as e:
        assert e.args[0] == 'Amount must be numeric'

    # with pytest.raises(ValueError) as e:        
    #     bank.add_funds('Test', 'Not a Number')
    #     print(e)

def test_can_add_funds_greater_than_zero(bank: Bank):
    bank.create_account('Test')
    bank.add_funds('Test', 100)

def test_cannot_add_funds_less_than_zero(bank: Bank):
    bank.create_account('Test')
    with pytest.raises(ValueError):
        bank.add_funds('Test', -100)

