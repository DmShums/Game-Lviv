import game_lviv as game

kozelnytska = game.Room("Kozelnytska street")
kozelnytska.set_description("Kozelnytska street. A lovely UCU campus that is full of students")

stryjska = game.Room("Stryjska street")
stryjska.set_description("Stryjska street. Suspicious district where you can find either batyars or kavalers")

stryjskyi_park = game.Room("Stryjskyi park")
stryjskyi_park.set_description("Stryjskyi park. Nice park full of students and kavalers")

krakivska = game.Room("Krakivska street")
krakivska.set_description("Krakivska street. Dangerous district where you can find either batyars or laydaks")

kozelnytska.link_room(stryjska, "south")
stryjska.link_room(kozelnytska, "north")
stryjska.link_room(krakivska, "west")
stryjska.link_room(stryjskyi_park, "east")
stryjskyi_park.link_room(stryjska, "west")
krakivska.link_room(stryjska, "east")

# Stryjska - Batiar
batyar_vasyl = game.Batyar("Vasyl", "A tempting batyar")
batyar_vasyl.set_conversation("Hey sweetheart. Let's have a walk.")
batyar_vasyl.set_weakness("broom") # cheese broom
stryjska.set_character(batyar_vasyl)

# Krakivska - Laydak
oles = game.Enemy("Oles", "A homeless person that can hit you")
oles.set_conversation("Give me some beer...")
oles.set_weakness("beer") # book beer
krakivska.set_character(oles)

# Stryjsky park - Kavaler
gentleman_petro = game.Kavaler("Petro", "Nice and polite gentleman")
gentleman_petro.set_conversation("Nice to meet you. Do you need a help?")
stryjskyi_park.set_support(gentleman_petro)

# Kozelnytska - Student
student_dmytro = game.Student("Dmytro", "Responsible and social student")
student_dmytro.set_conversation("Nice to meet you. Do you need a help?")
kozelnytska.set_support(student_dmytro)

broom = game.Item("broom")
broom.set_description("Long heavy broom of babcia Halia")
krakivska.set_item(broom)

beer = game.Item("beer")
beer.set_description("A bottle of Lviv's beer")
stryjska.set_item(beer)

current_room = kozelnytska
backpack = []

dead = False

while dead == False:
    print("")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    elif command == "help":
        current_room.get_support()
    else:
        print("I don't know how to " + command)
