#Question no 9:-
import math

try:
    sentence = input("Enter a sentence: ")

    if sentence.strip() == "":
        raise ValueError("Empty sentence is not allowed")

    words = set(sentence.split())

    print("Unique words:")
    for word in sorted(words):
        print(word)

    total = len(words)

    print("Number of unique words:", total)
    print("Unique words count raised to power 2:", math.pow(total, 2))

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Something went wrong:", e)