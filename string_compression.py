import unittest

def compress(s):

  res = ""
  prev, count = s[0], 1

  for char in s[1:]:
    if char == prev:
      count += 1
    else:
      res += prev + str(count)
      prev, count = char, 1
  return res + prev + str(count)



    
      
    
