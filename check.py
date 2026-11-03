def check_energy(energy):
  if energy <= 0:
    return "game over"
  else:
    return "keep playing"
print(check_energy(0))
print(check_energy(3))
