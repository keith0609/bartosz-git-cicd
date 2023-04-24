class Account:

    def __init__(self, account_type: str):
        self._account_type = account_type
        self._balance = 0

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        if amount > self._balance and self._account_type == 'savings':
            raise ValueError('Cannot overdraw on a savings account')
        self._balance -= amount

    @property
    def balance(self):
        return self._balance


def test_deposit_checking():
    account = Account('checking')
    account.deposit(100)
    assert account.balance == 100


def test_withdraw_checking():
    account = Account('checking')
    account.deposit(100)
    account.withdraw(50)
    assert account.balance == 50


def test_overdraw_checking():
    account = Account('checking')
    account.deposit(50)
    account.withdraw(100)
    assert account.balance == -50


def test_overdraw_savings():
    account = Account('savings')
    account.deposit(50)
    account.withdraw(100)
    assert account.balance == -50
