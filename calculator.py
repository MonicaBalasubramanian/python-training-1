def add(a,b):#define the module
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return"Error: Division by zero"
    return a//b
print("*****Calculator*****")
print("Press 'q' to quit.\n")
op=""
while op!="q":
    op=input("Enter the option('1','2','3','4','q': )")
    if op=="q":
       print("Exiting...Thankyou!")
       break
    if op not in('1','2','3','4','q'):
       print("Invalid operator.Try again")
       continue
       print("Choose operation")
       print("1.Add")
       print("2.Subtract")
       print("3.Multiply")
       print("4.Division")
    a=int(input("Enter the a value="))
    b=int(input("Enter the b value="))
    if(op=='1'):
      print("Result: ",a+b)
    elif(op=='2'):
      print("Result: ",a-b)
    elif(op=='3'):
      print("Result: ",a*b)
    elif(op=='4'):
      print("Result: ",a//b)
    else:
      print("Invalid option")