d=[]
print("STUDENT MANAGEMENT SYSTEM\n")
n=int(input("Enter number of students:"))
for i in range(n):
    print("Enter student",i+1,"name")
    d.append((input(":")))
print("List:",d)
g=input("Enter student to be removed:")
for i in d:
    if(g==i):
        d.remove(i)
print("Updated list:",d)
    
