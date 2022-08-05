import random
existing_passwords = []

integers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'q', 'x', 'y', 'z']
specials = ['!', '@', '#', '$', '%', '&']
capitals = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

def generatePassword():
    password = ''
    password_list = []
    for i in range(3):
        capital = chr(random.choice(capitals))
        special = random.choice(specials)
        password_list.append(capital)
        password_list.append(special)
    for i in range(5):
        integer = random.choice(integers)
        password_list.append(integer)
    for i in range(9):
        lower = random.choice(lowers)
        password_list.append(lower)
    random.shuffle(password_list)
    for i in range(len(password_list)):
        password+= str(password_list[i])
    if password in existing_passwords:
        generatePassword()
    return password