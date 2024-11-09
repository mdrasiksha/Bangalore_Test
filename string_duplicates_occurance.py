txt = "welcomewelcome"
for i in set(txt):
    count=txt.count(i)
    if count > 1:
        print(f"{i}:{count}")
    