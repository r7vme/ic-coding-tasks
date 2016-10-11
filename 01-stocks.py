#!/usr/bin/python2


def get_max_profit(prices):
    # Get max price, excluding initial price
    max_price = max(prices[1:])

    # Get index of max price.
    # If multiple equal values, use one on the right.
    max_price_i_reverted = prices[::-1].index(max_price)
    max_price_i = (len(prices)-1) - max_price_i_reverted

    # Get min price that was before last peak (max price).
    min_price = min(prices[:max_price_i])
    return (max_price - min_price)


if __name__ == "__main__":
    stock_prices_yesterday = [11, 10, 9, 8, 7, 3]
    print get_max_profit(stock_prices_yesterday)
