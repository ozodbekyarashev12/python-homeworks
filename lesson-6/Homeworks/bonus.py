import os
import string
from collections import Counter

def create_sample_file():
    """Create 'sample.txt' if it doesn't exist."""
    if not os.path.exists("sample.txt"):
        print("The file 'sample.txt' does not exist.")
        content = input("Please enter the text to create 'sample.txt':\n")
        with open("sample.txt", "w") as file:
            file.write(content)
        print("'sample.txt' created successfully!")

def count_word_frequency(top_n):
    """Count word frequency and save results to 'word_count_report.txt'."""
    # Ensure the sample file exists
    create_sample_file()
    
    # Read the file efficiently line by line
    word_counts = Counter()
    with open("sample.txt", "r") as file:
        for line in file:
            # Clean the line: lowercase, remove punctuation, and split
            line = line.lower().translate(str.maketrans("", "", string.punctuation))
            words = line.split()
            word_counts.update(words)  # Update the counter with the words in the line

    # Total words and top N words
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(top_n)

    # Display results
    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in top_words:
        print(f"{word} - {count} {'times' if count > 1 else 'time'}")

    # Save results to 'word_count_report.txt'
    with open("word_count_report.txt", "w") as report_file:
        report_file.write("Word Count Report\n")
        report_file.write(f"Total Words: {total_words}\n")
        report_file.write(f"Top {top_n} Words:\n")
        for word, count in top_words:
            report_file.write(f"{word} - {count}\n")

    print("\nResults saved to 'word_count_report.txt'.")

if __name__ == "__main__":
    create_sample_file()
    try:
        # Prompt the user for the number of top words to display
        top_n = int(input("How many top common words would you like to display? "))
        if top_n <= 0:
            print("Please enter a positive integer.")
        else:
            count_word_frequency(top_n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")