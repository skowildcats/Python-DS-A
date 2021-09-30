import random
import string

def shakespear(target):
  res = ""
  count = 1
  char = list(string.ascii_lowercase + " ")

  for _ in range(len(target)):
      res += char[random.randint(0, 26)]


  while res != target:
    tmp = list(res)
    for i in range(len(res)):
      if tmp[i] != target[i]:
        tmp[i] = char[random.randint(0, 26)]
    res = "".join(tmp)
    
    count += 1


    print(res, count)
  
  return (res, count)


print(shakespear(
    "when an unknown printer took a galley of type and scrambled it to make a type specimen book It has survived not only five centuries but also the leap into electronic typesetting remaining essentially unchanged It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum".lower()))
