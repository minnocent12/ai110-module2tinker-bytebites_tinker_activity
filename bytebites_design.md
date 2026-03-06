## ByteBites – UML Class Diagram

```
┌─────────────────────────────────────────┐
│                Customer                 │
├─────────────────────────────────────────┤
│ - name : str                            │
│ - purchase_history : List<Transaction>  │
├─────────────────────────────────────────┤
│ + add_transaction(t: Transaction) : void│
│ + is_verified() : bool                  │
└─────────────────────────────────────────┘
          │ has (0..*)
          ▼
┌─────────────────────────────────────────┐
│              Transaction                │
├─────────────────────────────────────────┤
│ - selected_items : List<FoodItem>       │
├─────────────────────────────────────────┤
│ + add_item(item: FoodItem) : void       │
│ + compute_total() : float               │
└─────────────────────────────────────────┘
          │ contains (1..*)
          ▼
┌─────────────────────────────────────────┐
│               FoodItem                  │
├─────────────────────────────────────────┤
│ - name : str                            │
│ - price : float                         │
│ - category : str                        │
│ - popularity_rating : float             │
└─────────────────────────────────────────┘
          ▲ holds (0..*)
          │
┌─────────────────────────────────────────┐
│                  Menu                   │
├─────────────────────────────────────────┤
│ - items : List<FoodItem>                │
├─────────────────────────────────────────┤
│ + add_item(item: FoodItem) : void       │
│ + get_all_items() : List<FoodItem>      │
│ + filter_by_category(cat: str)          │
│     : List<FoodItem>                    │
└─────────────────────────────────────────┘
```
