text = input()
a_list = []
z_list = []
for i, x in enumerate(text):
    if x == "A":
        a_list.append(i)
    if x == "Z":
        z_list.append(i)

a_z_len = max(z_list) - min(a_list) + 1
print(a_z_len)
