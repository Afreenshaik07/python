import random
p=int(input(“Length of password:- “))
s=’abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?’
m=””
for i in range(p):
m=m+random.choice(s)
print(m)