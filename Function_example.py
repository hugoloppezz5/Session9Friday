def greet():
    print("Hello!")
    """
    Simple function printing hello
    :return:0
    """
    print("Hello!")
    return 0

def greet_improved(name):
    """
    more complex greet that takes a name as param
    :param name: the name of the person to greet
    :return:  None
    """
    print("Hello", name)

greet_improved("John")
greet_improved("Jane")

def custom_operation(x=0,y=0):
    """
    Custom op: 10x + y
    :param x: the first number
    :param y: the second number
    :return: number, 10x+y
    """
    result = 10*x + y
    return result

print(custom_operation(5,8))
x = custom_operation(5,9) #arguments by position!
print(f"the result of custom_operation is: {x}")
x = custom_operation(y=9,x=5) #argumenrts by name!
print(f"the result of custom_operation is: {x}")
print(custom_operation(5)) #using values for y
print(custom_operation()) #default values for both
print(custom_operation(y=9)) #default value for x

def bond_intro(name):
    print("the name is:",name)

def bond_name(first,last):
    return f"{last},{first} {last}"

print(bond_name("Hugo","Lopez"))
bond_intro(bond_name("Hugo","Lopez"))

