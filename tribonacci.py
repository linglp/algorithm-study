# write a sequence for tribonacci numbers
# Instead of starting with two predetermined terms, the sequence starts with three predetermined terms and each term afterwards is the sum of the preceding three terms. 

# Example: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, ...
def add_up_three_numbers_in_a_row(numbers_lst):
    """add up three numbers in a row"""
    sum = numbers_lst[-1] + numbers_lst[-2] + numbers_lst[-3]
    return sum


def tribonacci_numbers(n):
    gather_result = []
    if n == 1: 
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        # make sure n > 1
        # so that when calling tribonacci_numbers function, the smallest integer to use is 1
        while n > 1:
            result = tribonacci_numbers(n-1)
            n = n-1
            gather_result.insert(0, result)
        next_num = add_up_three_numbers_in_a_row(gather_result)
        return next_num

result = tribonacci_numbers(5)
print(f'tribonacci numbers before the 8th one', result)