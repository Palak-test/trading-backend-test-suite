from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from portfolio.portfolio import Portfolio

scenarios('../features/portfolio.feature')

@given(parsers.parse('a portfolio with ${cash:d} cash'), target_fixture='portfolio')
def portfolio(cash):
    return Portfolio(cash=cash)

@when(parsers.parse('I buy {quantity:d} shares of "{symbol}" at ${price:d} each'))
def buy_shares(portfolio, quantity, symbol, price):
    try:
        portfolio.buy(symbol, quantity, price)
    except Exception as e:
        pytest.exception = e

@when(parsers.parse('I sell {quantity:d} shares of "{symbol}" at ${price:d} each'))
def sell_shares(portfolio, quantity, symbol, price):
    try:
        portfolio.sell(symbol, quantity, price)
    except Exception as e:
        pytest.exception = e

@then(parsers.parse('my portfolio has {quantity:d} shares of "{symbol}"'))
def check_position(portfolio, quantity, symbol):
    assert portfolio.get_position(symbol) == quantity

@then(parsers.parse('my cash balance is ${cash:d}'))
def check_cash(portfolio, cash):
    assert portfolio.get_cash() == cash

@then('an error should be raised')
def error_raised():
    assert hasattr(pytest, 'exception') and pytest.exception is not None
