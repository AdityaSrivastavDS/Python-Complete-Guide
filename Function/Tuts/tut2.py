def user_age_in_seconds():
    user_age = int(input("Enter as your age: "))
    age_seconds = user_age *365 *24 *60 *60
    print(f"Your age in seconds is {age_seconds}")

user_age_in_seconds()