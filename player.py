def player_level(points):
  if points < 10:
    return "beinner"
  elif points <= 20:
    return "intermediate"
  else:
    return "expert"

print(player_level(5))
print(player_level(15))
print(player_level(25))
    
