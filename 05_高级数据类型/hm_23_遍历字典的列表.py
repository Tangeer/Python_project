students = [{"name": "阿土"},
            {"name": "小美"},
            ]

# 在学员列表中搜索指定的姓名
find_name = "李四"

for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)

        #如果已经找到，应该直接退出循环，而不再遍历后续的元素
        break
else:
    print("抱歉，不存在该用户")
print("循环结束！")