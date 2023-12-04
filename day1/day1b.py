numberWords = [
  'zero',
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
]

numberDigits = [
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

magicNumber = 0
input = open("day1/input.txt", "r")
lines = input.readlines()
for line in lines:
  digitIndexes = []
  for i, numberWord in enumerate(numberWords):
    found = line.find(numberWord)
    if found >= 0:
      digitIndexes += [(i, found)]
  for i, numberDigit in enumerate(numberDigits):
    found = line.find(numberDigit)
    if found >= 0:
      digitIndexes += [(i, found)]
  for i, numberWord in enumerate(numberWords):
    found = line.rfind(numberWord)
    if found >= 0:
      digitIndexes += [(i, found)]
  for i, numberDigit in enumerate(numberDigits):
    found = line.rfind(numberDigit)
    if found >= 0:
      digitIndexes += [(i, found)]

  orderedIndexes = sorted(digitIndexes, key=lambda digit: digit[1])
  first = orderedIndexes[0][0]
  last = orderedIndexes[len(orderedIndexes) - 1][0]
  magicNumber += first*10 + last

print(magicNumber)