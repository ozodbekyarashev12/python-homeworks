# invest.py

def invest(amount, rate, years):
    """
    Tracks the growth of an investment over time.

    Parameters:
        amount (float): The initial principal amount.
        rate (float): The annual rate of return (e.g., 0.05 for 5%).
        years (int): The number of years to calculate.

    Prints:
        The amount at the end of each year, rounded to 2 decimal places.
    """
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

def main():
    # Get user inputs
    amount = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual rate of return (e.g., 0.05 for 5%): "))
    years = int(input("Enter the number of years: "))
    
    # Call the invest function
    invest(amount, rate, years)

if __name__ == "__main__":
    main()