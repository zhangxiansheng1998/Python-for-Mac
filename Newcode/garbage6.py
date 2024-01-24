class ParentClass:
    def __init__(self):
        self.parent_attribute = "Parent attribute"

    def parent_method(self):
        print("Parent method")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # 调用父类的构造函数
        self.child_attribute = "Child attribute"

    def child_method(self):
        print("Child method")

# 创建子类对象
child = ChildClass()
parent = ParentClass()
print(parent.parent_attribute)
print(parent.parent_method())
print(child.parent_method())
print(child.child_method())
