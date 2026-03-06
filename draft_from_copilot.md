## ByteBites – UML Class Diagram


┌─────────────────────────────────────┐
│              Customer               │
├─────────────────────────────────────┤
│ - name: String                      │
│ - purchase_history:List<Transaction>│
├─────────────────────────────────────┤
│ + add_transaction(t): void          │
│ + is_verified(): bool               │
└─────────────────────────────────────┘
              │
              │ has (0..*)
              ▼
┌─────────────────────────────────────┐
│             Transaction             │
├─────────────────────────────────────┤
│ - selected_items: List<FoodItem>    │
├─────────────────────────────────────┤
│ + add_item(item): void              │
│ + compute_total(): float            │
└─────────────────────────────────────┘
              │
              │ contains (1..*)
              ▼
┌─────────────────────────────────────┐
│              FoodItem               │
├─────────────────────────────────────┤
│ - name: String                      │
│ - price: float                      │
│ - category: String                  │
│ - popularity_rating: float          │
└─────────────────────────────────────┘
              ▲
              │ holds (0..*)
              │
┌───────────────────────────────────────────┐
│               Menu                        │
├───────────────────────────────────────────┤
│ - items: List<FoodItem>                   │
├───────────────────────────────────────────┤
│ + add_item(item): void                    │
│ + get_all_items(): List<FoodItem>         │
│ + filter_by_category(cat):List<FoodItem>  │
└───────────────────────────────────────────┘