#!/usr/bin/python3
"""Making Change Problem 0-making_change.py
"""


def makeChange(coins, total):
    """
    This function generates the minimum number of coins required to make change
    for a given total.

    Args:
        coins (list): List of available coins.
        total (int): Total amount.

    Returns:
        int: Minimum number of coins required to make change.
        -1: if change is not possible.
    """

    # If the total is not valid, return -1
    if total <= 0:
        return -1

    # If the total is valid, sort the coins in descending
    # order, and count the number of coins required to make
    # change.
    new_list = sorted(coins[:], reverse=True)
    count = 0
    value = total
    index = 0

    # Loop through the list of coins, and for each coin,
    # check if the value of the coin is less than the total.
    # If it is, subtract the value of the coin from the
    # total, and increment the count.
    while value > 0 and index < len(new_list):
        if value >= new_list[index]:
            value = value - new_list[index]
            count += 1
        # If the value of the coin is greater than the
        # total, move to the next coin in the list.
        elif value < new_list[index]:
            index += 1

    # If the index is equal to the length of the list,
    # and the value is not equal to zero, it means that
    # the total cannot be made with the available coins.
    # Therefore, return -1.
    if index == len(new_list):
        if value != 0:
            return -1
    return count