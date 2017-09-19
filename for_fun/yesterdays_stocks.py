"""
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:

  stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).

"""
from datetime import datetime, timedelta
# stock_prices_yesterday = [6, 7, 12, 2, 11, 9]
# stock_prices_yesterday = [9, 8, 7, 6, 5, 4]
# stock_prices_yesterday = [1, 2, 3, 4, 5, 6]
#stock_prices_yesterday = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, \
#6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 5, 4, 3,\
# 2, 1,1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1,1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1,1, 2, 3,\
#  4, 5, 6, 5, 4, 3, 2, 1,1, 2, 3, 4, 5, 6, 5, 4, 3, 4, 5, 6, 3, 2, 44, 2, 1]
stock_prices_yesterday = [2, 2, 2, 2, 2]
stock_market_open_hour = 9
stock_market_open_minute = 30


def get_max_profit(stock_prices_yesterday=stock_prices_yesterday, stock_market_open_hour=stock_market_open_hour, stock_market_open_minute=stock_market_open_minute):

    if len(stock_prices_yesterday) < 2:
        raise IndexError('There must be at least two prices listed in stock_prices_yesterday')

    yesterday_date = get_yesterday_market_open_datetime(stock_market_open_hour, stock_market_open_minute)
    buy_stock_price, buy_stock_time = get_buy_price_and_time(stock_prices_yesterday)
    sell_stock_price, sell_stock_time = get_sell_price_and_time(stock_prices_yesterday=stock_prices_yesterday, buy_stock_price=buy_stock_price, buy_stock_time=buy_stock_time)

    buy_stock_time_formatted = get_best_transaction_time(transaction_minute=buy_stock_time, yesterday_date=yesterday_date)
    sell_stock_time_formatted = get_best_transaction_time(transaction_minute=sell_stock_time, yesterday_date=yesterday_date)

    print_results(buy_stock_price=buy_stock_price,
                  buy_stock_time=buy_stock_time_formatted,
                  sell_stock_price=sell_stock_price,
                  sell_stock_time=sell_stock_time_formatted)


def get_best_transaction_time(transaction_minute, yesterday_date):
    best_transaction_time = yesterday_date + timedelta(minutes=transaction_minute)
    return best_transaction_time


def get_yesterday_market_open_datetime(stock_market_open_hour, stock_market_open_minute):
    yesterday_date = (datetime.now() - timedelta(days=1)).replace(
        hour=stock_market_open_hour, minute=stock_market_open_minute, second=0, microsecond=0)
    return yesterday_date


def format_best_transaction_time_for_print(transaction_time):
    hour = transaction_time.hour
    minute = transaction_time.minute
    formatted_transaction_time = '{}:{:02}'.format(hour, minute)
    return formatted_transaction_time


def get_buy_price_and_time(stock_prices_yesterday):
    buy_stock_price = stock_prices_yesterday[0]
    buy_stock_time = 0
    for price in stock_prices_yesterday:
        if buy_stock_price > price:
            buy_stock_price = price
    buy_stock_time = stock_prices_yesterday.index(buy_stock_price)
    return buy_stock_price, buy_stock_time


def get_sell_price_and_time(stock_prices_yesterday, buy_stock_price, buy_stock_time):
    sell_stock_price = buy_stock_price
    sell_stock_time = buy_stock_time
    for price in stock_prices_yesterday[buy_stock_time:]:
        if sell_stock_price < price:
            sell_stock_price = price

    sell_stock_time = stock_prices_yesterday.index(price)
    return sell_stock_price, sell_stock_time


def print_results(buy_stock_price, buy_stock_time, sell_stock_price, sell_stock_time):
    if buy_stock_time == sell_stock_time:
        print("No profit was to be made in stocks.")
    else:
        print('You should have bought stock at: {}'.format(format_best_transaction_time_for_print(buy_stock_time)))
        print('When it was selling for only: ${}'.format(buy_stock_price))
        print('**' * 25)
        print('Then sold it at: {}'.format(
            format_best_transaction_time_for_print(sell_stock_time)))
        print('When it was selling for: ${}'.format(sell_stock_price))


if __name__ == '__main__':
    get_max_profit()
