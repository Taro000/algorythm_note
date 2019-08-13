"""
Question, 整数Aと整数Bの最大公約数を求めよ。＝　ユークリッドの互除法

キモ：整数Aと整数Bを余りが０になるまで除算した時の割る数。a/b=c...0の時のb
"""


def euclid(k, l):
    warareru = k
    waru = l
    while waru != 0:
        s = warareru // waru
        d = warareru
        warareru = waru
        waru = d - s * waru
    return warareru


A, B = map(int, input("２つの整数を入力。整数同士の間は１スペースあけて。").split())

if A >= B:
    result = euclid(A, B)
else:
    result = euclid(B, A)

print(result)