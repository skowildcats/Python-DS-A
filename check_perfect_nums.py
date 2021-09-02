def checkPerfectNumber(self, num: int) -> bool:
  sum = 0
  i = 1
  while i * i < num:
      if num % i == 0:
          sum += i + num / i
      i += 1
  return sum - num == num

# Time Complexity: O(sqrt(n))
# Space Complexity: O(1), constant space used

# Only need to iterate up to square of i, significantly cutting on the number of
# computations necessary as num grows larger
