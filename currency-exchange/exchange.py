"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """Calculate estimated value after exchange."""
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange."""
    return budget - exchanging_value
    


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of currency at current denomination."""
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculate the number of currency units (bills) within the amount."""
    return amount // denomination 


def get_leftover_of_bills(amount, denomination):
    """Calculate leftover amount after exchanging into bills."""
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the new currency."""
    exchange_rate = exchange_rate * (1 + spread / 100)
    budget = exchange_money(budget, exchange_rate)
    budget = get_number_of_bills(budget, denomination)
    return get_value_of_bills(denomination, budget)
