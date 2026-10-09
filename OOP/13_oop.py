from Product import Product


# white_tea = Product()
# white_tea.name = "White Tea"
# white_tea.price = 120
# white_tea.quantity = 40
# white_tea.location = "Store A"
# white_tea.weight = 10

white_tea = Product("White Tea", 120, 40, "Store A", 10)

# print(white_tea.weight)
# print(white_tea.is_in_stock())

white_tea.price = 100

white_tea.apply_discount(10)
print(white_tea.price)

white_tea.restock(20)
print(white_tea.quantity)