def add(a,b):
    return a+b

def sub(a,b ):
    return a-b

def mult(a,b):
    return a *b

def div(a,b):
    if b/0:
        return "Cannot divide by zero"
    return a/b

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice =input("Enter your choice :")

a = float(input("Enter the first number :"))
b = float(input("Enter the second number :"))

if choice == "1":
    print(add(a,b))
elif choice == "2":
    print(sub(a,b))
elif choice == "3":
    print(mult(a,b))
elif choice == "4":
    print(div(a,b))
else:
    print("Invalid Choice")
