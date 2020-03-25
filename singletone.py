class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

a = Singleton()
print("Создание обьекта", a)
b = Singleton()
print("Создание обьекта", b)