menu =  {
    "popcorn":5.00,
    "cola":3,
    "Rice":4,
    "noodle":4,
    "fries":4,
    "nachos":2
}

cart=[]
total=0
print("---------menu----------")
for key,value in menu.items():
    print(f" {key:10} : ${value:.2f}")
print("-----------------------")
while(True):
    food = input("Select an item from menu (q to quit):  ").lower()
    if (food=="q"):
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total=+menu.get(food)