import sys
import pandas as pd
import util
import combat

cont = True

if (len(sys.argv) <= 1):
    print("Please include a configuration file.")
    cont = False
else:
    config_file = sys.argv[1]
    if config_file.endswith(".csv"):
        enemy_df = pd.read_csv(config_file, index_col=False)
    elif config_file.endswith(".xlsx") or config_file.endswith(".xls"):
        enemy_df = pd.read_csv(config_file, index_col=False)
    else:
        print("Invalid configuration file format. Valid file formats: .csv, .xlsx, .xls")
        cont = False
    
    if cont and enemy_df.empty:
        # TODO check that this properly catches data with incorrect path, format, etc
        print("Error reading config file.")
        cont = False

        if enemy_df.columns != ["name","code","type","AC","HP","str_mod","dex_mod","con_mod","int_mod","wis_mod","cha_mod","PB","attack1_name","attack1_mod","attack1_dmg","attack2_name","attack2_mod","attack2_dmg","attack3_name","attack3_mod","attack3_dmg"]:
            print("Incorrect data columns. Please check your column headers or use a template.")
            cont = False

while cont:
    usr_in = input("Please select an option: \n1. View combatants\n2. View enemy stats\n3. Set initiative\n4. Begin combat\n5. Exit\n")

    match usr_in:
        case "1":
            util.print_combatants(enemy_df)
        case "2":
            # TODO print all enemy stats
            print("Wip")
        case "3":
            init_df = util.initiative(enemy_df)
        case "4":
            # TODO begin combat
            print("Wip")
        case "5":
            cont = False
        case _:
            print("Invalid input. Please enter a number 1-5.")

