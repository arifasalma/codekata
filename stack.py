print("stack implementation")
stack=[]
while True:
    print("what function do you want to perform? \n 1.insert an element,2.remove an element,3.check the size of a stach,4.emptiness of stack.5.exit")
    n = int(input())
    if n== 1:
        print("enter the element you want to insert:")
        l = input()
        stack.append(l)
        print("elements in stack are:",stack)
    elif n == 2:
        if stack==[]:
            print("empty stack.you cannot delete!!")
        else:
            stack.pop()
            print("elements in stack are :",stack)
    elif n==3:
        print("size of stack is:",len(stack))
    elif n==4:
        if stack==[]:
            print("your stack is empty!!")
        else:
            print("you have",len(stack),"elements in your stack")
    elif n==5:
            print("exit")
            break
                  
            
