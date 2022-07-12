#Find the sum of all the multiples of 3 or 5 below 1000 
sum = 0
x=1
while x < 1000:
  if x % 5 == 0 or x % 3 == 0:
    sum += x
  x += 1
print("The sum of all the multiples of 3 or 5 below 1000:", sum)