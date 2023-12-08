import re

game_results = []
with open('day2/input.txt', 'r') as lines:
  game_results.append({ 'red': 0, 'green': 0, 'blue': 0 })
  for line in lines:
    game, results = line.split(':')
    game_number = int(re.findall('Game ([0-9]+)', game)[0])
    game_results.append({})
    for result in results.strip().split(';'):
      for color_count in result.strip().split(','):
        count, color = color_count.strip().split(' ')
        if color in game_results[game_number]:
          game_results[game_number][color] = max(game_results[game_number][color], int(count))
        else:
          game_results[game_number][color] = int(count)

sum_powers = 0
for result in game_results:
  power = result['red'] * result['green'] * result['blue']
  sum_powers += power

print(sum_powers)