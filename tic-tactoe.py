
# Author AGIPARE EMMANUEL.
# TIC-TAC-TOE game disigned to for two players who are represented by an 'X' and 'Y'

from pickle import APPEND


def main():
    player = ""
    show = create_grid()
    while not (win(show) or draw(show)):
        display_grid(show)
        choices(player, show)
    display_grid(show)
    print("Good game")

def create_grid():
   box = []
   for container in range (9):
       container.append(box + 1)
   return box 

def display_grid(box):
    print()
    print(box[0])|print(box[1])|print(box[2])
    print(box[3])|print(box[4])|print(box[5])
    print(box[6])|print([7])|print([8])
    print()


def choices(player, box):
    Container = int(input(f"{player}'s turn to choose a square (1-9): "))
    box[Container - 1] = player
    if player == "" or player == "o":
        return "x"
    elif player == "x":
        return "o"

def draw(box):
    for container in range(9):
        if box[container] != "x" and box[container] != "o":
            return False
    True

def win(box):
    return (box[0] == box[1] == box[2] or
            box[3] == box[4] == box[5] or
            box[6] == box[7] == box[8] or
            box[0] == box[3] == box[6] or
            box[1] == box[4] == box[7] or
            box[2] == box[5] == box[8] or
            box[0] == box[4] == box[8] or
            box[2] == box[4] == box[6])

if __name__ == "__main__":
    main()
