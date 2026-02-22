num1 = float(input("enter the number 1 "))
num2 = float(input("enter the number 2 "))

sym = input("enter the symbol")

if (sym == "+"):
    print("the value of the add",num1 + num2)
elif(sym == "-"):
    print("the value of the sub",num1 - num2)
elif(sym == "*"):
    print("the value of the multiplication ",num1 * num2)
elif(sym == "/"):
     print("the value of the divide",num1 / num2)
elif(sym == "%"):
     print("the value of the mod ",num1 % num2)

elif(sym == "**"):
    print("the value of the expo",num1 ** num2)

