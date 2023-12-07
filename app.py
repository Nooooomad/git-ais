#def factorial(n):
def factorial(n):
    total = 1
    for number in range(1, n + 1):
        total = total * number
    return total


result1 = factorial(0)
print(result1)

result2 = factorial(5)
print(result2)