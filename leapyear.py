st = int(raw_input())
if((st%400==0) or ((st%4==0) and (st%100!=0))):
    print("yes")
else:
    print("no")
