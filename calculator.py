def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b!=0):
        return a/b
    else:
        return "Division by 0 not possible"
n=int(input("Enter number 1:"))
m=int(input("Enter nummber 2:"))
op=input("Enter operation to be performed[add,sub,mul,div]:")
if(op=="add"):
    print(add(n,m))
elif(op=="sub"):
    print(sub(n,m))
elif(op=="mul"):
    print(mul(n,m))
else:
    print(div(n,m))
