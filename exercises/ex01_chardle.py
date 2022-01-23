"""EX01 - Chardle - A cute step toward Worlde."""

__author__ = "730461716"
word: str = input("Enter a 5-character word: ")

if len(word) > 5 or len(word) < 5:
    exit("Error: Word must contain 5 characters")

char: str = input("Enter a single character: ")
print("Searching for " + word + " in " + word)
x: int = 0

if char == word[0]:
    print(char + " found at index 0")
    x = x + 1
if char == word[1]:
    print(char + " found at index 1")
    x = x + 1
if char == word[2]:
    print(char + " found at index 2")
    x = x + 1
if char == word[3]:
    print(char + " found at index 3")
    x = x + 1
if char == word[4]:
    print(char + " found at index 4")
    x = x + 1

if x > 1:
    print(str(x) + " instances of " + char + " found in " + word)
else:
    print(str(x) + " instance of " + char + " found in " + word)
if x == 0:
    print("No instances of " + char + " found in " + word)
