arr = [67, 815, 45, 39, 2,901, 34]

ht = [0] * 11

for i in arr:
  h = i % 11
  step = 1
  while ht[h] != 0:
    h2 = (i * 3) % 7
    h = (h + step * h2) % 11
    step += 1
  ht[h] = i

print(ht)