import random

def monty_hall_simulation(num_simulations):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_simulations):
        # Randomly place the car behind one of the three doors
        doors = ["goat", "goat", "car"]
        random.shuffle(doors)

        # Contestant's initial choice
        initial_choice = int(input("0,1,2"))

        # Find the door Monty Hall can reveal (which has a goat)
        for i in range(3):
            if i != initial_choice and doors[i] == "goat":
                opened_door = i
                break

        # Contestant decides whether to switch or stay
        for i in range(3):
            if i != initial_choice and i != opened_door:
                switch_choice = i
                break

        # Check if the contestant wins with the initial choice
        if doors[initial_choice] == "car":
            stay_wins += 1

        # Check if the contestant wins by switching
        if doors[switch_choice] == "car":
            switch_wins += 1

    return stay_wins, switch_wins

num_simulations = 10000
stay_wins, switch_wins = monty_hall_simulation(num_simulations)



