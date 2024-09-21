#prompt the users to input num1 and num2
num1=float(input("enter the first number you choose: "))
num2=float(input("enter the second number: "))

# prompt the users to choose the operation

opration=input("enter the opration(+,*,-,/): ")
match opration:
    case '+':
        result=num1+num2
        print(result)
    case '*':
        result=num1*num2
        print(result)
    case'-':
        result=num1-num2
        print(result)
    case'/':
        if num2 !=0:
            result=num1/num2
            print(result)  
        else:
            print("error number can not divided by zero")
    case _:
        print("enter the valid operation")                  
