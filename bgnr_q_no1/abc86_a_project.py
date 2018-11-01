a, b = map(int, input("2つの整数をスペースで区切って入力して下さい。").split())

if (a*b)%2 == 0:
    print("Even")
else:
    print("Odd")