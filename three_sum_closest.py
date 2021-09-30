def threeSumClosest(nums, target):
  ps = [0] * len(nums)
  s = sorted(nums)

  d = [target - num for num in s]

  for i, num in enumerate(s):
    ps[i] = ps[i-1] + num

  print(s)
  print(d, ps)

threeSumClosest([-1, 2, 1, -4], 1)

# min(x + y + z - target)
