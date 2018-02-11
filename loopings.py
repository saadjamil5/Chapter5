requested_toppings=['mushroom','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print("Adding "+requested_topping+".")
print("\nFinished making your pizza!")



requested_toppings1=['mushroom','green peppers','extra cheese']
for requested_topping1 in requested_toppings1:
    if requested_topping1=='green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding "+requested_topping1+".")
print("\nFinished making your pizza!")


requested_topping2=[]
if requested_topping2:
    for requested_topping3 in requested_topping2:
        print("Adding "+ requested_topping3+".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plan pizza?")

available_toppings=['mashrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings3=['mashrooms','BBQ','extra cheese']
for requested_topping4 in requested_toppings3:
    if requested_topping4 in available_toppings:
        print("Adding "+requested_topping4+".")
    else:
        print("Sorry,we don't have "+requested_topping4+".")
print("\nFinished making your pizza!")
