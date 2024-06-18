#!/usr/bin/python3
""" Prime Game """


def generatePrimeNumbers(limit):
    """
    Generate list of primes up to limit

    Args:
        limit (int): The upper limit of the range of numbers to che

    Returns:
        list: A list of prime numbers up to the given limit
    """
    # Initialize empty list to store prime numbers
    primes = []
    # Create a boolean list where each index corresponds
    # to a number from 2 to limit + 1
    sieveList = [True] * (limit + 1)

    # Iterate through potential prime numbers from 2 to limit + 1
    for potentialPrime in range(2, limit + 1):
        # If the number is considered prime according to the sieve list
        if sieveList[potentialPrime]:
            # Add the number to the list of prime numbers
            primes.append(potentialPrime)
            # Mark all multiples of the number in the sieve list as non-prime
            for multiple in range(potentialPrime, limit + 1, potentialPrime):
                sieveList[multiple] = False

    # Return the list of prime numbers
    return primes


def isWinner(numRounds, roundValues):
    """
    Determine the winner of the game.

    Args:
        numRounds (int): The number of rounds in the game.
        roundValues (list): The list of number of prime
        numbers to generate in each round.

    Returns:
        str: The name of the winner or None if no winner.
    """
    # Check if the game has at least one round and round values.
    if not numRounds or not roundValues:
        return None

    # Initialize scores for Maria and Ben.
    maria_score = ben_score = 0

    # Iterate through each round.
    for i in range(numRounds):
        # Generate prime numbers for the round.
        primes = generatePrimeNumbers(roundValues[i])

        # Check if the number of prime numbers is even or odd.
        if len(primes) % 2 == 0:
            # If even, increment Ben's score.
            ben_score += 1
        else:
            # If odd, increment Maria's score.
            maria_score += 1

    # Determine the winner based on the scores.
    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"

    # If no winner, return None.
    return None