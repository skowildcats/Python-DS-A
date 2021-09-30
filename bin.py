import string
def binary(num, base):
  res = ""
  hex = dict(zip(range(10, 26), string.ascii_uppercase))

  while num != 0:
    if num % base >= 10:
      res += hex[num % base]
    else:
      res += str(num % base)
    num = num // base
  return res[::-1]


# print(oct(25))
print(binary(26, 26))
print(hex(389289323))
