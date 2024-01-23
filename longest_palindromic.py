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
                reversed_lst_one = list(reversed(str_one))
                str_two = ''.join(reversed_lst_one)

                # if the length is bigger than the existing palindromic str, then record the maximum length
                if str_one == str_two and max_length < len(str_one):
                    longest_palindromic_str = str_one
                    max_length = len(str_one)

            index = index + 1

    return longest_palindromic_str
    
# case one: "babad"
s = "babad"

longest_palindromic_str = find_longest_palindromic(s)
assert longest_palindromic_str == "bab"


# case two: "cbbd"
s = "cbbd"
longest_palindromic_str = find_longest_palindromic(s)
assert longest_palindromic_str == "bb"

# # case two: "applepp"
s = "aopepo"
longest_palindromic_str = find_longest_palindromic(s)
assert longest_palindromic_str == "opepo"