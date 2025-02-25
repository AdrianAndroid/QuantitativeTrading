# 定义基类
class Animal:
    def speak(self):
        pass


# 定义子类 Dog，继承自 Animal 类
class Dog(Animal):
    def speak(self):
        return "Woof!"


# 定义子类 Cat，继承自 Animal 类
class Cat(Animal):
    def speak(self):
        return "Meow!"


# 定义一个函数，接受一个 Animal 类型的对象
def animal_sound(animal):
    return animal.speak()


# 创建 Dog 和 Cat 的实例
dog = Dog()
cat = Cat()

# 调用 animal_sound 函数，传入不同的对象
print(animal_sound(dog))
print(animal_sound(cat))
