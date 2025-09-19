def is_even(n):
   if n % 2 == 0:
     return True
   else:
    return False

def find_max(a, b, c):
  return max(a, b, c)

def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

print(factorial(5))
print(is_even(2))
print(is_even(5))
print(find_max(9, 4, 13))