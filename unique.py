def unique(str):
  s = set()

  for char in str:
    if char in s:
      return False
    s.add(char)
  
  return True

print(unique("heloy"))