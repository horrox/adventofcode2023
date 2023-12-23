import re

with open('day4/input.txt', 'r') as lines:
  total_score = 0
  for line in lines:
    _, winners_str, mynumbers_str = re.split(':|\|', line)
    winners = list(map(int, re.split('\s+', winners_str.strip())))
    numbers = list(map(int, re.split('\s+', mynumbers_str.strip())))

    winner_count = 0
    for entry in winners:
      if entry in numbers:
        winner_count += 1
    if winner_count > 0:
      card_score = 2**(winner_count - 1)
      print(card_score)
      total_score += card_score

print(total_score)