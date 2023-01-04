arr = range(1,101)
evens = sorted([e for e in arr if e%2 ==0])

total = 0
for number in evens:
  total += number
print(total)
