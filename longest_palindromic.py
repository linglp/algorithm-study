import time
from functools import wraps

#### solution 1
# Given a string s, return the longest palindromic substring in s.
def find_longest_palindromic(str):
    total_length_str = len(str)
    longest_palindromic_str = None
    max_length = 0

    for pos, letter in enumerate(str):
        # for each letter in the str, try to find the next letter that is the same as this letter
        index = 0
        while  index < total_length_str:
            if index!= pos and letter == str[index]:
                # find the length 
                str_one = str[pos:index+1]
                # reverse string one and see if it is the same
                str_two = str_one[::-1]

                # if the length is bigger than the existing palindromic str, then record the maximum length
                if str_one == str_two and max_length < len(str_one):
                    longest_palindromic_str = str_one
                    max_length = len(str_one)

            index = index + 1

    if not longest_palindromic_str:
        return str[0]
    return longest_palindromic_str


s = "babad"
longest_palindromic_str = find_longest_palindromic(s)
assert longest_palindromic_str == "bab"

s = "cbbd"
longest_palindromic_str = find_longest_palindromic(s)
assert longest_palindromic_str == "bb"

s = "aopepo"
longest_palindromic_str = find_longest_palindromic(s)
assert longest_palindromic_str == "opepo"

s = "a"
longest_palindromic_str = find_longest_palindromic(s)
assert longest_palindromic_str == "a"

s = "ac"
longest_palindromic_str = find_longest_palindromic(s)
assert longest_palindromic_str == "a"

s = "eeeeee"
longest_palindromic_str = find_longest_palindromic(s)
assert longest_palindromic_str == "eeeeee"