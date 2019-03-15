info_tuple = ("张三", 18, 1.75)

# 1. 取值和取索引
print(info_tuple[0])
#已经知道元组的数据内容
print(info_tuple.index(1.75))

# 2. 统计计数
print(info_tuple.count("张三"))

print(len(info_tuple))