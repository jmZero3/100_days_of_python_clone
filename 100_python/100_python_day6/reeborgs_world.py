def turn_right():
    turn_left()
    turn_left()
    turn_left()
 

    

while not at_goal():
    while not wall_on_right():
        turn_right()
        move()
        if front_is_clear() and right_is_clear():
            turn_right()
            if front_is_clear():
                move()
                break
        
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
    else:
        turn_left()


# ! angelas solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()

turn_left()

while not at_goal():

    if right_is_clear():
        turn_right()
        move()

    elif front_is_clear():
        move()
    
    else:
        turn_left()
