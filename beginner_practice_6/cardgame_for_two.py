N = int(input())
cards_num = [int(x) for x in input().split(' ')]

cards_num.sort(reverse=True)

bob = []
alice = []

for j in range(len(cards_num)):
    if j % 2 == 0:
        bob.append(cards_num[j])
    else:
        alice.append(cards_num[j])

print(sum(bob)-sum(alice))