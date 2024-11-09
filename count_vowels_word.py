#counting vowels in given word
a="welcome to my python"
v=["a","e","i","o","u"]
count=0
for i in a:
    if i in v:
        count=count+1
print(count)