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

def count_word_frequency():
    """Count word frequency and save results to 'word_count_report.txt'."""
    # Ensure the sample file exists
    create_sample_file()
    
    # Read the file
    with open("sample.txt", "r") as file:
        text = file.read()

    # Clean the text
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    words = text.split()  # Split into words

    # Count word frequencies
    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(5)

    # Display results
    print(f"\nTotal words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} {'times' if count > 1 else 'time'}")

    # Save results to 'word_count_report.txt'
    with open("word_count_report.txt", "w") as report_file:
        report_file.write("Word Count Report\n")
        report_file.write(f"Total Words: {total_words}\n")
        report_file.write("Top 5 Words:\n")
        for word, count in top_words:
            report_file.write(f"{word} - {count}\n")

    print("\nResults saved to 'word_count_report.txt'.")

if __name__ == "__main__":
    count_word_frequency()