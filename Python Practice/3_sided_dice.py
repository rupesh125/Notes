
import random
rolles = (input("How many times to roll the dice? "))
sides = (input("How many sides does dice have? "))
if sides.isnumeric() and rolles.isnumeric():
    rolles = int(rolles)
    sides  = int(sides)
    while True:
        result = '|'
        for r in range(rolles):
            rand =  random.randint(1,sides)
            result+= f"{rand}|"
        
        print(result)
        reply = input("Roll again? ('q' to quit)")

        if reply == "q":
            break
else:
    print("You have entered invalid character try again")

