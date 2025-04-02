import os
import json

PLAYER_FOLDER = "backend/profiles/"



def create_player_file (first_name, last_name):
    
    # Ensure the player folder exists
    os.makedirs(PLAYER_FOLDER, exist_ok=True)

    # Create player data
    player_data = {
        "prenom": first_name,
        "nom": last_name,
        "scores": [0] * 12,
    }

    # Define the file path
    player_file_name = f"{first_name}_{last_name}.json"
    file_path = os.path.join(PLAYER_FOLDER, player_file_name)

    # Check if the file already exists
    if os.path.exists(file_path):
        return "Le fichier existe déjà."
    
    # Write the player data to a JSON file
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(player_data, file, indent=4)

    return "Le fichier a été créé avec succès."




def modify_player_file(first_name, last_name):
    # Define the file path
    player_file_name = f"{first_name}_{last_name}.json"
    file_path = os.path.join(PLAYER_FOLDER, player_file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        return "Le fichier n'existe pas."

    # Read the existing data
    with open(file_path, "r", encoding="utf-8") as file:
        player_data = json.load(file)

    # Update the scores
    player_data["scores"] = scores

    # Write the updated data back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(player_data, file, indent=4)

    return "Le fichier a été modifié avec succès."







print("Hello World!")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Creating player file...")
create_player_file(first_name, last_name)

