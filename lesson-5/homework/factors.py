

def factor():
    # Prompt the user to enter a positive integer
    num = int(input("Enter a positive integer: "))
    
    # Check for factors and print them
    for i in range(1, num + 1):
        if num % i == 0:
            print(f"{i} is a factor of {num}")

if __name__ == "__factor__":
    factor()
