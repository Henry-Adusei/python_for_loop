for x in range(0,151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1,101):
    if x%10==0:
        print("Coding Dojo")
    elif x%5==0:
        print("Coding")
    else:
        print(x)

i=0
for x in range(0,500001):
    if x%2!=0:
        i+=x
print(i)

for x in range(2018,0,-4):
    if x>=0:
        print(x)

lowNum=2
highNum=9
mult=3
    #plus 1 in order to include the highNum in the loop
for x in range(lowNum,highNum+1):
    if x%mult==0:
        print(x)
