# Simple Calculator using functions
# Demonstrates basic Python concepts: functions, conditionals, and error handling

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


print("Calculator Example")
print(add(2, 3))
print(divide(10, 2))