import random
n = random.randint(1,100)
a = -34
Gusse = 0
while(a != n):
    a = int(input("Gusse the number :"))
    if (a>n):
        print("Gusse lower number")
        Gusse +=1
    elif(a<n):
        print("Gausse higher number")
        Gusse +=1
print(f"Comgratulation! You gause the number in {Gusse} attempt")

