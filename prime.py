def check(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("no")
            return False
        else:
            return check(n, div-1)
    else:
        print("yes")
        return 'True'
n=int(input())
check(n)
