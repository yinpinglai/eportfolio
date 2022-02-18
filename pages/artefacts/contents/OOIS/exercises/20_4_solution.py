class Median:
  
  def calculate_median(
    self,
    a=None,
    b=None,
    c=None,
    d=None,
    e=None
  ):
    data = []
    if (a != None):
      data.append(a)
    if (b != None):
      data.append(b)
    if (c != None):
      data.append(c)
    if (d != None):
      data.append(d)
    if (e != None):
      data.append(e)
    
    data.sort()
    data_length = len(data)
    if data_length % 2 == 0:
      upper_index = data_length // 2
      lower_index = data_length // 2 - 1
      return (data[lower_index] + data[upper_index]) / 2
    else:
      median_index = len(data) // 2
      return data[median_index]
    
m = Median()
print(m.calculate_median(3, 5, 1, 4, 2))
print(m.calculate_median(8, 6, 4, 2))
print(m.calculate_median(9, 3, 7))
print(m.calculate_median(5, 2))
