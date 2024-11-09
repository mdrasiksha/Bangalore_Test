str = "AB150CCS450"
digit=0
for i in str:
    if i.isdigit():
        digit+=int(i)
print(digit)


