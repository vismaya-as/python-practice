num=[3,9,7,2,1]
def largest(n):
    large=n[0]
    for i in n:
        if(large<i):
           large=i
    num.remove(large)
    return large
print(largest(num))
print("Second largest:",largest(num))
