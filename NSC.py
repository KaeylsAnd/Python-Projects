# Choices
print ("Type: Bin to Hexa || Hexa to Bin")

# Input of the user
choice = input("Choose between Hexadecimal to Binary || Binary to Hexadecimal: ")

# Conditional Statements (Hexadecimal to Binary)
if (choice == "Hexa to Bin"):

# Input of the user if Hexa to Bin is chosen
    hexadecimalNumber = input("Enter a hexadecimal number: ")

# bin function means Binary (16 is the base)
    binaryNumber = bin(int(hexadecimalNumber, 16))

# [2:] will get rid of the prefix 0b
    binaryNumber = binaryNumber[2:]

# Output
    print("The binary of" , hexadecimalNumber, "is", binaryNumber)

# Conditional Statement (Binary to Hexadecimal)
elif (choice == "Bin to Hexa"):

# Input of the user if Hexa to Bin is chosen
    binaryNumber = input("Enter a binary number: ")

    # bin function means Binary (2 is the base)
    decimalNumber = int(binaryNumber, 2)

    # hex is hexadecimal
    hexadecimalNumber = hex(decimalNumber)

    # [2:] will get rid of the prefix 0b
    hexadecimalNumber = hexadecimalNumber[2:]

    # Output
    print("The Hexadecimal of", binaryNumber, "is", hexadecimalNumber)

# Conditional Statement (If the input doesn't satisfy the condition above)
else:
    print("Invalid Input, Please refer to the choices above.")
