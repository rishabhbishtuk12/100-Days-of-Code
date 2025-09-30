def factorial(value):
  if value == 1:
    print("Done!")
    return 1
  else:
    return value * factorial(value-1)

print(factorial(5))