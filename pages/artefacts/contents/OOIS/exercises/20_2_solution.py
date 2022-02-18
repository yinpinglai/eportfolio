class Airplane:
  def __init__(self, first_class, business_class, coach):
    self._first_class = first_class
    self._business_class = business_class
    self._coach = coach
  
  def total(self):
    return self._first_class + self._business_class + self._coach
  
class Train:
  def __init__(self, car1, car2, car3, car4, car5):
    self._car1 = car1
    self._car2 = car2
    self._car3 = car3
    self._car4 = car4
    self._car5 = car5
  
  def total(self):
    return self._car1 + self._car2 + self._car3 + self._car4 + self._car5
  
def passengers(obj):
  print(f'There are {obj.total()} passengers on board.')
  
airplane = Airplane(10, 20, 30)
train = Train(10, 10, 20, 40, 50)
print(passengers(airplane))
print(passengers(train))
