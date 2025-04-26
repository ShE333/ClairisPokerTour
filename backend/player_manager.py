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
    print("\nEntrez les informations du joueur.\n") 
    first_name = input("Entrez le prénom: (Appuyez sur ENTR pour annuler)\n")
    if first_name == "":
        print("Création du profile annulée.\n")
        return
    last_name = input("\nEntrez le nom: (Appuyez sur ENTR pour annuler)\n")
    if last_name == "":
        print("Création du profile annulée.\n")
        return

    print("\nCréation du profile...\n")

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

    print("\nListe des profiles de joueurs disponibles:\n")

    # List all player files
    nbr_files = 0
    for file in os.listdir(PLAYER_FOLDER):
        if file.endswith(".json"):
            nbr_files += 1
            print(f"{nbr_files}. {file}\n")


    # Ask for the file number or press enter to cancel
    if nbr_files == 0:
        print("Aucun fichier de joueur trouvé.\n")
        return
    
    if nbr_files == 1:
        print("Il n'y a qu'un seul fichier de joueur disponible.\n")
        return os.listdir(PLAYER_FOLDER)[0]
    
    else:

        nbr = int(input("Entrez le numéro du fichier voulu: (Entrez 0 (zéro) pour annuler)\n"))
        if nbr == 0:
            print("Sélection annulée.\n")
            return
        while(nbr < 1 or nbr > nbr_files) :
            nbr = input("\nNuméro de fichier invalide. Veuillez réessayer:\n")




    # Get the selected file name
    selected_file = os.listdir(PLAYER_FOLDER)[nbr - 1]

    return selected_file


# PLAYER FILE DISPLAY
def display_player_file():

    file = select_player_file()
    file_path = os.path.join(PLAYER_FOLDER, file)

    print("\n")
    print(f"Affichage du fichier: {file_path}\n")
    
    # Display player data
    with open(file_path, "r", encoding="utf-8") as file:
        player_data = json.load(file)
        print(json.dumps(player_data, indent=4, ensure_ascii=False))

    return

def display_player_file_wpath(file_path):

    print("\n")
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


# CALCULATE BEST 6 SCORES
def best_6_scores(scores):
    # Sort the scores in descending order
    sorted_scores = sorted(scores, reverse=True)
    
    # Calculate the sum of the best 6 scores
    best_6_sum = sum(sorted_scores[:6])
    
    return best_6_sum

# SCOREBOARD DISPLAY
def display_scoreboard():

    # Create the scoreboard table
    scoreboard = pt.PrettyTable()
    
    scoreboard.field_names = ["Prénom",
                              "Nom", 
                              "Tour 1", 
                              "Tour 2", 
                              "Tour 3", 
                              "Tour 4", 
                              "Tour 5", 
                              "Tour 6", 
                              "Tour 7", 
                              "Tour 8", 
                              "Tour 9", 
                              "Tour 10", 
                              "Tour 11", 
                              "Tour 12",
                              "Total",
                              "6 Bests"]


    # Sort the scoreboard by total score in descending order
    scoreboard.sortby = "6 Bests"
    scoreboard.reversesort = True

    scoreboard.align["Prénom"] = "l"
    scoreboard.align["Nom"] = "l"
    
    scoreboard.align["Tour 1"] = "c"
    scoreboard.align["Tour 2"] = "c"
    scoreboard.align["Tour 3"] = "c"
    scoreboard.align["Tour 4"] = "c"
    scoreboard.align["Tour 5"] = "c"
    scoreboard.align["Tour 6"] = "c"
    scoreboard.align["Tour 7"] = "c"
    scoreboard.align["Tour 8"] = "c"
    scoreboard.align["Tour 9"] = "c"
    scoreboard.align["Tour 10"] = "c"
    scoreboard.align["Tour 11"] = "c"
    scoreboard.align["Tour 12"] = "c"
    scoreboard.align["Total"] = "c"
    scoreboard.align["6 Bests"] = "c"
    
    scoreboard.title = "Tableau des scores des joueurs"


    # Fill the scoreboard with player data
    for file in os.listdir(PLAYER_FOLDER):
        if file.endswith(".json"):
            with open(os.path.join(PLAYER_FOLDER, file), "r", encoding="utf-8") as f:
                player_data = json.load(f)
                first_name = player_data["prenom"]
                last_name = player_data["nom"]

                scores = player_data["scores"]
                score1, score2, score3, score4, score5, score6, score7, score8, score9, score10, score11, score12 = scores

                total_player = sum(player_data["scores"])
                bests_6 = best_6_scores(player_data["scores"])


                scoreboard.add_row([first_name, last_name, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10, score11, score12, total_player, bests_6])

                # add divider line between players
                scoreboard.add_divider()

    # Print the scoreboard
    print(scoreboard)


# SCORE ENTRY
def enter_scores():

    print("\n")
    tournament_dates = [
        "26/04/2025", "10/05/2025", "07/06/2025", "12/07/2025",
        "30/08/2025", "13/09/2025", "25/10/2025", "08/11/2025",
        "20/12/2025", "17/01/2026", "28/02/2026", "14/03/2026"
    ]


    for i, date in enumerate(tournament_dates, start=1):
        print(f" {i}. {date}")
    

    selected_date = int(input("\nSélectionnez la date du tournoi:\n"))

    # Iterate over all player files to modify the score corresponding to the selected date
    for file in os.listdir(PLAYER_FOLDER):
        if file.endswith(".json"):
            file_path = os.path.join(PLAYER_FOLDER, file)

            # Display the player data before modification
            print("\n")
            display_player_file_wpath(file_path)

            # Open the player file to modify the score
            with open(file_path, "r+", encoding="utf-8") as f:
                player_data = json.load(f)
                print("\nEntrez le score du joueur:\n")
                score = int(input(f"Score pour {player_data['prenom']} {player_data['nom']}:\n"))

                # Update the score for the selected tournament
                player_data["scores"][selected_date - 1] = score

                # Write the updated data back to the file
                f.seek(0)  # Move the cursor to the beginning of the file
                json.dump(player_data, f, indent=4, ensure_ascii=False)
                f.truncate()  # Remove any leftover data from the old file


