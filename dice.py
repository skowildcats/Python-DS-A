import random

class Dice:
  def __init__(self, num_sides = 6) -> None:
    self.num_sides = num_sides
    self.curr_value = self.roll()

  def roll(self):
    self.curr_value = random.randint(1, self.num_sides + 1)
    return self.curr_value


six_sided = Dice()
ten_sided = Dice(10)

print(six_sided.roll())
print(six_sided.curr_value)

print(six_sided.roll())
print(six_sided.curr_value)

# print(ten_sided.curr_value)
