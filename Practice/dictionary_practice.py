# Define dictionary with correct key names (use quotes for keys)
dic = {"Name": ["Aditya", "Mahir", "Rahul", "Sakshi", "Ishika"],
       "Age": [20, 19, 22, 19, 20],
       "College": ["BBDU", "IIT Delhi", "BBDU", "BHU", "AIIMS Delhi"]}


def search_name(name):
    """Searches for a student's name in the dictionary and prints their information.

    Args:
        name (str): The name of the student to search for.

    Returns:
        None
    """

    for i in range(len(dic["Name"])):
        if name == dic["Name"][i]:
            print("Name found!")
            print("Age:", dic["Age"][i])
            print("College:", dic["College"][i])
            return  # Exit the function after finding the name
    print("Name not found.")

# Get user input
name = input("Enter the name of student: ")

# Call the function
search_name(name)