def frequencySort(self, nums: List[int]) -> List[int]:
  c = Counter(nums).most_common()

  c.sort(key=lambda x: x[0], reverse=True)
  c.sort(key=lambda x: x[1])

  res = []
  for i in c:
      res += [i[0]] * i[1]

  return res
