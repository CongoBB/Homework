from pprint import pprint


class Product:
    def __init__(self, name, total_weight, category):
        self.name = name
        self.total_weight: float = total_weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.total_weight}, {self.category}'


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r+') as file:
            file.seek(0)
            return file.read()

    def add(self, *products):
        with open(self.__file_name, 'r+') as file:
            for i in products:
                if str(i) in file.read():
                    print(f'{str(i)} уже есть в магазине')
                    file.seek(0)
                    continue
                else:
                    file.write(f'{i}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  

s1.add(p1, p2, p3)

print(s1.get_products())
