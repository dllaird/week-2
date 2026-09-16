import numpy as np


def ways(n, coin_types=[1, 5]):
    """
    Returns the number of ways to make change for n cents using the
    values in coin_types (default is pennies and nickels)
    """
    # Make sure cents is an integer
    n = int(n)

    # Returns zero if n is negative
    if n < 0:
        return 0

    # counts[a] holds the number of ways to make exactly a cents.
    counts = np.zeros(n + 1, dtype=np.int64)

    # there is only one way to make 0 cents (use no coins)
    counts[0] = 1

    # Consider one coin type at a time
    for coin in coin_types:
        for amount in range(coin, n + 1):
            # ways to make amount using this coin = ways to make the leftover
            counts[amount] += counts[amount - coin]

    # returns the number of ways to make exactly n cents
    return int(counts[n])

def lowest_score(names, scores):
    """
    Returns the name of the student with the lowest score
    """
    # converts inputs to numpy arrays
    names = np.asarray(names)
    scores = np.asarray(scores)

    # argmin gives the position of the smallest score
    return names[np.argmin(scores)]


def sort_names(names, scores):
    """
    Returns the names sorted in descending order of their test scores
    """
    # converts inputs to numpy arrays
    names = np.asarray(names)
    scores = np.asarray(scores)

    # sort scores from high to low
    order = np.argsort(scores)[::-1]

    # reorder the names using those positions
    return names[order]
