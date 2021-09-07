class Bag:
  def __init__(self):
    self._items = []

  def length(self):
    return len(self._items)

  def contains(self, item):
    return item in self._items

  def add(self, item):
    self._items.append(item)


tmp = Bag()
tmp.add(5)
tmp.add(6)
print(tmp.contains(4))


