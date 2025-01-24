#!/usr/bin/python3
"""Change making
"""


def makeChange(coins, total):
    """main program
    """
    if total <= 0:
        return 0
    mer = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while mer > 0:
        if coin_idx >= n:
            return -1
        if mer - sorted_coins[coin_idx] >= 0:
            mer -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
