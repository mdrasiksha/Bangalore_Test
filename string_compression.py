compress_string = "aaabbccdd"
compressed = ""
count = 1
for i in range(1,len(compress_string)):
    if compress_string[i] == compress_string[i-1]:
        count+=1
        print(count)
    else:
        compressed += compress_string[i-1] + str(count)
        print(compressed)

