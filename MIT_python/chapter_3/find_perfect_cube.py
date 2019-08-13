# 完全立方の立方根を求める

x = int(input())
ans = 0
while ans**3 < abs(x):   # abs(x) - ans **3 という減少関数になっている。距離が０以下になるとループを抜ける。
    ans += 1

if ans**3 != abs(x):
        print(f'{x} is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print(f'Cube root of {x} is {ans}')