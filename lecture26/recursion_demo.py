# Create 2 recursive functions

def recursiveCount(n):
    """ Loop for n iterations using recursion.

    Args:
        n (int): The number of iterations to loop for

    Returns:
        int: The number of iterations elapsed (n)

    """

    if n > 0: # Base case is n == 0
        return 1 + recursiveCount(n-1) # Recursive call
    else:
        return 0 # Base case

def factorial(n):
    """ Calculate n! using recursion.

    n! = n * (n-1) * (n-1) * ... * 3 * 2 * 1
       = n * (n-1)!

    Args:
        n (int): The positive integer to calculate n! for

    Returns:
        int: The value n!

    """

    if n > 1: # Base case is when n == 1
        return n * factorial(n-1) # Recursive call
    else:
        return 1 # Base case
