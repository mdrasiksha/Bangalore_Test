#check string contain any special charcter
import re
str="welcome to my world"
regex=re.compile('[%,#]')
if regex.search(str)==None:
    print("not present")
else:
    print("present")