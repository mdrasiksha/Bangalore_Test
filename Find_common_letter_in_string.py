def common_letter():
    str1 = input("enter first name")
    str2 = input("enter second name")
    s1=set(str1)
    s2=set(str2)
    li = s1 & s2
    print(li)
common_letter()