def add(num1,num2):
        return num1+num2

def sub(num1,num2):
        return num1-num2

def mult(num1,num2):
        return num1*num2

def div(num1,num2):
        return num1/num2

def mod(num1,num2):
        return num1%num2
while True:
    print("========== CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    operator = input("Choose an option: ")

    if operator=="6":
          print("Thank you for using calculator!")
          break
    
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))

    if operator=="1":
        print(add(num1,num2))
    elif operator=="2":
        print(sub(num1,num2))
    elif operator=="3":
        print(mult(num1,num2))
    elif operator=="4":
        if num2==0:
                print("not divisible by zero")
        else:
                print(div(num1,num2))
    elif operator=="5": 
        if num2==0:
              print("Cannot perform modulus with zero")
        else:
            print(mod(num1,num2))
    else:
        print("invalid operator")
    




 