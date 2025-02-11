def my_function():
    print("Hello World") 

my_function()

def my_function_with_args(username, greeting):
    print("Hello, %s, From my Function!, I wish you %s" %(username, greeting))

my_function_with_args("Samuel", "Saludo")

def sum_two_numbers(a, b):
    return a + b

x = sum_two_numbers(5, 5)
print(x)