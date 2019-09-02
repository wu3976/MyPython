#This program would simulator a more advanced calculator
num1=float(input("Enter the first number: "))
operator=input("Enter operator: ")
num2=float(input("Enter the second number: "))
result=0
print_it=True

#figure out what operator in user's input
if (operator=="+"):
    result=num1+num2
elif (operator=="-"):
    result=num1-num2
elif (operator=="*"):
    result=num1*num2
elif (operator=="/"):
    result=num1/num2
elif (operator=="%"):
    result=num1%num2
else: #in case none of them are satisfied, print an error
    print_it=False
    print("Invalid operator!")

if (print_it):
    print(result)

