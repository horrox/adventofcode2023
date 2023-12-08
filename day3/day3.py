import re
from functools import reduce

parts = []
symbols = []
ints =  re.compile(r'\d+')
syms = re.compile(r'[^0-9\n.]')
with open('day3/input.txt', 'r') as lines:
  for line_num, line in enumerate(lines):
    for part_match in ints.finditer(line):
      parts.append({'row': line_num, 'col_start': part_match.start(), 'col_end': part_match.end() - 1, 'part': int(part_match.group())})
    for sym_match in syms.finditer(line):
      symbols.append({'row': line_num, 'col': sym_match.start(), 'symbol': sym_match.group()})

# most inefficient search ever!
part_list = []
for part in parts:
  for sym in symbols:
    if abs(sym['row'] - part['row']) <= 1:
      if sym['col'] >= part['col_start'] - 1 and sym['col'] <= part['col_end'] + 1:
        part_list.append(part['part'])
        break

# Part A
part_sum = sum(part_list)
print(part_sum)

# most inefficient search ever, part 2!
gear_part_list = []
gears = (sym for sym in symbols if sym['symbol'] == '*')
for sym in gears:
  part_list = []
  for part in parts:
    if abs(sym['row'] - part['row']) <= 1:
      if sym['col'] >= part['col_start'] - 1 and sym['col'] <= part['col_end'] + 1:
        part_list.append(part['part'])
  if len(part_list) > 1:
    gear_part_list.append(part_list)

# Part B
def product(iterable): return reduce(lambda a, b: a * b, iterable, 1)
ratio_sum = sum(map(product, gear_part_list))
print(ratio_sum)
