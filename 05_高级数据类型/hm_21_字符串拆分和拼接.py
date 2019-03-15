# 假设：　以下内容是从网络上抓取的
# 要求：
# 1. 将字符串中的空白字符全部去掉
# 2. 在使用 "" 作为分隔符，拼接成一个整齐的字符串
poem_str = "\t\n登黄鹤楼\t王焕之\t\n白日依山尽\t黄河入海流\t欲穷千里目\t更上一层楼"
print(poem_str)


# 1. 拆分字符串
poem_list = poem_str.split()
print(poem_list)

# 2. 拼接字符串
result = " ".join(poem_list)
print(result)