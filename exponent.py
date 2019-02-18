inp=raw_input().split()
S=int(inp[0])
t=int(inp[1])
power=1
for i in range(1,t+1):
    power=power*S
print(power)    
