def sum_def(x , y , /):
    return x + y

def print_def(*, name, age):
    print(f'my name is {name} and {age} years old')

def calculator(x, y, /, *, operator):
    if operator == '+':
        return x + y
    elif operator == '*':
        return x * y
    elif operator =='-':
        return x - y
    elif operator =='/':
        return x / y


print(sum_def(2 , 3))
print_def(name= 'ali' , age= 23)
inp_int1 = int(input("num1: "))
inp_int2 = int(input('num2: '))
inp = input("enter operator: ")

print(calculator(inp_int1 , inp_int2 , operator= inp))
