#overriding a variable
class parent:
    name="scott"

class child(parent):
    pass

obj=child()
print(obj.name)