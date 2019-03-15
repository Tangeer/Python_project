for num in [1,2,3]:
    print(num)
    # 遇到break就不会执行else里的代码
    if num == 2:
        break
else:
    print("会执行吗？")
print("循环结束")