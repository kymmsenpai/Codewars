from direct_reduct import dirReduc

testing_variable = [dirReduc(['EAST', 'NORTH', 'WEST', 'EAST', 'NORTH', 'EAST', 'NORTH', 'NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'SOUTH', 'EAST', 'NORTH', 'SOUTH', 'WEST', 'WEST', 'EAST', 'WEST', 'NORTH']),
                    dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]),
                    dirReduc(['EAST', 'WEST', 'WEST', 'WEST', 'EAST', 'NORTH', 'EAST', 'WEST', 'SOUTH', 'EAST', 'SOUTH', 'NORTH', 'WEST', 'NORTH', 'SOUTH'])]

for tv in testing_variable:
  print()
  print(tv)