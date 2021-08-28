cache = {}

def fib(n):
  if n in cache:
    return cache[n]

  if n == 1 or n == 2:
    retVal = 1
  else:
    retVal = fib(n-1) + fib(n-2)

  cache[n] = retVal
  return retVal



print(fib(10))


def recFib(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n - 1) + fib(n -2)
  
print(recFib(10))


