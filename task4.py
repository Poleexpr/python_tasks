boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

sortedBoys = sorted(boys)
sortedGirls = sorted(girls)
k = -1

if len(boys) == len(girls):
 while k < len(boys) - 1:
  k = k + 1
  print(sortedBoys[k], sortedGirls[k])
  