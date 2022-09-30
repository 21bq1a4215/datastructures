from random import randint
s=''
for k in range (100):
   s=s+str(randint(0,1))
print(s)
z=0
for k in range(100+1):
    if "0"*k in s:
        z=k
print(z)
    


