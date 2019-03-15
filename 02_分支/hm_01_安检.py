has_ticket = True

knife_length = 30

if has_ticket:
    print("车票检查通过，准备开始安检")
    if knife_length > 20:
        print("您的刀太长了，有 %d 公分长" %knife_length)
else:
    print("没有车票，不得入内")

