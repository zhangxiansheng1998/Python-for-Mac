class Animal(object):
    """动物类"""

    def func(self):
        print('动物发出了声音')


class Cat(Animal):
    """猫类"""

    def func(self):
        print('喵 喵 喵')


class Dog(Animal):
    """狗类"""

    def func(self):
        print('汪 汪 汪 ')


class Hero:
    def func(self):
        print('这个是英雄类的方法，不是动物类的对象')


def work01(musen: Animal):
    musen.func()


work01(Hero())