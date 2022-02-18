class Cyclist:
  
  def __init__(self, name, nationality, nickname):
    self._name = name
    self._nationality = nationality
    self._nickname = nickname
    
  def get_name(self):
    return self._name
      
  def get_nationality(self):
    return self._nationality
      
  def get_nickname(self):
    return self._nickname
  
  def set_name(self, new_name):
    self._name = new_name
  
  def set_nationality(self, new_nationality):
    self._nationality = new_nationality
  
  def set_nickname(self, new_nickname):
    self._nickname = new_nickname
    
  name = property(get_name, set_name)
  nationality = property(get_nationality, set_nationality)
  nickname = property(get_nickname, set_nickname)

my_cyclist = Cyclist("Greg LeMond", "American", "Le Montstre")
print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)
my_cyclist.name = "Eddy Merckx"
my_cyclist.nationality = "Belgian"
my_cyclist.nickname = "The Cannibal"
print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)
