cars =['audi','bmw','subaru','toyota']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())



requested_topping ='mashrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")


answer =17
if answer !=42:
    print("That is not correct amswer,Please try again!")


banned_users =['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(user.title()+ ",you can post a response if you wish.")


age=17
if age>=18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


age1=12
if age1 <4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")



age2=22
if age <4:
    price=0
elif age <18:
    price=5
else:
    price=10
print("Your admission cost is $" +str(price) +".")


age3=12
if age3<4:
    price=0
elif age3<18:
    price=5
elif age3<65:
    price=10
elif age3>=65:
    price=5
print("Your admission cost is $" + str(price)+".")

requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
