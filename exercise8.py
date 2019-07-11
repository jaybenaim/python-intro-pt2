
# current_distance = 0  


# def runner(runner_number): 
#     distance = input("How far did person {} run?".format(runner_number))
#     distance = float(distance) 
#     current_distance = distance 

#     return distance 

# def time(person): 
#     time_taken = input("How long (in minutes) did person {} take to run {} metres?".format( current_distance))
#     time_taken = float(time_taken)
#     return time_taken * 60

# def speed():
#     speed = runner() / time() 
#     return speed 

# print(runner(1))
# print(runner(2))
# print(runner(3))

# print(time())

# if speed1 > speed2 and speed > speed():
#   print("Person 3 was the fastest at {} m/s".format(speed()))
# elif speed2 > speed() and speed2 > speed1:
#   print("Person 2 was the fastest at {} m/s".format(speed2))
# elif speed1 > speed() and speed1 > speed2:
#   print("Person 1 was the fastest at {} m/s".format(speed1))
# elif speed1 == speed2 and speed2 == speed():
#   print("Everyone tied at {} m/s".format(speed1))
# else:
#   print("Well done everyone!")


# person_number = 1 

# def print_distance(): 
#     print("How far did person {} run (in metres)?".format(person_number))

#


def dist(person): # ask user how far they ran 
    distance = input("How far did person {} run? (in meters)\n".format(person))
    distance = float(distance) 
    return distance 

def time(person, distance): # ask user how long it took to get there 
    mins = input("How long (in minutes) did person {} take to run {} metres?\n".format(person, distance))
    mins = float(mins) 
    return mins 
    
def calc_speed(distance): # get users speed in m/s 
    seconds = float(distance) * 60 
    speed = float(distance)/seconds 
    return speed 

def display_winner(person, speed): # show winner 
    return "Person {} was the fastest at {:.6f} m/s".format(person, speed)

def find_winner():  # Asks user for inputs and determines winner 
    distance1 = dist(1)
    min1 = time(1, distance1)
    distance2 = dist(2)
    min2 = time(2, distance2)
    distance3 = dist(3)
    min3 = time(3, distance3)

    msec1 = min1 * 60
    msec2 = min2 * 60
    msec3 = min3 * 60

    speed1 = calc_speed(distance1) / msec1
    speed2 = calc_speed(distance2) / msec2 
    speed3 = calc_speed(distance3) / msec3 

    if speed3 > speed2 and speed3 > speed1:
        return display_winner(1, speed3)
    elif speed2 > speed3 and speed2 > speed1:
        return display_winner(1, speed2)
    elif speed1 > speed3 and speed1 > speed2:
        return display_winner(1, speed1)
    elif speed1 == speed2 and speed2 == speed3 and speed1 == speed3:
        return "Everyone tied at {:.6f} m/s".format(speed1)
    else:
        return "Well done everyone!"

print(find_winner())