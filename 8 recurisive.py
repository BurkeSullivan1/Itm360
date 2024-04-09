

def Hanoi(n, start, to, spare):
    if (n == 1):
        print(str(start) + " --> " + str(to))
        return
    Hanoi(n-1, start, spare, to)
    Hanoi(1, start, to, spare)
    Hanoi(n-1, spare, to, start)
print(Hanoi(100,1,3,2))

"""
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

def F(n):
    if (n < 0):
        return F(-n) # returns absoulte value
    if (n < 10):
        return n
    return F(n / 10) # returns the division of 10
print(F(7))
"""