films = {
    # age and ticket number
    "Avengers Endgame": [18, 5],
    "The Lion King": [18, 3],
    "Captain Marvel": [15, 5],
    "Aladdin": [12, 5],
    "Hobbs & Shaw": [13, 5]

}
while True:

    choice = input("What film would you like to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: "))

        # check user age
        if age > films[choice][0]:

            # check enough seat
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out")
        else:
            print("You are too young to wat the film")
    else:
        print("We dont't have that film")
