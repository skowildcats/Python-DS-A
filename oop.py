class Car:
  def __init__(self, miles = 0):
    self.mileage = miles
    self.warrant = 10
  
  def miles(self):
    print(self.mileage)

  def warranty(self):
    print(self.warrant)

class Honda(Car):
  def __init__(self, miles=0):
    Car.__init__(self)
    self.mileage = miles + 5

newCar = Car(5)
newCar.miles()
newCar.warranty()

newHonda = Honda(4)
newHonda.miles()
newHonda.warranty()

