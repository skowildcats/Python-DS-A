def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2

  left = arr[:mid]
  right = arr[mid:]

  return merge(merge_sort(left), merge_sort(right))



def merge(arr1, arr2):
  res = []
  while len(arr1) > 0 and len(arr2) > 0:
    if arr1[0] < arr2[0]:
      res.append(arr1.pop(0))
    else:
      res.append(arr2.pop(0))
  res += arr1 + arr2
  return res


print(merge_sort([10, 23,51,18,4,31,13,5]))
