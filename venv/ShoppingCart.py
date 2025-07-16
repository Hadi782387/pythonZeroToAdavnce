foods=[]
prices=[]
total=0

while(True):
    food = input("Enter what you want to purchase (q for quit): ")
    if food=='q':
        break
    else:
        price=float(input(f"Enter price your {food}$: "))
        foods.append(food)
        prices.append(price)
print("_______________You Cart___________")
for food in foods:
    print(food,end=" ")
for price in prices:
    total+=price
    print(total)
print(f"your total is {total}")
