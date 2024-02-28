
"""
def F(n):
    if (n == 0):
        return 0
    return n + F(n - 1)
print(F(5))
print(F(10))
print(F(-1))


def F(n): #Function returns 0
    if (n == 0):
        return 0
    return n * F(n - 1)
print(F(4))


def F(x, n):
    if (n == 0):
        return 0
    return n + F(x, n - 1)

print(F(-100,100))
"""
def F(n):
    if (n < 0):
        return F(-n) # returns absoulte value
    if (n < 10):
        return n
    return F(n / 10) # returns the division of 10
print(F(7))
