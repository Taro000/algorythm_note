"""
Question, 配列の長さと最大値、合計を求めよ。

キモ：繰り返し処理で変数「長さ」、変数「最大値」、変数「合計」を更新していく。
"""

num_text = input("適当に数字を羅列してください")

taget_list = []
for i in num_text:
    taget_list.append(int(i))

length = 0
max_num = 0
sigma = 0
for i in taget_list:
    length += 1
    sigma += i
    if i > max_num:
        max_num = i

print(f"list:{taget_list}, length:{length}, max:{max_num}, sigma:{sigma}")