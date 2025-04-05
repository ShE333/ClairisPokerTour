import os
import json
import player_manager as pm



# Main program
if __name__ == "__main__":
    # Check if the player folder exists, if not create it
    os.makedirs(pm.PLAYER_FOLDER, exist_ok=True)
    
    print("\n\n\n\n\n**** Welcome to Clairis Poker Tour Manager! ****\n")


    while(True):
        print("Que voulez vous faire:\n")
        print("1. Créer un nouveau profile\n")
        print("2. Afficher un profile existant\n")
        print("3. Modifier un profile\n")
        print("4. Supprimer un profile\n")
        print("5. Afficher le tableau des scores\n")
        print("6. Entrer les scores\n")
        print("7. Quitter\n")
        choice = input("Entrez votre choix: \n")


        match choice:
            case "1": # Créer un profile

                pm.create_player_file()
                
                print("\n----------------------------------------------\n")
                continue

            case "2": # Afficher un profile existant

                pm.display_player_file()
                
                print("\n----------------------------------------------\n")
                continue

            case "3": # Modifier un profile

                pm.modify_player_file()

                print("\n----------------------------------------------\n")
                continue

            case "4": # Supprimer un profile
                
                pm.delete_player_file()
                
                print("\n----------------------------------------------\n")
                continue

            case "5": # Afficher le tableau des scores

                pm.display_scoreboard()

                print("\n----------------------------------------------\n")
                continue
            
            case "6": # Entrer les scores

                

                print("\n----------------------------------------------\n")
                continue
            

            case "7": # Quitter

                print("\nMerci d'avoir utilisé Clairis Poker Tour Manager!\n")
                exit()

            case _:
                print("\nChoix invalide. Veuillez réessayer.\n")
                print("\n----------------------------------------------\n")












