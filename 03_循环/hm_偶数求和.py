#计算 0~100之间的所有的偶数累计求和结果

i = 0
sum = 0

while i <= 100:
    if i%2 ==0:
        sum += i
        print(i)
        i += 1

print(sum)