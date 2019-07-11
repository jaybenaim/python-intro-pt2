#Exercise 7

def how_far(person_id): #Asks user for input and returns distance in metres.
    print('How far did person {} run (in metres)?'.format(person_id))
    return float(input())

def how_long(person_id, distance): #Asks user for input and returns time in minutes.
    print('How long (in minutes) did it take person {} to run {} metres?'.format(person_id, distance))
    return float(input())

def get_speed(min, distance): #Takes time and distance and returns speed.
    return round((distance / (min * 60)),4)

def display_winner(person_id, speed): #Returns a string that displays winner id and their speed.
    return 'Person {} was the fastest at {} m/s.'.format(person_id, speed)

def test_runners(): #Asks user how far each runner went, how long it took, and returns a string that displays the winner.
    distance1 = how_far(1)
    mins1 = how_long(1, distance1)
    speed1 = get_speed(mins1, distance1)

    distance2 = how_far(2)
    mins2 = how_long(2, distance2)
    speed2 = get_speed(mins2, distance2)

    distance3 = how_far(3)
    mins3 = how_long(3, distance3)
    speed3 = get_speed(mins3, distance3)

    if (speed1 > speed2) and (speed1 > speed3):
        return display_winner(1, speed1)
    elif (speed2 > speed1) and (speed2 > speed3):
        return display_winner(2, speed2)
    elif (speed3 > speed1) and (speed3 > speed2):
        return display_winner(3, speed3)
    elif (speed1 == speed2) and (speed2 == speed3):
        return "Everyone tied at {} m/s.".format(speed1)
    else:
        print("Well done everyone!")
    
    
print(test_runners())