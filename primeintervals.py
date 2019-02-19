inp=raw_input().split()
lower = int(inp[0])
upper= int(inp[1])

for num in range(lower+1,upper):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print num,
