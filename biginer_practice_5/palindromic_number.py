A, B = map(int, input().split(" "))

total_palindromic = 0
for i in range(A, B+1):
    if str(i)[0] == str(i)[-1] and str(i)[1] == str(i)[-2]:
        total_palindromic += 1

print(total_palindromic)