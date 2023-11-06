# implement factorial 

# Example:

# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1
# Replacing the calculated values gives us the following expression
# 4! = 4 * 3 * 2 * 1

# when calculating factorial 4, I would need to first calculate factorial 3
# when calculating factorial 3, I would need to first calculate factorial 2

def factorial(n):
    if n == 0: 
        return 1
    else:
        print(n)
        return n* factorial(n-1)

result = factorial(3)
print('result', result)
