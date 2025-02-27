class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east

def main():
    room_list = []

    # Rooms from 0 to 11
    obstacle_room = Room("A long fall and some platforms separate you from the door ahead.",
                         3,
                         None,
                         1,
                         None)

    room_list.append(obstacle_room)

    entrance = Room("You are in the entry hall, numerous old columns surround you.",
                 4,
                 None,
                 2,
                 0)

    room_list.append(entrance)

    guide_room = Room("You find a talking head, he tells you the treasure room is at the bottom of this dungeon.",
                      5,
                      None,
                      None,
                      1)

    room_list.append(guide_room)

    library = Room("You found a library! All the books are blank, weird.",
                 6,
                 0,
                 4,
                 None)

    room_list.append(library)

    monster_room = Room(
        "There´s a huge dead monster in the center of the room, it looks like someone killed it. The walls are engraved with strange characters.",
        7,
        1,
        5,
        3)

    room_list.append(monster_room)

    button_room = Room("There´s a big red button in the center of the room. You press it, nothing happens.",
                    8,
                    2,
                    None,
                    4)

    room_list.append(button_room)

    stairs_room = Room("This room is empty, only a door lies before you. The words 'DONT GO IN' are written in blood next to it.",
                 None,
                 6,
                 7,
                 None)

    room_list.append(stairs_room)

    labyrinth_e = Room("An enormous room with what seems to be a labyrinth.",
                 9,
                 4,
                 None,
                 None)

    room_list.append(labyrinth_e)

    ghost_room = Room("You feel a dark presence in this room. It makes you really uncomfortable.",
                    None,
                    5,
                    None,
                    7)

    room_list.append(ghost_room)

    labyrinth_9 = Room("You have entered the labyrinth",
                 None,
                 7,
                 10,
                 None)

    room_list.append(labyrinth_9)

    labyrinth_10 = Room("It´s getting dizzy... and dark for sure.",
                 11,
                 None,
                 None,
                 9)

    room_list.append(labyrinth_10)

    labyrinth_11 = Room("There´s a dim light coming in, it might be the exit.",
                 None,
                 10,
                 6,
                 None)

    room_list.append(labyrinth_11)

    # Current room
    current_room = 1
    done = False

    while not done:
        print()
        print(room_list[current_room].description)

        action = ""
        while action.lower != "n" or action.lower != "s" or action.lower != "e" or action.lower != "w":
            action = input("What do you do?: ")

            if not action.lower == "n" or not action.lower == "s" or not action.lower == "e" or not action.lower == "w":
                print()
                print("Sorry, that's not a valid input.")
                print()
main()
