import pandas as pd
import random
import warnings

warnings.filterwarnings("ignore")

def print_combatants(enemy_df):
    # TODO make this nicer
    print(enemy_df)

def print_enemies_short(enemy_df):
    print_str = ""
    for i in enemy_df.index:
        print_str+=enemy_df["code"][i]+"  "
    print("Enemies:", print_str)

def initiative(enemy_df):
    print_enemies_short(enemy_df)

    init_df = pd.DataFrame(columns=["code","roll","order","bonus"])

    init_in = input("Would you like to auto-generate enemy initiative? Y/N\n")
    if (init_in.lower() == "y"):
        for i in enemy_df.index:
            roll = random.randint(1,20)
            init_df.loc[len(init_df)] = [enemy_df["code"][i], roll+enemy_df["dex_mod"][i], 0, (1 if roll == 20 else (-1 if roll ==1 else 0))]
    while init_in.lower() != "e":
        init_in = input("Enter initiative in format \"Code/Name roll\". Enter \"20*\" for nat 20 and \"1*\" for nat 1. Enter \"e\" to exit.\n")
        if init_in.lower() != "e":
            init = init_in.split(" ")
            if len(init) != 2 or not init[1].strip("*").isdigit():
                print("Invalid input.")
            else:
                init_roll = int(init[1].strip("*"))
                if init[0].lower() in init_df["code"].apply(str.lower).values:
                    # overwriting existing initiative
                    check = input("This will overwrite initiative for "+init[0]+" are you sure you would like to proceed? Y/N\n")
                    if check.lower() == "y":
                        loc = init_df.loc[init_df["code"] == init[0]].index[0]
                        init_df["roll"][loc] = init_roll
                        if "*" in init[1]:
                            init_df["bonus"][loc] = 1 if init_roll >= 20 else -1
                else:
                    if "*" in init[1]:
                        bonus = 1 if init_roll >= 20 else -1
                    else: 
                        bonus = 0
                    init_df.loc[len(init_df)] = [init[0], init_roll, 0, bonus]
    # TODO handle ties
    init_df["order"] = init_df["roll"].loc[init_df["bonus"]==0].rank(method="max")
    # TODO handle ties
    init_df["order"].loc[init_df["bonus"] == 1] = 0
    init_df["order"] = init_df["order"].apply(lambda x : x+1)
    # TODO handle ties
    init_df["order"].loc[init_df["bonus"] == -1] = len(init_df)

    init_df = init_df.sort_values(by=["order"])
    print(init_df)
    return init_df
