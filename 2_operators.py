# 1 - Arithmetic Operators

print("Arithmetic Operators")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Addition, + ----->", a + b)

print("Subtraction, - ----->", a - b)

print("Multiplication, * ----->", a * b)

print("Division, / ----->", a / b)

print("Remainder/Modulus, % ----->", a % b)

print("Exponent, ** ----->", a ** b)

print("Floor Division, // ----->", a // b)
# 2 - Bitwise Operators

print("Bitwise Operators")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("& Bitwise AND operator ---->", a & b)

print("^ Bitwise XOR operator ---->", a ^ b)

print("| Bitwise OR operator ---->", a | b)
# 3 - Shift Operators

print("Shift Operators")

a = int(input("Enter the value: "))
b = int(input("Enter the value: "))

print("<< Left Shift Operator ---->", a << b)

print(">> Right Shift Operator ---->", a >> b)
# 4 - Identity Operators

print("Identity Operators")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("is identity operator ---->", a is b)

print("is not identity operator ---->", a is not b)
# 5 - Relational Operators

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("> Greater than ---->", a > b)

print("< Less than ---->", a < b)

print("<= Less than or equal to ---->", a <= b)

print(">= Greater than or equal to ---->", a >= b)

print("== Equal to ---->", a == b)

print("!= Not equal to ---->", a != b)
# logical operators
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("AND logical:", a > 0 and b > 0)
print("OR logical:", a > 0 or b > 0)
print("NOT logical:", not (a > 0))
#7- assingment operators
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

a = b
print("Assignment :", a)

a += b
print("Assignment sum :", a)

a -= b
print("Assignment difference :", a)

a *= b
print("Assignment product :", a)

a /= b
print("Assignment quotient :", a)

a %= b
print("Assignment remainder :", a)

a **= b
print("Assignment exponent :", a)

a //= b
print("Assignment floor division :", a)
# 8 - Membership Operators

print("Membership Operators")

a = int(input("Enter the value of a: "))

numbers = [10, 20, 30, 40, 50]

print("in membership operator ---->", a in numbers)

print("not in membership operator ---->", a not in numbers)
#9-  program that find average of three numbers
a = int(input("enter the value of a :"))
b = int(input("enter the value of b :"))
c = int(input("enter the value of c :"))
average= (a+b+c)/3
print("input vlaues are =",a,b,c)
print("average of three number:",average)




























