def grade_calculate(m):
    avg=0
    sum=0
    for i in m:
        avg+=i
    sum=avg/5
    if(100>=sum>95):
        return "Grade A+"
    elif(95>=sum>85):
        return "Grade A"
    elif(85>=sum>75):
        return "Grade B+"
    elif(75>=sum>65):
        return "Grade B"
    elif(65>=sum>55):
        return "Grade C"
    elif(55>=sum>45):
        return "Grade D"
    else:
        return "Grade U"
a=[]
for i in range(5):
    print("Subject",i+1,"-")
    a.append(int(input("Enter marks:")))
print("Your Grade:",grade_calculate(a))
