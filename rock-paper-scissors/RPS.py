import random

def player(prev_play, opponent_history=[]):

    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 2:
        return random.choice(["R", "P", "S"])

    last = opponent_history[-1]
    second_last = opponent_history[-2]

    def counter(move):
        return {"R":"P", "P":"S", "S":"R"}[move]

    if last == second_last:
        return counter(last)

    counts = {
        "R": opponent_history.count("R"),
        "P": opponent_history.count("P"),
        "S": opponent_history.count("S")
    }

    most_common = max(counts, key=counts.get)
    return counter(most_common)
