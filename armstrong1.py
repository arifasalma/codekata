inp=raw_input().split()
lower =int(inp[0])
upper= int(inp[1])
for num in range(lower+1,upper):
   order= len(str(num))
   sum=0
   temp=num
   while temp >0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)
       
       
 
