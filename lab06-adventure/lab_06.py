import time


class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east

def main():
    room_list = []

    # Rooms
    # 0
    obstacle_room = Room("A long fall and some platforms separate you from the door ahead.",
                         3,
                         None,
                         1,
                         None)

    room_list.append(obstacle_room)

    # 1
    entrance = Room("You are in the entry hall, numerous old columns surround you.",
                 4,
                 None,
                 2,
                 0)

    room_list.append(entrance)

    # 2
    guide_room = Room("You find a talking head, he tells you the treasure room is at the bottom of this dungeon. There is a door to the north",
                      5,
                      None,
                      None,
                      1)

    room_list.append(guide_room)

    # 3
    library = Room("You found a library! All the books are blank, weird. There is a door to the east",
                 None,
                 0,
                 4,
                 None)

    room_list.append(library)

    # 4
    monster_room = Room(
        "A huge dead monster lies in the center of the room, it looks like someone killed it. The walls are engraved with strange characters.",
        7,
        1,
        5,
        3)

    room_list.append(monster_room)

    # 5
    button_room = Room("There´s a big red button in the center of the room. You can press it, but you don´t know what it does.",
                    8,
                    2,
                    None,
                    4)

    room_list.append(button_room)

    # 6
    stairs_room = Room("This room is empty, only a door lies before you. The words 'DONT GO IN' are written in blood next to it. There´s also a slide behind you, to the south.",
                 12,
                 3,
                 11,
                 None)

    room_list.append(stairs_room)

    # 7
    labyrinth_e = Room("An enormous room with what seems to be a labyrinth lying ahead.",
                 9,
                 4,
                 None,
                 None)

    room_list.append(labyrinth_e)

    # 8
    ghost_room = Room("You feel a dark presence in this room. It makes you really uncomfortable. Just walk through the door at your left or behind you.",
                    None,
                    5,
                    None,
                    7)

    room_list.append(ghost_room)

    # 9
    labyrinth_9 = Room("You have entered the labyrinth",
                 None,
                 7,
                 10,
                 None)

    room_list.append(labyrinth_9)

    # 10
    labyrinth_10 = Room("It´s getting dizzy... and dark for sure.",
                 11,
                 None,
                 None,
                 9)

    room_list.append(labyrinth_10)

    # 11
    labyrinth_11 = Room("There´s a dim light coming in, it might be the exit.",
                 None,
                 10,
                 None,
                 6)

    room_list.append(labyrinth_11)

    # 12
    treasure_room = Room("",
                         None,
                         None,
                         None,
                         None)

    room_list.append(treasure_room)

    # Variables
    current_room = 1
    done = False
    pushed = False
    opened = False
    game_over = False
    again = True

    # Set mode
    mode = ""
    room_counter = None
    while mode != "normal" and mode != "hard":
        print("Normal | Hard")
        mode = input("Select mode: ")
        mode = mode.lower()
        if mode == "normal":
            room_counter = -100000000
            print("Normal mode selected.")
            print("No penalties will be applied.")
        elif mode == "hard":
            room_counter = 0
            print()
            print("Hard mode selected.")
            print("Moving between rooms will have a penalty. Once a certain number of penalties have been reached, the game will end.")
        else:
            print("Invalid mode.")

    # Game loop
    while again:
        while not (done or game_over):
            print()
            print(room_list[current_room].description)

            # Checks if button is pushed
            ans2 = ["y", "n", "yes", "no"]
            if current_room == 5 and pushed == False:
                activate = False
                while activate not in ans2:
                    activate = input("Do you want to push it?: ")
                    activate = activate.lower()
                    if activate == "y" or activate == "yes":
                        pushed = True
                        opened = True
                        time.sleep(1)
                        print("That was a loud noise, something like a mechanism, where did it come from?")
                    elif activate == "n" or activate == "no":
                        pushed = False
                    else:
                        print()
                        print("Sorry, that's not a valid input.")

            # Checks if the door is locked
            if current_room == 6 and opened == False:
                print("Looks like the door is locked. You try pushing it, achieving nothing.")
            elif current_room == 6 and opened == True:
                print("You find stairs. It´s a very long way down but, when you make it, you only find one door.")
                time.sleep(1)
                print("You open it.")
                time.sleep(1)
                print("It´s the treasure room, you made it!")
                print()
                done = True


            # Player input
            action = ""
            ans = ["n", "s", "e", "w", "north", "south", "east", "west"]
            next_room = None
            while action.lower() not in ans or next_room is None:
                if not done and not game_over:
                    print()
                    action = input("What do you do?: ")
                    action = action.lower()

                    if action not in ans:
                        print()
                        print("Sorry, that's not a valid input.")

                    # Direction triggers
                    else:
                        if action == "n" or action == "north":
                            next_room = room_list[current_room].north
                            if next_room is None:
                                print()
                                print("There´s nowhere to go that way.")
                            else:
                                current_room = next_room
                            room_counter += 1

                        elif action == "s" or action == "south":
                            next_room = room_list[current_room].south
                            if next_room is None:
                                print()
                                print("There´s nowhere to go that way.")
                            else:
                                current_room = next_room
                            room_counter += 1

                        elif action == "e" or action == "east":
                            next_room = room_list[current_room].east
                            if next_room is None:
                                print()
                                print("There´s nowhere to go that way.")
                            else:
                                current_room = next_room
                            room_counter += 1

                        elif action == "w" or action == "west":
                            next_room = room_list[current_room].west
                            if next_room is None:
                                print()
                                print("There's nowhere to go that way.")
                            else:
                                current_room = next_room
                            room_counter += 1

                        else:
                            print()
                            print("That´s not a verb I understand.")

                        if room_counter > 10:
                            game_over = True
                else:
                    break

        if done:
            current_room = 1
        elif game_over:
            print()
            print("You starved to death.")
            print("Game over.")
            current_room = 1

        again_input = None
        while again_input != "y" and again_input != "n" and again_input != "yes" and again_input != "no":
            again_input = input("Play again?: ")
            again_input = again_input.lower()
            if again_input == "y" or again_input == "yes":
                again = True
                done = False
                game_over = False
                if mode == "normal":
                    room_counter = -100000000
                elif mode == "hard":
                    room_counter = 0
            elif again_input == "n" or again_input == "no":
                again = False
            else:
                print()
                print("Sorry, that's not a valid input.")

main()