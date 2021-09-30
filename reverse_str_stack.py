
def reverse(str):
  stack = []

  for char in str:
    stack.append(char)

  res = ""
  while stack:
    res += stack.pop()

  return res

print(reverse("Hello"))