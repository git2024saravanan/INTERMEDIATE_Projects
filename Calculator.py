
from art import logo
print(logo)
def add(n1,n2):
  return n1 + n2
def subtract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2

operations={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  for symbol in operations:
    print(symbol)
  should_continue=True
  while should_continue:
    operations_symbol = input("Pick the operation from the line above: ")
    calculation_function=operations[operations_symbol]
    first_answer=calculation_function(num1,num2)
    print(f"{num1} {operations_symbol} {num2} = {first_answer}")
    
    operations_symbol = input("Pick another operation: ")
    num3=int(input("Enter the next number: "))
    calculation_function=operations[operations_symbol]
    second_answer=calculation_function(calculation_function(num1,num2),num3)
    print(f"{first_answer} {operations_symbol} {num3} = {second_answer}")
    if input("Type 'y' to continue with the answer or type 'n' to exit: ") == 'y':
      num1=first_answer
    else:
      should_continue=False
      calculator()
calculator()