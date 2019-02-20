print("queue data structure")
queue=[]
while True:
    print("what function do you want to perform? \n 1.insert an element,2.remove an element,3.check the size of a stach,4.emptiness of stack.5.exit")
    n = int(input())
    if n== 1:
        print("enter the element you want to insert:")
        l = input()
        print("where you want to inset? \n 1.first,2.rear")
        option=int(input())
        if option==1:
            queue.insert(0,l)
            print("the elements in queue are:",queue)
        else:
            queue.append(l)
            print("the elements in the queue are:",queue)
    elif n == 2:
        if queue==[]:
            print("empty queue.you cannot delete!!")
        else:
            l=input()
            print("where you want to delete? \n 1.first,2.rear")
            element=int(input())
            if element==1:
                queue.pop(0)
                print("the elements in the queue are:",queue)
            else:
                queue.pop()
                print("the elements in the queue are:",queue)
    elif n==3:
        print("size of queue is:",len(queue))
    elif n==4:
        if queue==[]:
            print("your queue is empty!!")
        else:
            print("you have",len(queue),"elements in your queue")
    elif n==5:
            print("exit")
            break
