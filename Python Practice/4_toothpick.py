player_one = input("Enter player 1's name ")
player_two = input("Enter player 2's name ")

user = player_one
num_left = 13
print(f"There are {num_left} toothpicks left")

while True:
    
    print("| "*num_left)
    
    pick = int(input(f"how many do you take {user} "))
    while pick < 0 or pick > 3:
        pick = int(input(f"how many do you take {user} "))

    num_left -=pick

    if num_left <=0:
        print(f"{user} wins!!!")
        break

    print(f"There are {num_left} toothpicks left")
    
    if user ==player_two:
        user = player_one
    else:
        user = player_two


print("GAME OVER!!")