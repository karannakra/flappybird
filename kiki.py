x=int(input())
lft_brckt=0
rt_brckt=0
count=0
for i in range(x):
    a=str(input())
    if a==')':
        lft_brckt+=1
    if a=='(':
        lft_brckt+=1
    if a=='()':
        lft_brckt+=1
        rt_brckt+=1
if lft_brckt>rt_brckt:
    grtr=lft_brckt
    lowr=rt_brckt
else:
    grtr=rt_brckt
    lowr=lft_brckt
for i in range(1,grtr+1):
    for j in range(1,lowr+1):
        if (i+j)%2==0:
            print(i,j)
            count+=1
print(count)
