name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引
print(name_list[2])
print(name_list.index("wangwu"))
# print("列表的长度：%d" %(name_list.count()))

#2. 修改

name_list[1] ="李四"

#3. 增加

#append 方法在末尾处追加数据
name_list.append("王小二")
#insert 方法在指定的位置插入数据
name_list.insert(1,"小妹妹")
#extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾
temp_list = ["孙悟空","猪二哥","沙师弟"]
name_list.extend(temp_list)

#4. 删除

# remove 方法可以从列表中删除指定的数据
name_list.remove("wangwu")
# pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
#带参删除指定位置
name_list.pop(1)
#clear 方法可以清空列表
name_list.clear()







print(name_list)

