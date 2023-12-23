import re

with open('day4/input.txt', 'r') as lines:
  card_copy_count = []
  total_score = 0
  for line in lines:
    game, winners_str, mynumbers_str = re.split(':|\|', line)
    game_num = int(game.replace('Card', ''))
    winners = list(map(int, re.split('\s+', winners_str.strip())))
    numbers = list(map(int, re.split('\s+', mynumbers_str.strip())))
    
    winner_count = 0
    for entry in winners:
      if entry in numbers:
        winner_count += 1
    for i in range(len(card_copy_count) - 1, game_num + winner_count - 1):
      card_copy_count.append(0)
    card_copy_count[game_num - 1] += 1
    for i in range(game_num, game_num + winner_count):
      card_copy_count[i] += card_copy_count[game_num - 1]

sum = 0
for i in range(0, game_num):
  sum += card_copy_count[i]

print(sum)