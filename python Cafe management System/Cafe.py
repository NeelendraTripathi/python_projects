print("\n\n!!***************** [!!-- WELCOME TO NTR CAFE -- !!] **********************!!")
#Cafe Menu
menu ={
    "pizza":120,
    "burger":100,
    "coffee":70,
    "salad":50,
    "samosa":30,
    "tea":20,
    "ice creme":90
}

print("\tPlease Choose the Items :!")
print("\tPizza:Rs 120\n\tBurger:Rs 100\n\tCoffee:Rs 70\n\tSalad:Rs 50\n\tSamosa:Rs 30\n\tTea:Rs 20\n\tIce Cream:Rs 90 ")
total_order= 0
item_1 =input("Enter the item you want to order= ")
if item_1 in menu:
    total_order +=menu[item_1]
    print(f"Your item {item_1} has been added to your order ")
else:
    print(f"Ordered item {item_1} not availble yet !")
another_item =input("Do you want to add another item ?(YES/No):")
if another_item == "Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        total_order+= menu[item_2]
        print(f"Item {item_2} has been added to your order ")
    else:
        print(f"Oredr item {item_2} not avaialable !")
print("\n\tTHANK YOU FOR ORDER:")
print(f"The total amount of items to pay is Rs:{total_order} \n")