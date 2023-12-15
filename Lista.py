import random

num=[0,1,2,3,4,5,6,7,8,9]
asc=[0,1,2,3,4,5,6,7,8,9]
des=[0,1,2,3,4,5,6,7,8,9]

a=len(num)
for i in range(a):
    numrandom=random.randint(1, 100)
    num[i]= numrandom
    print (f"El numero {i+1} es {num[i]}")
for i in range(a):
    asc[i]=num[i]
    des[i]=num[i]
n=len(asc)
for i in range(n-1):       #
        for j in range(n-1-i): 
            if asc[j] > asc[j+1]:
                asc[j], asc[j+1] = asc[j+1], asc[j]
for i in range(n-1):       #
        for j in range(n-1-i): 
            if des[j] < des[j+1]:
                des[j], des[j+1] = des[j+1], des[j]
print ("La lista ascendente es: ")
for i in range(n):
    print(asc[i])
print ("La lista descendete es: ")
for i in range(n):
    print(des[i])