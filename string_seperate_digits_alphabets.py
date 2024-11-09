str1= "wel123come456"
digit=""
alphabets=""
for i in str1:
    if i.isdigit():
        digit+=i
    else:
        alphabets+=i
print(digit)
print(alphabets)

        