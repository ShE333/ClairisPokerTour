import os
import sys
import json
import subprocess as sp
import time
#import PrettyTable


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
""" def display_scoreboard():

    # Get all player files
    player_files = [f for f in os.listdir(PLAYER_FOLDER) if f.endswith(".json")]

    # Create a list to store player data
    player_data_list = []

    # Read each player file and extract data
    for file in player_files:
        file_path = os.path.join(PLAYER_FOLDER, file)
        with open(file_path, "r", encoding="utf-8") as f:
            player_data = json.load(f)
            player_data_list.append(player_data)

    # Sort the players by their scores (sum of scores)
    sorted_players = sorted(player_data_list, key=lambda x: sum(x["scores"]), reverse=True)

    # Create a PrettyTable object to display the scoreboard
    table = PrettyTable()
    table.field_names = ["Nom", "Prénom", "Scores"]

    # Add each player's data to the table
    for player in sorted_players:
        table.add_row([player["nom"], player["prenom"], player["scores"]])

    print("\nTableau des scores:\n")
    print(table) """