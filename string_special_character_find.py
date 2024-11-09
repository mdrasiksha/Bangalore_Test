x = "wel$%$%come123"
y=""
z=""
for i in x:
    if i.isnumeric():
        y+=i
    else:
        z+=i
print(z)
