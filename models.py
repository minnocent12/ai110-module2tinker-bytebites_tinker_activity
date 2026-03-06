# ByteBites Models
# This file defines the core classes used in the ByteBites food ordering system.
#
# FoodItem      → represents a menu item (name, price, category, popularity)
# Menu          → stores all available FoodItems and allows filtering
# Transaction   → represents a single order containing multiple FoodItems
# Customer      → represents a user and stores their purchase history


class FoodItem:
    # Represents a single food item on the menu
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        # Store basic information about the item
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    # Represents the full menu of food items
    def __init__(self):
        # List that will store FoodItem objects
        self.items = []

    def add_item(self, item: FoodItem) -> None:
        # Add a new FoodItem to the menu
        self.items.append(item)

    def get_all_items(self) -> list[FoodItem]:
        # Return a copy of the list of all items
        return self.items[:]

    def filter_by_category(self, cat: str) -> list[FoodItem]:
        # Return only the items whose category matches 'cat'
        return [item for item in self.items if item.category == cat]


class Transaction:
    # Represents a single order placed by a customer
    def __init__(self):
        # List of FoodItems selected for this order
        self.selected_items = []

    def add_item(self, item: FoodItem) -> None:
        # Add a FoodItem to the transaction
        self.selected_items.append(item)

    def compute_total(self) -> float:
        # Compute the total price of all items in the transaction
        return sum(item.price for item in self.selected_items)


class Customer:
    # Represents a user of the ByteBites app
    def __init__(self, name: str):
        # Customer name
        self.name = name
        # List storing past Transaction objects
        self.purchase_history = []

    def add_transaction(self, t: Transaction) -> None:
        # Add a completed transaction to the customer's history
        self.purchase_history.append(t)

    def is_verified(self) -> bool:
        # A simple verification rule:
        # Customer must have a name and at least one past transaction
        return bool(self.name) and len(self.purchase_history) > 0