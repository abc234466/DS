def fib_db(n):
    return [-1]*(n+1)

n = int(input())

table = fib_db(n)

def fib(n):
    if table[n] >=0:
        return table[n]
    else:
        if n <= 1:
            table[n] = n
            return n
        else:
            table[n] = fib(n-1) + fib(n-2)
            return table[n]
print(fib(n))
    
