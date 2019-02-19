inp=raw_input().split()
lower = int(inp[0])
upper= int(inp[1])
for num in range(lower+1,upper):
    if num%2 == 0:
        print num,
