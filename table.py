chip=input()
a=int(chip[0])
b=int(chip[2])
c=int(chip[4])
d=int(chip[6])
tempi=a
tempo=1
temp=0
min=d*a
flag=True
if a%b==0:
    print('hello')
    print(0)
else:
    for i in range(1,2000):
        a=tempi+tempo

        if a%b==0:
            break
        tempo+=1
    if min>tempo*c:
        min=tempo*c
        print(min)
    else:
        print(min)



