input = open("day1/input.txt", "r")
lines = input.readlines()
magic_number = 0
for line in lines:
  for i, char in enumerate(line):
    if char.isdigit():
      first = char
      break
  for i, char in enumerate(line[::-1]):
    if char.isdigit():
      last = char
      break
  magic_number += int(first + last)

print(magic_number)