s, t = map(input().split())

tf = []
for i in range(0, len(s)-1):
    if s[i] == t[i]:
        tf.append(True)
    else:
        break


if s[:len(s)] == t[:len(s)] and len(s) < len(t):
    print("Yes")
elif s[:len(tf)-1] == t[:len(tf)-1] and s[len(tf)] < t[len(tf)]:
    print("Yes")
else:
    print("No")