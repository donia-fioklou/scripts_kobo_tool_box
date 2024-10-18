import os
import requests
import psycopg2
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Obtenir les valeurs depuis le fichier .env
API_TOKEN = os.getenv('API_TOKEN')
ASSET_UID = os.getenv('ASSET_UID')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# URL de l'API pour récupérer les données
url = f'https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/data.json'

# Headers pour l'authentification à l'API KoboToolbox
headers = {
    'Authorization': f'Token {API_TOKEN}'
}

# Requête pour récupérer les données depuis KoboToolbox
response = requests.get(url, headers=headers)

if response.status_code == 200:
    #print('data_api',response.text) # Les données sont au format JSON
    data = response.json() 
    print("Données récupérées avec succès!")
else:
    print(f"Erreur lors de la récupération des données : {response.status_code}")
    exit()

# Connexion à la base de données PostgreSQL
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cur = conn.cursor()

    # Insertion des données dans la table beneficiaries
    for record in data['results']:
        # Récupérer les champs du formulaire (adapte les noms de champs selon ton formulaire)
        nom_beneficiaire = record.get('Nom_du_b_n_ficiaire', None)
        identification = record.get('Num_ro_d_identification_du_b_n_ficiaire', None)
        sexe = record.get('Sexe', None)
        age = record.get('_ge', None)

        # Requête SQL d'insertion
        sql = """
            INSERT INTO beneficiaries (nom_beneficiaire, identification, sexe, age)
            VALUES (%s, %s, %s, %s)
        """
        val = (nom_beneficiaire, identification, sexe, age)

        try:
            cur.execute(sql, val)
            conn.commit()  # Sauvegarder les changements dans la base de données
            print(f"Données insérées pour {nom_beneficiaire}")
        except psycopg2.Error as e:
            print(f"Erreur lors de l'insertion des données: {e}")

    # Fermeture du curseur et de la connexion à la base de données
    cur.close()
    conn.close()

except psycopg2.Error as err:
    print(f"Erreur de connexion à la base de données : {err}")
