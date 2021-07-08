from dataclasses import dataclass
from datetime import datetime
from typing import Set, List


@dataclass(frozen=True)
class Account:
    name: str


@dataclass(frozen=True)
class Transaction:
    account: Account
    date: datetime
    amount: int


class Bank:
    def __init__(self):
        self._accounts: Set[Account] = set()
        self._transactions: Set[Transaction] = set()

    @property
    def accounts(self) -> List[Account]:
        """Get a copy of the bank's accounts"""
        return list(self._accounts)

    @property
    def transactions(self) -> List[Transaction]:
        """Get a copy of the bank's transactions"""
        return list(self._transactions)

    def create_account(self, name: str) -> Account:
        """Creates a new account with the name provided"""
        account = Account(name)
        self._accounts.add(account)
        return account

    def get_account(self, name: str) -> Account:
        """Gets the named account, if it exists"""
        for account in self.accounts:
            if account.name == name:
                return account
        raise ValueError('Account not found')

    def add_funds(self, name: str, amount: int) -> None:
        """Add funds to the named account"""
        account = self.get_account(name)
        now = datetime.now()

        if type(amount) != int:
            raise TypeError('Amount must be numeric')            

        if amount <= 0:
            raise ValueError('Amount must be > 0')
            
        self._transactions.add(Transaction(account, now, amount))
