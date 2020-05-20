def func(a):
    count=0
    tutl=int(a[0])
    div=int(a[1])
    x=int(tutl/div)
    for i in range(a[2],a[3]+1):
        if i%div==0:
            count+=1
    rsult=x-count
    return rsult
rsult=0
a=[]
totl=int(input())
# for i in range(totl):
#     x=input()
#     a.append(x[0])
#     a.append(x[2])
#     a.append(x[4])
#     a.append(x[6])
#
func(a)


