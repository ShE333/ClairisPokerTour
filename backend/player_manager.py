import os
import sys
import json
import subprocess as sp
import time
import prettytable as pt


# CONSTANTS
PLAYER_FOLDER = "backend/profiles/"


# PLAYER FILE CREATION
def create_player_file ():
    
    # Ensure the player folder exists
    os.makedirs(PLAYER_FOLDER, exist_ok=True)

    # getting player information
    print("Entrez les informations du joueur.\n") 
    first_name = input("Entrez le prénom: \n")
    last_name = input("Entrez le nom: \n")

    print("Création du profile...\n")

    # Create player data
    player_data = {
        "prenom": first_name,
        "nom": last_name,
        "scores": [0] * 12,
    }

    
    # Create a unique filename for the player
    file_name = f"{first_name}_{last_name}.json"
    file_path = os.path.join(PLAYER_FOLDER, file_name)

    # Check if the file already exists
    if os.path.exists(file_path):
        print("Le fichier existe déjà. Veuillez choisir un autre nom.\n")
        return
    
    
    # Write the player data to a JSON file
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(player_data, file, indent=4)

    print("Le fichier a été créé avec succès.\n")


# PLAYER FILE SELECTOR
def select_player_file():

    print("Liste des profiles de joueurs disponibles:\n")

    # List all player files
    nbr_files = 0
    for file in os.listdir(PLAYER_FOLDER):
        if file.endswith(".json"):
            nbr_files += 1
            print(f"{nbr_files}. {file}\n")


    # Ask for the file number
    nbr = int(input("Entrez le numéro du fichier voulu: \n"))
    while(nbr < 1 or nbr > nbr_files) :
        nbr = input("Numéro de fichier invalide. Veuillez réessayer:\n")

    # Get the selected file name
    selected_file = os.listdir(PLAYER_FOLDER)[nbr - 1]

    return selected_file


# PLAYER FILE DISPLAY
def display_player_file():

    file = select_player_file()
    file_path = os.path.join(PLAYER_FOLDER, file)

    print(f"Affichage du fichier: {file_path}\n")
    
    # Display player data
    with open(file_path, "r", encoding="utf-8") as file:
        player_data = json.load(file)
        print(json.dumps(player_data, indent=4, ensure_ascii=False))

    return

def display_player_file_wpath(file_path):

    print(f"Affichage du fichier: {file_path}\n")
    
    # Display player data
    with open(file_path, "r", encoding="utf-8") as file:
        player_data = json.load(file)
        print(json.dumps(player_data, indent=4, ensure_ascii=False))

    return


# PLAYER FILE MODIFICATION
def modify_player_file():
    
    print("\nSélectionnez le fichier à modifier:\n")
    file = select_player_file()
    file_path = os.path.join(PLAYER_FOLDER, file)

    # Open text editor to modify the file
    print("\nOuverture du fichier dans l'éditeur de texte par défaut...\n")
    sp.Popen(["notepad.exe", file_path])

    # Ask the user to close the editor
    input("\nAppuyez sur 'Entrée' lorsque vous avez terminé de modifier le fichier.\n")
    print("\nFermeture de l'éditeur de texte...\n")


    # Close the editor (if it is still open)
    try:
        sp.Popen(["taskkill", "/F", "/IM", "notepad.exe"])

    except Exception as e:
        print(f"Erreur lors de la fermeture de l'éditeur de texte: {e}")
    
    time.sleep(3)


# PLAYER FILE DELETION
def delete_player_file():

    print("Sélectionnez le fichier à supprimer:\n")
    file = select_player_file()
    file_path = os.path.join(PLAYER_FOLDER, file)

    # Make sure it is the right file to delete
    print("\n")
    display_player_file_wpath(file_path)
    selection = input("Etes-vous sur de vouloir supprimer ce fichier? Cette action est irréversible (o/n)\n")

    match selection:
        case "O" | "o":
            print(f"\nSuppression du fichier: {file_path}\n")

            # Delete the player file
            os.remove(file_path)

            print("\nLe fichier a été supprimé avec succès.\n")
            return
        
        case "N" | "n":
            print("\nAucune action effectuée. Abandon de la suppression\n")
            return
        

        case _:
            print("\nSélection invalide. Aucune action effectuée.\n")
            return


# SCOREBOARD DISPLAY
def display_scoreboard():

    # Create the scoreboard table
    scoreboard = pt.PrettyTable()
    
    scoreboard.field_names = ["Prénom", "Nom", "Tournois n°1", "Tournois n°2", "Tournois n°3", "Tournois n°4", "Tournois n°5", "Tournois n°6", "Tournois n°7", "Tournois n°8", "Tournois n°9", "Tournois n°10", "Tournois n°11", "Tournois n°12"]
    
    scoreboard.align["Prénom"] = "l"
    scoreboard.align["Nom"] = "l"
    
    scoreboard.align["Tournois n°1"] = "c"
    scoreboard.align["Tournois n°2"] = "c"
    scoreboard.align["Tournois n°3"] = "c"
    scoreboard.align["Tournois n°4"] = "c"
    scoreboard.align["Tournois n°5"] = "c"
    scoreboard.align["Tournois n°6"] = "c"
    scoreboard.align["Tournois n°7"] = "c"
    scoreboard.align["Tournois n°8"] = "c"
    scoreboard.align["Tournois n°9"] = "c"
    scoreboard.align["Tournois n°10"] = "c"
    scoreboard.align["Tournois n°11"] = "c"
    scoreboard.align["Tournois n°12"] = "c"
    
    scoreboard.title = "Tableau des scores des joueurs"

    # Fill the scoreboard with player data
    for file in os.listdir(PLAYER_FOLDER):
        if file.endswith(".json"):
            with open(os.path.join(PLAYER_FOLDER, file), "r", encoding="utf-8") as f:
                player_data = json.load(f)
                first_name = player_data["prenom"]
                last_name = player_data["nom"]

                score1 = player_data["scores"][0]
                score2 = player_data["scores"][1]
                score3 = player_data["scores"][2]
                score4 = player_data["scores"][3]
                score5 = player_data["scores"][4]
                score6 = player_data["scores"][5]
                score7 = player_data["scores"][6]
                score8 = player_data["scores"][7]
                score9 = player_data["scores"][8]
                score10 = player_data["scores"][9]
                score11 = player_data["scores"][10]
                score12 = player_data["scores"][11]


                scoreboard.add_row([first_name, last_name, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10, score11, score12], divider=True)

    # Print the scoreboard
    print(scoreboard)