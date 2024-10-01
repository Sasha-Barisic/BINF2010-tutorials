"""
A script that takes in word(s) provided by the user and prints out the meaning into a file.

Topics:
    user input, reading/writing to files and function creation.

Usage:
    python3 data-wrangling/input.py word1 word2
    python3 input.py word1 word2

Author:
    Sasha Barisic

Date:
    01/10/2024
"""

import sys

from PyDictionary import PyDictionary

# Initialise dictionary.
dictionary = PyDictionary()


def generate_file(filename: str, data: dict):
    with open(f"{filename}_dictionary.txt", "w") as file:

        # Add the results
        if "Noun" in data.keys():
            nouns = data["Noun"]
            file.write(
                f"The word {filename} has {len(nouns)} different meanings and they are:\n"
            )
            file.write("\n")

            for i, n in enumerate(nouns):
                file.write(f"{i + 1}. {n}\n")


def read_file():
    with open(f"cat_dictionary.txt", "r") as file:

        for lines in file:
            print(lines)


def search_dictionary(words: list) -> None:
    # Loop through the list of words
    for word in words:

        # Grab the meaning from the dictionary
        meaning = dictionary.meaning(word)

        # Generate the file
        generate_file(word, meaning)


if __name__ == "__main__":
    # Uncomment the line below to see what it prints out

    if len(sys.argv) > 1:
        words = sys.argv[1:]
        search_dictionary(words)
    else:
        print("No words have been provided. Aborting.")
        exit(1)
