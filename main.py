def fight_soldiers(soldier_one, soldier_two):

    soldier_one_dps = soldier_dps(soldier_one)
    soldier_two_dps = soldier_dps(soldier_two)

    if soldier_one_dps > soldier_two_dps:
        winner= "soldier 1 wins"
    
    elif soldier_two_dps > soldier_one_dps:
        winner= "soldier 2 wins"
    
    else:
        winner= "both soldiers die"

    return winner, soldier_one_dps, soldier_two_dps

def soldier_dps(soldier_dict):
    return soldier_dict["damage"] * soldier_dict["attacks_per_second"]