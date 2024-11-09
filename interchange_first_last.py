list=[23,65,99,32]
def swap(list):
    list[0],list[-1]=list[-1],list[0]
    return list
print(swap(list))