import core


def gladiator():
    print("----THE HAVOC STADIUM----")
    print("....setting up the game....")
    gladiator_1 = core.new_gladiator(100, 0, 10, 50)
    gladiator_2 = core.new_gladiator(100, 0, 5, 60)

    print("*GLADIATOR 1*")
    while True:  # whole game play loop
        if core.is_dead(gladiator_1):
            print("!GLADIATOR 2 WINS!")
            break
        if core.is_dead(gladiator_2):
            print("!GLADIATOR 1 WINS!")
            break

        while True:  # everything dealing with gladiator 1s turn
            print('Gladiator 1:', gladiator_1['health'], "HP", "||",
                  gladiator_1['rage'], "Rage")
            print("Gladiator 2:", gladiator_2['health'], "HP", "||",
                  gladiator_2['rage'], "Rage")

            response = input(
                "What would you lke to do? \n >> attack \n >> pass \n >> quit \n >> heal \n  "
            ).strip().lower()
            if response == 'attack':
                core.attack(gladiator_1, gladiator_2)
                print("Player 2's Health:", gladiator_2['health'])
                break
            elif response == 'pass':
                break
            elif response == 'quit':
                return
            elif response == 'heal':
                core.heal(gladiator_1)
                print("Player 1's Current Health:", gladiator_1['health'])
            else:
                print("Invalid choice, pick a valid choice to fight!!")
        print("*GLADIATOR 2*")
        print('Gladiator 1:', gladiator_1['health'], "HP", "||",
              gladiator_1['rage'], "Rage")
        print("Gladiator 2:", gladiator_2['health'], "HP", "||",
              gladiator_2['rage'], "Rage")

        while True:  # everything with the second glads turn
            response = input(
                "What would you lke to do? \n >> attack \n >> pass \n >> quit \n >> heal \n  "
            ).strip().lower()
            if response == 'attack':
                core.attack(gladiator_2, gladiator_1)
                print("Player 1's Health:", gladiator_1['health'])
                break
            elif response == 'pass':
                break
            elif response == 'quit':
                return
            elif response == 'heal':
                core.heal(gladiator_1)
                print("Player 2's Current Health:", gladiator_2['health'])
            else:
                print("Invalid choice, pick a valid choice to fight!!")

        print("*GLADIATOR 1*")


def main():
    gladiator()


if __name__ == '__main__':
    main()
