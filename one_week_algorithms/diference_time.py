"""
Question, 時間Aと時間Bの間は何時何分何秒あるか？　＝　時間A - 時間B

キモ　h時m分s秒を　h*3600 + m*60 + s 秒に変換
"""


def to_second(T: str) -> int:
    h = int(T[:2])
    m = int(T[3:5])
    s = int(T[6:-1])

    return h * 3600 + m * 60 + s


A, B = input('00：00：00(H:M:S)の表記で入力。２つの時間の間は１スペース開ける。').split()  # A, B[str]

A_second = to_second(A)  # A[int]
B_second = to_second(B)  # B[int]

if A_second >= B_second:
    result = A_second - B_second  # result[int]
else:
    result = B_second - A_second

print(A_second, B_second, result)

H = result//3600
M = (result - H*3600)//60
S = (result - H*3600) - M*60

print(f"{H}:{M}:{S}")
