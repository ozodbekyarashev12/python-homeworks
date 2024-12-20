def is_prime(n):
    """
    Determines if a number is a prime number.

    Parameters:
        n (int): A positive integer greater than 0.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):  # Check divisors up to the square root of n
        if n % i == 0:
            return False
    return True