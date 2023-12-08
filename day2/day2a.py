import re

game_results = []
with open('day2/input.txt', 'r') as lines:
  game_results.append({ 'red': 0, 'green': 0, 'blue': 0 })
  for line in lines:
    game, results = line.split(':')
    game_number = int(re.findall('Game ([0-9]+)', game)[0])
    game_results.append({ 'red': 0, 'green': 0, 'blue': 0 })
    for result in results.strip().split(';'):
      for color_count in result.strip().split(','):
        count, color = color_count.strip().split(' ')
        game_results[game_number][color] = max(game_results[game_number][color], int(count))

max_red = 12
max_green = 13
max_blue = 14

valid_games_sum = 0
for index, result in enumerate(game_results):
  if result['red'] > max_red:
    continue
  if result['green'] > max_green:
    continue
  if result['blue'] > max_blue:
    continue
  valid_games_sum += index

print(valid_games_sum)