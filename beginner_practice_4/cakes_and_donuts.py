N = int(input())

cake_price = 4
donut_price = 7

match_tf = "No"
for c in range(N//4+1):
    for d in range(N//7+1):
        if c * cake_price + d * donut_price == N:
            match_tf = "Yes"

print(match_tf)
