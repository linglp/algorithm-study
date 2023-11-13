import timeit
# implement factorial 

# Example:

# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1
# Replacing the calculated values gives us the following expression
# 4! = 4 * 3 * 2 * 1

# when calculating factorial 4, I would need to first calculate factorial 3
# when calculating factorial 3, I would need to first calculate factorial 2


## recursive approach
def factorial(n):
    if n == 0: 
        return 1
    else:
        print(n)
        return n* factorial(n-1)

start = timeit.default_timer()
factorial(4)
time_cost = timeit.default_timer() - start
print('time cost of recursive approach', time_cost)

## iterative approach
def factorial_iterative(n):
    cal_result = 1
    for i in range(2, n):
        cal_result = cal_result * i

    return cal_result

start_time2 = timeit.default_timer()
factorial(4)
time_cost = timeit.default_timer() - start_time2
print('time cost of recursive approach', time_cost)







