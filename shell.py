import core

from time import sleep


def gladiator():
    print("----THE HAVOC STADIUM----")

    print("....setting up the game....")

    gladiator_1 = core.new_gladiator(100, 0, 10, 50)
    gladiator_2 = core.new_gladiator(100, 0, 5, 60)

    # print("*GLADIATOR 1*")
    while True:
        message = input(
            "**Before you start, choose your armor to battle with: \n *The Enclosed Helmet![1] \n *The Pavise Shield![2] \n *The Girdle of MIGHT![3] \n"
        ).strip()
        if message == 'The Enclosed Helmet' or message == '1':
            print("You have chosen the mighty ",
                  core.armor('helmet' ['Enclosed Helmet']))
            break

    print("*GLADIATOR 1*")
    while True:  # whole game play loop
        if core.is_dead(gladiator_1):
            print("Gladiator 1 has died, always in our hearts.")
            print("~~~GLADIATOR 2 WINS~~~")
            break

        while True:  # everything dealing with gladiator 1s turn
            print('Gladiator 1:', gladiator_1['health'], "HP", "||",
                  gladiator_1['rage'], "Rage")
            print("Gladiator 2:", gladiator_2['health'], "HP", "||",
                  gladiator_2['rage'], "Rage")

            response = input(
                "What would you lke to do? \n >> [a]ttack \n >> [p]ass \n >> [q]uit \n >> [h]eal \n  "
            ).strip().lower()
            if response == 'attack' or response == 'a':
                core.attack(gladiator_1, gladiator_2)
                print("You attacked Player 2, their health is now decreased!")
                print("Player 2's Health:", gladiator_2['health'])
                break
            elif response == 'pass' or response == 'p':
                print("You have passed to Gladiator 2!")
                break
            elif response == 'quit' or response == 'q':
                print("Hope you come to battle later!!")
                print("***QUITTING***")
                return
            elif response == 'heal' or response == 'h':
                core.heal(gladiator_1)
                print("You have healed your health!")
                print("Player 1's Current Health:", gladiator_1['health'])
            else:
                print("Invalid choice, pick a valid choice to fight!!")
        if core.is_dead(gladiator_2):
            print("~~~GLADIATOR 1 WINS~~~")
            print("Gladiator 2 has died, always in our hearts.")
            break

        print("-----------------------------------")
        print("*GLADIATOR 2*")
        print('Gladiator 1:', gladiator_1['health'], "HP", "||",
              gladiator_1['rage'], "Rage")
        print("Gladiator 2:", gladiator_2['health'], "HP", "||",
              gladiator_2['rage'], "Rage")

        while True:  # everything with the second glads turn
            response = input(
                "What would you lke to do? \n >> [a]ttack \n >> [p]ass \n >> [q]uit \n >> [h]eal \n  "
            ).strip().lower()
            if response == 'attack' or response == 'a':
                core.attack(gladiator_2, gladiator_1)
                print("You attacked Player 1, their health is now decreased!")
                print("Player 1's Health:", gladiator_1['health'])
                print("*GLADIATOR 1*")
                break
            elif response == 'pass' or response == 'p':
                print("You have passed to Gladiator 1!")
                print("*GLADIATOR 1*")
                break
            elif response == 'quit' or response == 'q':
                print("Hope you come to battle later!!")
                print("***QUITTING***")
                return
            elif response == 'heal' or response == 'h':
                core.heal(gladiator_1)
                print("You have healed your health!")
                print("Player 2's Current Health:", gladiator_2['health'])
                print("*GLADIATOR 1*")
            else:
                print("Invalid choice, pick a valid choice to fight!!")

            #print("*GLADIATOR 1*")


def main():
    # gladiator()
    sleep(2)
    print("             What lies behind us")
    print("                  and what lies before us")
    print("                     are small matters;")
    print("                         compared to what lies within us..")

    print('''                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`''')

    sleep(2)

    gladiator()


if __name__ == '__main__':
    main()
