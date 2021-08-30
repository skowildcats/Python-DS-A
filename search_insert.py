def searchInsert(nums, target):
  idx = len(nums) // 2

  if len(nums) == 0:
      return 0
  elif nums[idx] == target:
      return idx
  else:
      if nums[idx] > target:
          return searchInsert(nums[0:idx], target)
      else:
          return idx + searchInsert(nums[idx+1:len(nums)], target) + 1


print(searchInsert([1,3,5,6], 2))