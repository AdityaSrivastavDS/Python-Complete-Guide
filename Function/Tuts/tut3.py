friends = ["Rahul", "Rohit", "Raj", "Ravi", "Rajesh"]

def add_friend():
    friend_name = input("Enter friend name: ")
    f = friends + [friend_name]
    print(f)

add_friend()