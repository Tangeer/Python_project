import random

# player = int(input("请输入您要出的拳："))
player = 1
computer = random.randint(1, 3)

print("玩家选择的拳头是 %d - 电脑出的拳是 %d" % (player, computer))

