try:
    num1=int(input("enter first number"))
    num2=int(input("enter second number"))
    result = num1//num2
    print(result)

except ZeroDivisionError:
    print("Pass")
except SyntaxError:
    print("fail")
except ValueError:
    print("value error executed")
else:
    print("pass")
finally:
    print("everything cleared ")