import random

class Lottery:
  def shuffle(self):
    results = []
    for i in range(5):
      results.append(random.randint(1, 20))
    return results

class PowerBall(Lottery):
  
  def shuffle(self):
    return [random.randint(1, 99) for _ in range(0, 6)]
  
power_ball = PowerBall()
print(power_ball.shuffle())
