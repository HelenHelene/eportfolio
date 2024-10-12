# Jupyter Notebook Activity - pytest

## Introduction
The following task involves experimenting with pytest using the Python programming language. <br> 
<br>

### _wallet.py_
```python
# code source: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# wallet.py

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
```

<br>

### _test_wallet.py_
```python
# code source: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
```

<br>

### First Run the tests without amend the code
<img src="SEPM_Unit06_Output1.jpg" alt="output" width="700"/>

<br>

---

### Amend the code in _wallet.py_ so that the test fail. <br>
```python
# code source: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# wallet.py

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
        self.balance -= amount  # change the add_cash method from "self.balance += amount" to cause a test to fail
```

<br>

### Second Run the tests with amended code <br>
<img src="SEPM_Unit06_Output2.jpg" alt="output" width="900"/>

<br>

## Reflections
Reflecting on the Jupyter Notebook activity with pytest, I've learned the importance of testing in software development and how it ensures code reliability. Experimenting with pytest demonstrated how simple assertions can effectively validate code functionality. By intentionally causing tests to fail, I gained insight into how errors are detected and resolved, reinforcing the significance of test-driven development. This understanding will be invaluable for future coding assignments, where writing tests alongside code will help catch bugs early and maintain high-quality software.
<br><br>

---

## Reference
Gathuku, K. (2024) Testing Python Applications with Pytest. Available from: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

Jupter. (N.D.) Try Jupyter. Available from: https://jupyter.org/try

<br><br>

---

[Return to Module 5 Unit 6](SEPM_Unit06.md)
