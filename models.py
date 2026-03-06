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

    def filter_by_category(self, category: str) -> list[FoodItem]:
        # Return only the items whose category matches 'category'
        return [item for item in self.items if item.category == category]

    def sort_by_price(self) -> list[FoodItem]:
        # Return all items sorted from lowest to highest price
        return sorted(self.items, key=lambda item: item.price)

    def sort_by_popularity(self) -> list[FoodItem]:
        # Return all items sorted from highest to lowest popularity rating
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


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

    def add_transaction(self, transaction: Transaction) -> None:
        # Add a completed transaction to the customer's history
        self.purchase_history.append(transaction)

    def is_verified(self) -> bool:
        # A simple verification rule:
        # Customer must have a name and at least one past transaction
        return bool(self.name) and len(self.purchase_history) > 0