InputValue=raw_input()
s,t,u=InputValue.split(" ")
if((s>t) and (s>u)):
    print(s)
elif((t>u) and (t>s)):
    print(t)
elif((u>s) and (u>t)):
    print(u)
