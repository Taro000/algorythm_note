r, g, b = map(int, input("１〜９の整数をスペース区切りで1つずつ入力").split())

if (r*100+g*10+b)%4 == 0:
    print("YES")
else:
    print("NO")