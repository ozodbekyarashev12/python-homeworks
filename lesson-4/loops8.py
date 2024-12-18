print("Prime numbers between 1 and 100:")

for num in range(2, 101):  # Start from 2 since 1 is not a prime number
    is_prime = True  # Assume the number is prime
    for divisor in range(2, int(num**0.5) + 1):  # Check divisors up to the square root of the number
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
