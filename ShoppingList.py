import tkinter as tk
from tkinter import messagebox


window = tk.Tk()


class ShoppingList:

    def __init__(self, window):

        self.window = window
        self.window.title('Список покупок')
        self.recipes = {}  # здесь будем хранить рецепты
        self.existing_products = {} # а здесь - имеющиеся продукты


        # Поля для ввода данных
        tk.Label(window, text='Название блюда:').pack()
        self.entry_recipe_name = tk.Entry(window, width=50)
        self.entry_recipe_name.pack()

        tk.Label(window, text='Название ингредиента:').pack()
        self.ingredient_name = tk.Entry(window, width=25)
        self.ingredient_name.pack()

        tk.Label(window, text='Количество (г/мл/шт):').pack()
        self.ingredient_quantity = tk.Entry(window, width=25)
        self.ingredient_quantity.pack()

        tk.Button(window, text='Добавить ингредиент', command=self.add_ingredient).pack(pady=10)


        # Ввод имеющихся продуктов
        tk.Label(window, text='Название продукта:').pack()
        self.existing_product = tk.Entry(window, width=25)
        self.existing_product.pack()

        tk.Label(window, text='Количество (г/мл/шт):').pack()
        self.existing_product_quantity = tk.Entry(window, width=25)
        self.existing_product_quantity.pack()

        tk.Button(window, text='Добавить имеющийся продукт', command=self.set_existing_products).pack(pady=10)


        # Сам список покупок
        self.button_get_shopping_list = tk.Button(window,
                                                  text='Получить список покупок',
                                                  command=self.get_shopping_list)
        self.button_get_shopping_list.pack()

        self.text_area = tk.Text(window, width=40, height=15)
        self.text_area.pack(padx=10, pady=10)


        # список сохраненных рецептов
        tk.Label(window, text='Сохраненные рецепты:').pack()
        self.recipes_area = tk.Text(window, width=40, height=10, state='disabled')  #disabled
        self.recipes_area.pack(pady=10)


        # список имеющихся продуктов
        tk.Label(window, text='Имеющиеся продукты:').pack()
        self.existing_area = tk.Text(window, width=40, height=10, state='disabled')
        self.existing_area.pack(pady=10)


    def add_ingredient(self):
        ingredient_name = self.ingredient_name.get().strip()  #strip - для удаления лишних пробелов по краям
        quantity = self.ingredient_quantity.get().strip()

        if not ingredient_name or not quantity:
            messagebox.showwarning('Предупреждение',
                                   'Пожалуйста, введите название ингредиента и количество.', icon='error')
            return

        try:
            quantity_ = float(quantity)
            if quantity_ <= 0:
                raise ValueError('Количество должно быть положительным числом.')

            # Добавление ингредиента в рецепт
            recipe_name = self.entry_recipe_name.get().strip()
            if recipe_name not in self.recipes:
                self.recipes[recipe_name] = {}
            self.recipes[recipe_name][ingredient_name] = quantity_

            # Очистка полей ввода
            self.ingredient_name.delete(0, tk.END)
            self.ingredient_quantity.delete(0, tk.END)

            messagebox.showinfo('Информация',
                                f'Ингредиент "{ingredient_name}" добавлен к рецепту "{recipe_name}".')
            self.update_recipes_area()  # Обновить список рецептов
        except ValueError:
            messagebox.showerror('Ошибка', 'Количество должно быть числом')


    def set_existing_products(self):
        product_name = self.existing_product.get().strip()
        quantity = self.existing_product_quantity.get().strip()

        if not product_name or not quantity:
            messagebox.showwarning('Предупреждение',
                                   'Пожалуйста, введите название продукта и количество.')
            return

        try:
            quantity_float = float(quantity)
            if quantity_float < 0:
                raise ValueError('Количество должно быть положительным числом.')

            # добавляем продукты, которые уже есть
            self.existing_products[product_name] = quantity_float
            self.existing_product.delete(0, tk.END)  # очищаем поле ввода
            self.existing_product_quantity.delete(0, tk.END)

            messagebox.showinfo('Информация', f'Продукт "{product_name}" сохранён.')
            self.update_existing_area()  # Обновляем список
        except ValueError:
            messagebox.showerror('Ошибка', 'Количество должно быть числом')

    def get_shopping_list(self):
        shopping_list = {}
        for ingredients in self.recipes.values():
            for item, quantity in ingredients.items():
                needed_quantity = quantity - self.existing_products.get(item, 0)
                if needed_quantity > 0:
                    shopping_list[item] = shopping_list.get(item, 0) + needed_quantity

        self.text_area.delete(1.0, tk.END)  # Очистить текстовое поле перед выводом нового списка

        if shopping_list:
            self.text_area.insert(tk.END, 'Что нужно купить:\n')
            for item, quantity in shopping_list.items():
                self.text_area.insert(tk.END, f'{item}: {quantity} г/мл/шт\n')
        else:
            self.text_area.insert(tk.END, 'Все нужные продукты уже есть!')

    def update_recipes_area(self):
        self.recipes_area.config(state='normal')     # включение редактирования
        self.recipes_area.delete(1.0, tk.END)  # удаление всего текста из поля
        for recipe_name, ingredients in self.recipes.items():
            self.recipes_area.insert(tk.END, f'Рецепт: {recipe_name}\n')
            for ingredient, quantity in ingredients.items():
                self.recipes_area.insert(tk.END, f'  - {ingredient}: {quantity} г/мл/шт\n')
            self.recipes_area.insert(tk.END, '\n')
        self.recipes_area.config(state='disabled')   # отключение редактирования

    def update_existing_area(self):
        self.existing_area.config(state='normal')    # аналогично предыдущему методу
        self.existing_area.delete(1.0, tk.END)
        for product_name, quantity in self.existing_products.items():
            self.existing_area.insert(tk.END, f'{product_name}: {quantity} г/мл/шт\n')
        self.existing_area.config(state='disabled')


app = ShoppingList(window)
window.mainloop()