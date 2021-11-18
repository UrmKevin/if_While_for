#NofN=N=MaxN=""
    #NofN=int(input("How many numbers you want to write? : "))
#if NofN>0:
#    N=int(input("Write your numbers: "))
#    NofN-=1
#    MaxN=N
#    while NofN>0:
#        NofN-=1
#        N=int(input("Write your numbers: "))
#           print("Only numbers!")
#        if N>MaxN: MaxN=N
#    print(MaxN," is the biggest")
#else:
#    print("Wrong input")

#km=sum=10
#print("1. päeval pikkus oli ",km)
#for p in range(2,8,1):
#    km*=1.1
#    print(p,". päeval pikkus oli",round(km,2))
#    sum+=km
#print("Terve tee pikkus oli",round(sum,2))

#m=100
#c=q=""
#while m>0:
#    c=int(input("How many meters you want to buy? "))
#    if m>c:
#        print("Sold!")
#        m-=c
#    elif m==c:
#        print("Sold!",end="\n"+"We don't have any more materials.")
#        m=0
#    else:
#        q=str(input("Sorry, we have only "+str(m)+". Whould you like to buy? yes/no "))
#        a=q.lower()
#        if a=="yes":
#            print("Sold!",end="\n"+"We don't have any more materials.")
#            m=0
#        elif a=="no":
#            print("Have a good day!")
#        else:
#            print("Invalid input")
        
 #28
#from random import*
#secret=randint(1,10)
#ans=att=0
#while ans!=secret:
#    ans=int(input("Guess a number from 1 to 10: "))
#    att+=1
#print("U got this! You used ",att," attemts")

a=b=h=-1
while True:
    start=str(input("Хотите решить площадь трапеции? y/n "))
    if start.lower()=="y":
        while a<0:
            a=float(input("Первое основание: "))
        while b<0:
            b=float(input("Второе основание: "))
        while h<0:
            h=float(input("Высота: "))
        print((a+b)/2*h)
    elif start.lower()=="n":
        print("Хорошего дня!")
        break
    else:
        break
