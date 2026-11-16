n,m = map(int,input().split())
borrowed = set()
for i in range (1,(m+1),+1):
    op,x = map(int,input().split())
    if (op==1 or op==2 or op==3) and (1<=x<=n):
        tf = True
        if op==1: # 借出
            if x not in borrowed:
                borrowed.add(x)
                print("borrow success")
            else:
                print("borrow fail")
        if op==2: # 归还
            if x in borrowed:
                print("return success")
                borrowed.remove(x)
            else:
                print("return fail")
        if op==3: # 查询
            if x not in borrowed:
                print("on shelf")
            else:
                print("borrowed")
    else:
        tf = False