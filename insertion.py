nums = [6, 3, 10, 48, 33, 28, 83, 293, 118]


def insertion(nums):
  for i in range(1, len(nums)):
    tmp = nums[i]

    j = i - 1
    while j >= 0 and tmp < nums[j]:
      nums[j + 1] = nums[j]
      j -= 1
    
    nums[j + 1] = tmp
  return nums


print(insertion(nums))
