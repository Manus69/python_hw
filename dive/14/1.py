import pytest 

class Account:
    def __init__(self, balance=0):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0: raise ValueError()

        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance: raise ValueError()

    def get_balance(self):
        return self.balance
    
_B = 100
@pytest.fixture
def account():
    return Account(_B)

def test_balance(account):
    assert account.get_balance() == _B

def test_deposit(account):
    account.deposit(50)
    assert account.get_balance() == _B + 50

def test_ifnd(account):
    with pytest.raises(ValueError):
        account.withdraw(2 * _B)

def test_nf(account):
    with pytest.raises(ValueError):
        account.deposit(- _B)

