# 1.输入苹果的价格
price_str = input("苹果的单价：")
# 2.输入苹果的重量
weight_str  = input("苹果的重量：")
# 3.计算支付的总金额
money = float(price_str)* float(weight_str)
# 打印总金额
print(money)