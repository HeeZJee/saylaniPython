"""
Answer # 4
Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same
backward as forward, e.g., madam
"""

def palindromeTEST(word):
    reverse = ''.join(reversed(word))
    if word == reverse and word != "":
        return "You entered a palindrome."
    else:
        return "It is'nt palindrome."

check_palindrome = input("Enter any word to test if it is pelindrome: ")
print(palindromeTEST(check_palindrome))