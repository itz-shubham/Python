# # [factorial of n]
# # n! = n * n - 1 * n - 2 * n - 3 * ... * 1
#
# def factorial(n):
#     """
#         :param n: Integer
#         :return: n! = n * n - 1 * n - 2 * n - 3 * ... * 1
#     """
#
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# number = int(input("Enter the number: "))
#
# print(factorial(number))


# #### fibonacci series

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


numbers = int(input("Enter your number: "))

print(fibonacci(numbers))
