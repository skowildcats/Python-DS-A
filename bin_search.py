nums = [2, 5, 10, 11, 23, 25, 50, 130]

def bin_search(nums, target):
  start = 0
  end = len(nums) - 1

  while start <= end:
    mid = (start + end) // 2

    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return start

print(bin_search(nums, 3))
  
