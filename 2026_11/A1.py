n = int(input()) # 最大行数
for i in range(1,(n+1),+1): # 左闭右开
    print(" "*(n-i),"*"*((2*i)-1))