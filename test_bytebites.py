from models import FoodItem, Menu, Transaction, Customer


# --- Menu.filter_by_category ---

def test_filter_by_category_returns_matching_items():
    menu = Menu()
    menu.add_item(FoodItem("Burger", 8.99, "Main", 4.5))
    menu.add_item(FoodItem("Soda", 1.99, "Drinks", 3.8))
    menu.add_item(FoodItem("Water", 0.99, "Drinks", 3.0))

    results = menu.filter_by_category("Drinks")

    assert len(results) == 2
    assert all(item.category == "Drinks" for item in results)


def test_filter_by_category_excludes_other_categories():
    menu = Menu()
    menu.add_item(FoodItem("Burger", 8.99, "Mains", 4.5))
    menu.add_item(FoodItem("Soda", 1.99, "Drinks", 3.8))

    results = menu.filter_by_category("Mains")

    assert len(results) == 1
    assert results[0].name == "Burger"


def test_filter_by_category_returns_empty_for_missing_category():
    menu = Menu()
    menu.add_item(FoodItem("Burger", 8.99, "Mains", 4.5))

    results = menu.filter_by_category("Desserts")

    assert results == []


# --- Menu.sort_by_price ---

def test_sort_by_price_orders_lowest_to_highest():
    menu = Menu()
    menu.add_item(FoodItem("Burger", 8.99, "Mains", 4.5))
    menu.add_item(FoodItem("Water", 0.99, "Drinks", 3.0))
    menu.add_item(FoodItem("Soda", 1.99, "Drinks", 3.8))

    result = menu.sort_by_price()

    assert result[0].price == 0.99
    assert result[1].price == 1.99
    assert result[2].price == 8.99


def test_sort_by_price_does_not_modify_original_list():
    menu = Menu()
    menu.add_item(FoodItem("Burger", 8.99, "Mains", 4.5))
    menu.add_item(FoodItem("Water", 0.99, "Drinks", 3.0))

    menu.sort_by_price()

    assert menu.items[0].name == "Burger"


# --- Menu.sort_by_popularity ---

def test_sort_by_popularity_orders_highest_to_lowest():
    menu = Menu()
    menu.add_item(FoodItem("Burger", 8.99, "Mains", 4.5))
    menu.add_item(FoodItem("Water", 0.99, "Drinks", 3.0))
    menu.add_item(FoodItem("Soda", 1.99, "Drinks", 3.8))

    result = menu.sort_by_popularity()

    assert result[0].popularity_rating == 4.5
    assert result[1].popularity_rating == 3.8
    assert result[2].popularity_rating == 3.0


# --- Transaction.compute_total ---

def test_compute_total_empty_transaction_returns_zero():
    t = Transaction()

    assert t.compute_total() == 0.0


def test_compute_total_single_item():
    t = Transaction()
    t.add_item(FoodItem("Burger", 8.99, "Mains", 4.5))

    assert t.compute_total() == 8.99


def test_compute_total_multiple_items():
    t = Transaction()
    t.add_item(FoodItem("Burger", 8.99, "Mains", 4.5))
    t.add_item(FoodItem("Soda", 1.99, "Drinks", 3.8))
    t.add_item(FoodItem("Water", 0.99, "Drinks", 3.0))

    assert t.compute_total() == 11.97


# --- Customer.is_verified ---

def test_is_verified_no_transactions_returns_false():
    customer = Customer("Alice")

    assert customer.is_verified() == False


def test_is_verified_with_one_transaction_returns_true():
    customer = Customer("Alice")
    t = Transaction()
    t.add_item(FoodItem("Burger", 8.99, "Mains", 4.5))
    customer.add_transaction(t)

    assert customer.is_verified() == True


def test_is_verified_empty_name_returns_false():
    customer = Customer("")
    t = Transaction()
    t.add_item(FoodItem("Burger", 8.99, "Mains", 4.5))
    customer.add_transaction(t)

    assert customer.is_verified() == False
