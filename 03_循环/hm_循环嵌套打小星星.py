#在默认的情况下，print 函数输出内容之后，会自动在内容末尾增加换行
i = 1
while i < 5:
    j = 0
    while j < i:
        print("*",end="")
        j += 1
    print("")
    i += 1