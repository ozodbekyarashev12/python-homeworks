# Number Data Type Questions

# 1. Round a float to 2 decimal places
num = float(input("Enter a float number: "))
print(f"Rounded number: {round(num, 2)}")

# 2. Largest and smallest of three numbers
nums = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
print(f"Largest: {max(nums)}, Smallest: {min(nums)}")

# 3. Convert kilometers to meters and centimeters
km = float(input("Enter distance in kilometers: "))
print(f"{km} km = {km * 1000} meters, {km * 100000} centimeters")

# 4. Integer division and remainder
num1, num2 = int(input("Enter first number: ")),
int(input("Enter second number: "))
print(f"Quotient: {num1 // num2}, Remainder: {num1 % num2}")

# 5. Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
print(f"{celsius}C = {(celsius * 9/5) + 32}F")

# 6. Last digit of a number
num = int(input("Enter a number: "))
print(f"Last digit: {num % 10}")

# 7. Check if a number is even
num = int(input("Enter a number: "))
print(f"{num} is {'even' if num % 2 == 0 else 'odd'}")

# String Questions

# 1. Name and year of birth to calculate age
name, birth_year = input("Enter your name: "), int(input("Enter year of birth: "))
print(f"Hello {name}, you are {2025 - birth_year} years old.")

# 2. Extract car names
txt = 'LMaasleitbtui'
car_names = [txt[i:i+4] for i in range(0, len(txt), 4)]
print("Extracted car names:", car_names)

# 3. String operations: length, uppercase, lowercase
user_string = input("Enter a string: ")
print(f"Length: {len(user_string)}, Uppercase: {user_string.upper()}, Lowercase: {user_string.lower()}")

# 4. Check if a string is palindrome
user_string = input("Enter a string: ")
print(f"{user_string} is {'a palindrome' if user_string == user_string[::-1] else 'not a palindrome'}")

# 5. Count vowels and consonants
user_string = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for char in user_string if char in vowels)
consonant_count = sum(1 for char in user_string if char.isalpha() and char not in vowels)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

# 6. Check if one string contains another
string1, string2 = input("Enter first string: "), input("Enter second string: ")
print(f"'{string2}' {'found' if string2 in string1 else 'not found'} in '{string1}'")

# 7. Replace a word in a sentence
sentence, word_to_replace, replacement_word = input("Enter sentence: "), input("Word to replace: "), input("Replacement word: ")
print(sentence.replace(word_to_replace, replacement_word))

# 8. First and last character of a string
user_string = input("Enter a string: ")
print(f"First: {user_string[0]}, Last: {user_string[-1]}")

# 9. Reversed version of a string
user_string = input("Enter a string: ")
print(f"Reversed: {user_string[::-1]}")

# 10. Count words in a sentence
sentence = input("Enter a sentence: ")
print(f"Word count: {len(sentence.split())}")

# 11. Check if a string contains digits
user_string = input("Enter a string: ")
print(f"Contains digits: {'Yes' if any(char.isdigit() for char in user_string) else 'No'}")

# 12. Join words into a string with separator
words = input("Enter words: ").split()
separator = input("Enter separator: ")
print(f"Joined: {separator.join(words)}")

# 13. Remove all spaces from a string
user_string = input("Enter a string: ")
print(f"Without spaces: {user_string.replace(' ', '')}")

# 14. Check if two strings are equal
string1, string2 = input("Enter first string: "), input("Enter second string: ")
print(f"Strings are {'equal' if string1 == string2 else 'not equal'}")

# 15. Create an acronym
sentence = input("Enter a sentence: ")
print(f"Acronym: {''.join(word[0].upper() for word in sentence.split())}")

# 16. Remove a specific character from a string
user_string, char_to_remove = input("Enter a string: "), input("Character to remove: ")
print(f"After removal: {user_string.replace(char_to_remove, '')}")

# 17. Replace vowels with a symbol
user_string = input("Enter a string: ")
print(f"Vowels replaced: {''.join('*' if char in 'aeiouAEIOU' else char for char in user_string)}")

# 18. Check if string starts and ends with specific words
user_string, start_word, end_word = input("Enter a string: "), input("Start word: "), input("End word: ")
print(f"Starts with {start_word} and ends with {end_word}: {'Yes' if user_string.startswith(start_word) and user_string.endswith(end_word) else 'No'}")

# Boolean Data Type Questions

# 1. Check if username and password are not empty
username, password = input("Enter username: "), input("Enter password: ")
print(f"Both are {'not empty' if username and password else 'empty'}")

# 2. Check if two numbers are equal
num1, num2 = int(input("Enter first number: ")),
int(input("Enter second number: ")),
print(f"{num1} and {num2} are {'equal' if num1 == num2 else 'not equal'}")

# 3. Check if a number is positive and even
num = int(input("Enter a number: "))
print(f"{num} is {'positive and even' if num > 0 and num % 2 == 0 else 'not positive and even'}")

# 4. Check if three numbers are different
nums = [int(input(f"Enter number {i+1}: ")) for i in range(3)]
print("All numbers are different" if len(set(nums)) == 3 else "Numbers are not different")

# 5. Check if two strings have the same length
string1, string2 = input("Enter first string: "), input("Enter second string: ")
print(f"Same length: {'Yes' if len(string1) == len(string2) else 'No'}")

# 6. Check if a number is divisible by both 3 and 5
num = int(input("Enter a number: "))
print(f"{num} is divisible by both 3 and 5: {'Yes' if num % 3 == 0 and num % 5 == 0 else 'No'}")

# 7. Check if sum of two numbers is greater than 50.8
num1, num2 = float(input("Enter first number: ")),
float(input("Enter second number: ")),
print(f"Sum greater than 50.8: {'Yes' if num1 + num2 > 50.8 else 'No'}")

# 8. Check if a number is between 10 and 20 (inclusive)
num = int(input("Enter a number: "))
print(f"{num} is {'between 10 and 20' if 10 <= num <= 20 else 'not between 10 and 20'}")
