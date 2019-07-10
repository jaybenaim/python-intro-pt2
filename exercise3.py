def double(my_number): 
    return my_number * 2

# print(double(3))
# print(double(6))
# print(double(12))
# print(double(24))

def negative(num): 
    if num > 0: 
        return False
    else: 
        return True 

# print(negative(-3))
# print(negative(-32))
# print(negative(32))
# print(negative(3))

def is_even(num): 
    if num % 2 == 0: 
        return True
    else: 
        return False 

# print(is_even(3))
# print(is_even(32))
# print(is_even(21))

def is_string(string): 
    if len(string) < 8: 
        return False 
    else: 
        return True 
# print(is_string("jacob is here"))
# print(is_string("jay"))


