place=["tambaram","adayar","ambathur"]
dist=[35,30,50]
price=[7,8,9]
print("WHERE DO YOU WANT TO GO?\n 1.tambaram,2.adayar,3.ambathur")
choice=int(input())
if choice==1:
       kms=dist[0]
       print("the place you have choosed is tambaram")
elif choice==2:
       kms=dist[1]
       print("the place you have choosed is adayar")
elif choice==3:
       kms=dist[2]
       print("the place you have choosed is ambathur")
print("WHICH TYPE DO YOU WANT?\n 1.nano,2.micro,3.mini,4.prime")
option=int(input())
if option==1:
    cost=price[o]
    print("the type of cab choosed is nano")
elif option==2:
    cost=price[1]
    print("the type of cab choosed is micro")
elif option==3:
    cost=price[2]
    print("the type of cab choosed is mini")
elif option==4:
    cost=price[4]
    print("the type of cab choosed is prime")
print ("the estimated amount is",kms*cost)
print ("do you want to confirm this booking?\n 1.yes,2.no")
choice=int(input())
if choice==1:
    print("thanks for your booking")
elif choice==2:
    print("better try next time")
       
       
