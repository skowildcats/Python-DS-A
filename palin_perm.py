import collections

def palin_perm(string):
  d = collections.defaultdict(int)
  for char in string:
    if char != " ": d[char.lower()] += 1

  odd = False
  
  for value in d.values():
    if value % 2 != 0 and odd:
      return False
    if value % 2 != 0:
      odd = True
  return True


print(palin_perm("Tact Cata"))

