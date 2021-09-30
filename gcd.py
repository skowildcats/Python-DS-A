def gcd(a, b):
  if a == 0:
    return b
  elif b == 0:
    return a
  
  return gcd(b, a % b)


print(gcd(270, 192))