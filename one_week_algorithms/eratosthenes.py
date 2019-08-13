"""
Question, 整数N以下の素数をすべて列挙せよ。 ＝　エラトステネスのふるい

キモ：明らかな素数である２の倍数を消し、次に2以上で最小の素数３の倍数を消す。以下を整数N以下の最大素数まで続ける。
"""

N = int(input("整数を１つ。"))

data = []
result = []
m = 2
n = 0

for i in range(N+1):
    data.append(1)
    result.append(0)

data[0] = 0
data[1] = 0


while N > m:
    i = 2 * m
    if data[m] == 1:
        while N > i:
            data[i] = 0
            i += m

        result[n] = m
        n += 1
    m += 1


print([y for y in result if y > 0])
