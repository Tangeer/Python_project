xiaoming_dict = {"name": "小明"}

# 1. 取值
print(xiaoming_dict["name"])
#在取值的时候，如果指定的key不存在，程序会报错！

# 2. 增加/修改
xiaoming_dict["age"] = 18
xiaoming_dict["name"] = "小小明"
print(xiaoming_dict)

# 3. 删除
# xiaoming_dict.pop("name")
xiaoming_dict.clear()
print(xiaoming_dict)