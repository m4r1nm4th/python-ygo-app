from card import *
from deck import *
from hand import Hand


def monteCarlo(num_trials, myDeck):
    counter = 0
    matrix = [[0 for _ in range(6)] for _ in range(6)]

    # counter_zero_starter = 0
    # counter_one_starter = 0
    # counter_two_starter = 0
    while( counter < num_trials):
        counter += 1
        myHand = myDeck.drawHand()
        matrix[myHand.numberStarter()][myHand.numberNonEngine()] += 1
        # match myHand.numberStarter():
        #     case 0:
        #         counter_zero_starter += 1
        #     case 1:
        #         counter_one_starter += 1
        #     case 2:
        #         counter_two_starter += 1
    print(matrix)
    # print(f"Zero Starter: {counter_zero_starter}, OneStarter: {counter_one_starter}, TwoStarter: {counter_two_starter}")

def run():
    myDeck = myDeck1()
    monteCarlo(1000000, myDeck)
    # print(myDeck)
    

if __name__ == "__main__":
    run()