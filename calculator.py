#Calculator:
def calculator (a,b,opr):
    if opr=="+":
        return (str(a)+" + "+str(b)+" = "+str(a+b))
    elif opr=="-":
        return (str(a)+" - "+str(b)+" = "+str(a-b))
    elif opr=="*":
        return (str(a)+" * "+str(b)+" = "+str(a*b))
    elif opr=="/":
        if b==0:
            return "Eror: Division by zero is not allowed!"
    else:
        return (str(a)+" / "+str(b)+" = "+str(a/b))   
while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        opr = input("Select your operation: +, -, *, / ")
        print(calculator(a,b,opr)) 
    except ValueError:
     print("Please enter valid numbers.")
    again = input("Do you want to perform another operation? (yes to continue / q to quit): ")
    if again.lower() == "q":
        print("Goodbye! 👋")
        break   






    
