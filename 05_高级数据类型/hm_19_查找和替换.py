hello_str = "hello world"

#1. 判断是否以指定字符串开始
print(hello_str.startswith("hello"))

#2. 判断是否以指定字符串结束
print(hello_str.endswith("world"))

#3. 查找指定字符串
print(hello_str.find("llo"))
#find 和 index的区别在于，find输出是不报错
print(hello_str.find("abc"))

#4. 替换字符串
#replace 方法不会修改原有的字符串，只会返回一个新的字符串
print(hello_str.replace("world","python"))