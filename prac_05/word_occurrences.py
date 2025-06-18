"""CP1404 Practical
Program to count word occurrences in a string
Estimated time to complete: 30 minutes
"""

# Get input string from user
text = input("Text: ")

# Create dictionary to store word counts
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

# Find the longest word length for formatting
max_length = max(len(word) for word in word_counts.keys())

# Sort and print word counts with aligned formatting
for word in sorted(word_counts.keys()):
    print(f"{word:{max_length}} : {word_counts[word]}")