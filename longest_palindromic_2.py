#### solution 2
def find_center_index_str(random_str:str) -> int:
    """finding center index depending on length of string 

    Args:
        random_str (str): any given string

    Returns:
        int: index of the center letter
    """
    # see if the length is odd or even
    if (len(random_str) % 2) == 0:
        center_index = int(len(random_str) / 2)
    else:
        center_index = int((len(random_str) - 1)/2)
    return center_index

def if_palindromic(random_str:str) -> bool:
    """check if a string is palindromic string 
    The idea is to compare letters in a string starting from both edges

    Args:
        random_str (str): a random str

    Returns:
        bool:a boolean showing if a string is palindromic or not 
    """
    # if the string only contains one letter, then it is still a palindromic string
    if len(random_str) == 1:
        return True
    
    left = 0
    right = len(random_str)
    # find center of a given string
    center_index = find_center_index_str(random_str)
    # keep looping through all the letters from both edges 
    while left < center_index:
        # if the letter on the left is always the same as the letter on the right, 
        # then this letter has potential to be palindromic string
        if random_str[left] == random_str[right-1]:
            left = left + 1
            right = right -1
        else:
            return False
    return  True

def find_palindromic_str(s: str) -> str:
    """find the longest palindromic string 

    Args:
        s (str): a str

    Returns:
        str: the longest palindromic string inside a str
    """

    left_index = 0 
    max_palindromic_length = 0
    # if a string does not contain any palindromic str, return the first letter.
    longest_palindromic_str = s[0]

    while left_index < len(s):
        right_index = len(s)
        while right_index > left_index: 
            str_to_test = s[left_index:right_index]
            # if the length of this string is already smaller than the longest palindromic str
            # that we have already found. Then no need to check if it contains palindromic str
            if len(str_to_test) > max_palindromic_length:
                if if_palindromic(str_to_test) and len(str_to_test) > max_palindromic_length:
                    max_palindromic_length = len(str_to_test)
                    longest_palindromic_str = str_to_test

                    # since we always start from the "longest" possible
                    # if we find a plaindromic string at this point when the right index is relatively big,
                    # we don't have to keep looping with a smaller right index and the same left index
                    right_index = 0
            right_index = right_index - 1
                
        left_index = left_index + 1

    return longest_palindromic_str
        

assert if_palindromic("aba") == True
assert if_palindromic("abcmd") == False
assert if_palindromic("bb") == True
assert if_palindromic("b") == True
assert if_palindromic("bmgcgmb") == True
assert if_palindromic("adccda") == True
assert if_palindromic("baba") == False

assert find_palindromic_str("hadccda") == "adccda"
assert find_palindromic_str("babad") == "bab"
assert find_palindromic_str("cbbd") == "bb"
assert find_palindromic_str("ac") == "a"
assert find_palindromic_str("acccccccc") == "cccccccc"
assert find_palindromic_str("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"

