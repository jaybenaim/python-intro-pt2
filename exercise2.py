documentary = 'Fyre'
drama = 'Jane the virgin'
comedy = 'Family guy'
dramedy = 'Friends'


rate_doc = input("Rate documentaries between 1 and 5\n").lower() 
rate_doc = int(rate_doc)  

rate_drama = input("Rate dramas between 1 and 5\n").lower()
rate_drama = int(rate_drama)

rate_comedy = input("Rate comedies between 1 and 5\n").lower()
rate_comedy = int(rate_comedy)


if rate_doc >= 4: 
    print("You should try watching " + documentary) 
elif rate_doc <=3 and rate_comedy >= 4 and rate_drama >= 4:
    print("You should try watching " + dramedy)
elif rate_drama >= 4: 
    print("You should try watching " + drama)
elif rate_comedy >= 4:
    print("You should try watching " + comedy)
elif rate_comedy <= 3 and rate_doc <= 3 and rate_drama <= 3:
    if rate_comedy > rate_doc and rate_comedy > rate_drama: 
        print(comedy)
    elif rate_doc > rate_comedy and rate_doc > rate_drama:
        print(documentary) 
    elif rate_drama > rate_comedy and rate_drama > rate_doc: 
        print(drama)
    else: 
        print("Maybe you will like the book called: The power of now, by Eckhart Tolle ")

else: 
    print("Maybe you will like the book called: The power of now, by Eckhart Tolle ")
