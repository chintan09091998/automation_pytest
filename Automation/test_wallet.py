from Wallet import Wallet,InsufficientAmount
import pytest

def test_initial_amount():
    wallet=Wallet()
    assert wallet.balance==0

def test_spend_cash_amount():
    wallet=Wallet(100)
    wallet.spend_cash(50)
    assert wallet.balance == 50
    
def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100
    
def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
    
    
