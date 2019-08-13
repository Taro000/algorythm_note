x = int(input())

root = 1
while root ** 2 < x:  # 減少関数1つ目
    root += 1

pwr = 100
while pwr > 0:  # 減少関数2つ目

    # MIT教科書ではここに1つ目の減少関数を置いてたけど外出せるよね
    # root = 1
    while root ** 2 < x:
        root += 1

    if root**pwr == x:
        print(root, pwr)
    pwr -= 1
