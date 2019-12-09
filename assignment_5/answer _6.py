"""
Answer # 6
Suppose a customer is shopping in a market and you need to print all the items
which user bought from market.
Write a function which accepts the multiple arguments of user shopping list and
print all the items which user bought from market.
(Hint: Arbitrary Argument concept can make this task ease)
"""



def boughtITEM():
    cart = []
    while True:                                  
        carts = input("\nEnter an item to add it in your cart: \nor Press [ENTER] to finish: \n")
        if carts == "":
            break
        cart.append(carts)
    item_list = ""
    for item in range(0,len(cart)):
        item_list = item_list + cart[item].title() + "\n"
    print("\nItems you have bought is:\n"+item_list)

boughtITEM()