documentary = 'Fyre'
drama = 'Jane the virgin'
comedy = 'Family guy'
dramedy = 'Friends'

which_movie = input("Do you prefer; documentaries, drama, or comedy\n").lower()

if which_movie == 'documentaries': 
    print("You should try watching " + documentary) 
elif which_movie == 'drama and comedy' or which_movie == 'comedy and drama': 
    print("You should try watching " + dramedy)
elif which_movie == 'drama': 
    print("You should try watching " + drama)
elif which_movie == 'comedy': 
    print("You should try watching " + comedy) 
else: 
    print("Maybe you will like the book called: The power of now, by Eckhart Tolle ")
