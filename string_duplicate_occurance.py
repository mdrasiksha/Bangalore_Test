txt="welcomewelcome"
for i in set(txt):
    total=txt.count(i)
    print(total)
    if total > 1:
        print(f"{i}:{total}")