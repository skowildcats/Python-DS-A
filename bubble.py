nums = [3, 6, 10, 48, 33, 28, 83, 293]


def bubble(nums):
  sorted = False

  while not sorted:
    sorted = True
    for i in range(len(nums) - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        sorted = False
  

bubble(nums)
print(nums)
  
