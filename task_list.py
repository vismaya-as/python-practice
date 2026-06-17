task=[]
date=input("Enter today's date(dd/mm/yy):")
n=int(input("Enter number of tasks:"))
for i in range(n):
    print("Enter task number",i+1,":")
    task.append(input())
print("DATE:",date,"\nTODAY'S TO-DOs:\n")
for i in task:
        print("->",i)
q=input("Would you like to add tasks?(yes/no):")
if(q=="yes"):
    task.append(input("Enter new task:"))
print("\nDATE:",date,"\nUPDATED TO-DO LIST:")
for i in task:
        print("->",i)
