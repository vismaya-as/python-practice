student={}
n=int(input("Enter number of students:"))
for i in range(n):
    name=input("Enter name:")
    roll=int(input("Enter roll no:"))
    gpa=float(input("Enter gpa:"))
    student[name]={ "Gpa":gpa,"Roll no":roll}
print(student)
upname=input("Enter name of student for update:")
upgpa=float(input("Enter updated gpa:"))
for i in student:
    if(upname==i):
        student[i]["Gpa"]=upgpa
print("Updated Dictionary:",student)
