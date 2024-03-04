name = '张三'  # 全局变量


class Info():

    weight = '52KG'  # 类变量

    def __init__(self):
        self.age_value = None
        self.age_range = None
        self.his = None
        self.be = '是'  # __init__实例变量

    def age(self):
        self.age_value = '18'  # 实例变量

    def sex(self):
        sex_type = '男生'  # 局部变量
        return sex_type   # 如果没有return返回值的话，就会返回None

    def combine(self):
        self.age()
        self.his=name+self.be+self.age_value
        # return self.his
        print(self.his)


if __name__ == '__main__':

    print(name)     # 全局变量的调用
    print(Info.weight)     # 类变量的调用
    print(Info().be)     # __init__实例变量的调用
    Info().combine()    # 实例变量的调用


