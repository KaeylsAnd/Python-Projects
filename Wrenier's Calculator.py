print("CALCULATOR BY: CARILLO WRENIER G:")
print("Choose an operation to be used. Pick a number on the corresponding options below:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operations = int(input("Enter the Number of Operation:"))

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

if operations == 1:
    print("The sum is: ", add)
elif (operations) == 2:
    print("The difference is: ", sub)
elif operations == 3:
    print("The product is: ", mul)
elif operations == 4:
    print("The quotient is: ", div)
else:
    print("Unsupported Operation. Please Select a Number Between 1 - 4")
