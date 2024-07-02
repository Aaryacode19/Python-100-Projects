import math
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def div(n1,n2):
  return n1/n2
def mul(n1,n2):
  return n1*n2
def calc(n1=None):
  if n1 is None:
    n1 = float(input('Enter number 1: '))  # Convert input to float
  n2 = float(input('Enter number 2: '))
  operation = input("tell the operation you wanna perform")
  if operation == "add":
    result = add(n1,n2)
  elif operation == "sub":
    sub(n1,n2)
  elif operation == "mul":
    mul(n1,n2)
  elif operation == "div":
    div(n1,n2)
  else:
    print("Invalid operation!")
    return
  print("Result:", result)
  return result
should_continue = True
n1 = None
while should_continue:
  result = calc(n1)
  again = input("Type 'y' to continue calculating, or type 'n' to start a new calculation: ")
  if again == "y":
    n1 = result
  else:
    should_continue = False
## Modified the calc() function to take an optional argument 'n1' which represents the first number in the calculation.
# If 'n1' is provided (not None), the function skips the input prompt for 'n1' and uses the provided value.
# Updated the main loop to initialize 'n1' to None and pass it to calc() on each iteration.
# After each calculation, the result is stored in 'n1' for use in the next iteration, eliminating the need to prompt the user for 'n1' again.
   #also can refer https://chatgpt.com/share/ebbf4e39-c49c-438f-a9e9-76d0949bdf9a
    
