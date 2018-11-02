text = input()
new_text_li = []
for i in range(len(text)):
    if i % 2 == 0:
        new_text_li.append(text[i])

new_text = "".join(new_text_li)
print(new_text)
