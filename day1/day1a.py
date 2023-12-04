input = open("day1/input.txt", "r")
lines = input.readlines()
magicNumber = 0
for line in lines:
  for i, char in enumerate(line):
    if char.isdigit():
      first = char
      break
  for i, char in enumerate(line[::-1]):
    if char.isdigit():
      last = char
      break
  magicNumber += int(first + last)

print(magicNumber)