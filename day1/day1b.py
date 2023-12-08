number_words = [
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

number_digits = [
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

magic_number = 0
input = open("day1/input.txt", "r")
lines = input.readlines()
for line in lines:
  digit_indexes = []
  for i, numberWord in enumerate(number_words):
    found = line.find(numberWord)
    if found >= 0:
      digit_indexes += [(i, found)]
  for i, numberDigit in enumerate(number_digits):
    found = line.find(numberDigit)
    if found >= 0:
      digit_indexes += [(i, found)]
  for i, numberWord in enumerate(number_words):
    found = line.rfind(numberWord)
    if found >= 0:
      digit_indexes += [(i, found)]
  for i, numberDigit in enumerate(number_digits):
    found = line.rfind(numberDigit)
    if found >= 0:
      digit_indexes += [(i, found)]

  ordered_indexes = sorted(digit_indexes, key=lambda digit: digit[1])
  first = ordered_indexes[0][0]
  last = ordered_indexes[len(ordered_indexes) - 1][0]
  magic_number += first*10 + last

print(magic_number)