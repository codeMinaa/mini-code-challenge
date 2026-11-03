
def check_energy(energy):
  if energy > 5:
    return "high energy"
  elif energy > 0:
    return "low energy"
  else:
    return "game over"
print(check_energy(8))
print(check_energy(3))
print(check_energy(0))  