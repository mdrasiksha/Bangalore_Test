vowel = ["a","e","i","o","u"]
txt = "programming"
count = 0
for character in txt:
    if character not in vowel:
        count = count+1
print(count)
