def calculate_reward(points):
  if points < 10:
    return 5
  elif points <= 20:
    return 15
  else:
    return 30

print(calculate_reward(5))
print(calculate_reward(15))
print(calculate_reward(25))

