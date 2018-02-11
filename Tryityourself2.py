print("Ex:5-8")
usernames = ['saad', 'oj', 'admin', 'ali']
for username in usernames:
    if username == 'admin':
        print("Hello " + username + ",would you like to see a status report?")
    else:
        print("Hello " + username + ",thank you for logging in again. ")

print("Ex:5-9")
users = []
if users:
        for user in users:
            print("Adding " + user + ".")
        print("\nFinished your user data")
else:
        print("We need to find some users!")
print("The End")


print("Ex:5-10")
current_users=['oj','ali','arbaz','rafay','sana']
new_users=['Qb','Ab','oj','ali','sb']
for new_user in new_users:
    if new_user in current_users:
        print(new_user+" Enter a new username")
    else:
        print(new_user+" the username is not available")
print("The EnD")

print("Ex:5-11")
Numbers=['1','2','3','4','5','6','7','8','9']
for number in Numbers:
    if number==str(1):
        print(number+"st")
    else:
        print("Bubye")