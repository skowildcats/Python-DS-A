num1 = [1, 2, 7, 38, 40,130, 482]
num2 = [4, 8, 39,]

def merge_list(num1, num2):
  newList = []
  a = 0
  b = 0
  while a < len(num1) and b < len(num2):
    if num1[a] < num2[b]:
      newList.append(num1[a])
      a += 1
    else:
      newList.append(num2[b])
      b += 1
  newList += num1[a:] + num2[b:]
  return newList

print(merge_list(num1, num2))
