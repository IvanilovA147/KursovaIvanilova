class Item:
    def __init__(self, name, quantity, category, price):
        self.name = name
        self.quantity = quantity
        self.category = category
        self.price = price
        self.purchased = False

    def mark_as_purchased(self):
        self.purchased = True

    def __str__(self):
        return f"{'[✔]' if self.purchased else '[ ]'} {self.name} - {self.quantity} шт, {self.category}, {self.price} грн"


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_items_by_name(self, name):
        return [item for item in self.items if item.name.lower() == name.lower()]

    def display_matching_items(self, items):
        for i, item in enumerate(items):
            print(f"{i + 1}. {item}")

    def get_user_index(self, max_index):
        try:
            choice = int(input("Оберіть номер товару: ")) - 1
            if 0 <= choice < max_index:
                return choice
            else:
                print("Невірний номер!")
        except ValueError:
            print("Введено не число!")
        return None

    def update_item(self, name, new_name, new_quantity, new_category, new_price):
        matches = self.find_items_by_name(name)
        if not matches:
            print("Товар не знайдено!")
            return

        self.display_matching_items(matches)
        index = self.get_user_index(len(matches))
        if index is None:
            return

        item = matches[index]
        item.name = new_name
        item.quantity = new_quantity
        item.category = new_category
        item.price = new_price
        print("Товар оновлено!")

    def remove_item(self, name):
        matches = self.find_items_by_name(name)
        if not matches:
            print("Товар не знайдено!")
            return

        self.display_matching_items(matches)
        index = self.get_user_index(len(matches))
        if index is None:
            return

        self.items.remove(matches[index])
        print("Товар видалено!")

    def mark_as_purchased(self, name):
        matches = self.find_items_by_name(name)
        if not matches:
            print("Товар не знайдено!")
            return

        self.display_matching_items(matches)
        index = self.get_user_index(len(matches))
        if index is None:
            return

        matches[index].mark_as_purchased()
        print("Товар позначено як куплений!")

    def filter_by_category(self, category):
        print(f"Товари у категорії: {category}")
        for item in self.items:
            if item.category.lower() == category.lower():
                print(item)

    def sort_items_by_name(self):
        self.items.sort(key=lambda item: item.name.lower())

    def sort_items_by_category(self):
        self.items.sort(key=lambda item: item.category.lower())

    def sort_items_by_price(self):
        self.items.sort(key=lambda item: item.price)

    def display_items(self):
        if not self.items:
            print("Список порожній.")
        for item in self.items:
            print(item)


def main():
    shopping_list = ShoppingList()

    while True:
        print("\n1. Додати товар")
        print("2. Оновити товар")
        print("3. Видалити товар")
        print("4. Позначити товар як куплений")
        print("5. Фільтрувати за категорією")
        print("6. Сортувати (1 - за назвою, 2 - за категорією, 3 - за ціною)")
        print("7. Показати список")
        print("8. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Назва товару: ")
            quantity = int(input("Кількість: "))
            category = input("Категорія: ")
            price = float(input("Ціна: "))
            shopping_list.add_item(Item(name, quantity, category, price))
        elif choice == "2":
            old_name = input("Назва товару для оновлення: ")
            new_name = input("Нова назва: ")
            new_quantity = int(input("Нова кількість: "))
            new_category = input("Нова категорія: ")
            new_price = float(input("Нова ціна: "))
            shopping_list.update_item(old_name, new_name, new_quantity, new_category, new_price)
        elif choice == "3":
            name = input("Назва товару для видалення: ")
            shopping_list.remove_item(name)
        elif choice == "4":
            name = input("Назва товару для позначення: ")
            shopping_list.mark_as_purchased(name)
        elif choice == "5":
            category = input("Категорія для фільтрації: ")
            shopping_list.filter_by_category(category)
        elif choice == "6":
            sort_choice = input("Оберіть спосіб сортування: ")
            if sort_choice == "1":
                shopping_list.sort_items_by_name()
            elif sort_choice == "2":
                shopping_list.sort_items_by_category()
            elif sort_choice == "3":
                shopping_list.sort_items_by_price()
        elif choice == "7":
            shopping_list.display_items()
        elif choice == "8":
            print("Вихід...")
            break
        else:
            print("Невідома команда!")


if __name__ == "__main__":
    main()