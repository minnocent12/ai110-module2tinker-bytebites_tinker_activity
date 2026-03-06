# ByteBites Tinker Activity – Tech Fellow Summary

## The Core Concept Students Needed to Understand

The most important concept in this assignment was learning how to Tackle down all the features request and turn it into a clear system design using classes `(OOD:object-oriented design)`. We had to identify the main objects in the system, like `Customer`, `Menu`, `FoodItem`, and `Transaction`, and understand how they relate to each other. Once the design was clear in the UML diagram, implementing the code became much easier because each class had a clear role.


## Where Students Are Most Likely to Struggle

Students will probably struggle the most with deciding which class should handle certain behaviors. For example, it can be confusing at first to figure out that filtering and sorting should happen in the Menu class because it manages the list of `FoodItem` objects. Another challenge is translating the UML diagram into code without adding extra features that were not part of the specification.

## Where AI Was Helpful vs. Misleading

AI was helpful for generating initial ideas for the class structure and helping draft method implementations. It also helped review code and suggest improvements like adding type hints or making comments clearer. However, sometimes AI suggested adding new features or methods that were not required, so it was important to check that everything still matched the original design.

## One Way to Guide a Student Without Giving the Answer

If a student is stuck, I would ask them which class owns the data they are trying to work with. Looking back at the UML diagram usually helps identify where a method should belong. This helps the student think through the design instead of just giving them the solution directly.
