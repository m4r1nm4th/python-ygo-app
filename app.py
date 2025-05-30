from deck import myDeck1


def monteCarlo(num_trials, myDeck):
    counter = 0
    matrix = [[0 for _ in range(6)] for _ in range(6)]

    # counter_zero_starter = 0
    # counter_one_starter = 0
    # counter_two_starter = 0
    while (counter < num_trials):
        counter += 1
        myHand = myDeck.drawHand()
        matrix[myHand.numberStarter()][myHand.numberNonEngine()] += 1
    print(matrix)


def run():
    myDeck = myDeck1()
    monteCarlo(1000000, myDeck)


if __name__ == "__main__":
    run()
