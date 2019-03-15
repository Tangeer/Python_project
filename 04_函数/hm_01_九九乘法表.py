
def multiple_table():
    # 九九乘法表的特点：乘号前一个数为列数，乘号后一个数为行数
    row = 1
    while row < 10:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (col, row, row * col), end="\t")
            col += 1
        print("")
        row += 1









