product1Name = "Green Tea"
product2Name = "Black Tea"
product3Name = "White Tea"

# print(product1Name)
# print(product2Name)
# print(product3Name)

productNames = ["Green Tea", "Black Tea", "White Tea"]

#  Shortcut to comment out multiple lines: Ctrl + K, C 

# print(productNames[0])
# print(productNames[1])
# print(productNames[2])

# for productName in productNames:
#     print(productName)

# print(productNames[3]) # IndexError: list index out of range

# for i in range(3):
#     print(f"{i+1}. {productNames[i]}")

mixed_list = ["Name", 25]

# for item in mixed_list:
#     print(item)

productNames.append("Brown Tea")
productNames.insert(2, "Yellow Tea")

productNames[0] = "Purple Tea"

# for productName in productNames:
#     print(productName)

# print(len(productNames))
# print(min(productNames))
# print(max(productNames))

# print(productNames[1:4:2])
# print(productNames[::-1])

print("White Tea" in productNames)
print("Orange Tea" not in productNames)