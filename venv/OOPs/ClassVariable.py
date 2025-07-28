class MyExample:
    students=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        MyExample.students+=1
s1 = MyExample("yaseen",12)
s2=MyExample("bghadawa", 123)
print(MyExample.students)
