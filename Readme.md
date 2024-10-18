
# KoboToolbox et PostgreSQL

Ce projet permet de récupérer les données de formulaires depuis l'API **KoboToolbox** et de les insérer dans une base de données **PostgreSQL**. Le projet utilise Python et exploite les bibliothèques `requests`, `psycopg2`, et `dotenv` pour gérer les connexions à l'API, le traitement des données et l'insertion dans la base de données.

## Fonctionnalités

- Récupération des données via l'API KoboToolbox.
- Insertion automatique des données dans une table PostgreSQL.
- Gestion des informations sensibles (comme les tokens API) via un fichier `.env`.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.x**
- **PostgreSQL**
- Les bibliothèques Python suivantes :
  - `requests`
  - `psycopg2`
  - `python-dotenv`

Vous pouvez installer ces bibliothèques via `pip` :

```bash
pip install requests psycopg2 python-dotenv
```

## Installation

1. Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/donia-fioklou/scripts_kobo_tool_box.git
cd scripts_kobo_tool_box
```

2. Créez un fichier `.env` dans le répertoire principal pour stocker vos informations sensibles :

```bash
touch .env
```

3. Remplissez le fichier `.env` avec vos informations d'API KoboToolbox et PostgreSQL :

```
API_TOKEN=ton_api_token_kobotoolbox
ASSET_UID=ton_asset_uid
DB_HOST=localhost
DB_NAME=nom_de_ta_base
DB_USER=ton_utilisateur
DB_PASSWORD=ton_mot_de_passe
```

4. Créez une table PostgreSQL pour stocker les données récupérées. Voici un exemple de script SQL pour créer la table :

```sql
CREATE TABLE beneficiaries (
    id SERIAL PRIMARY KEY,
    nom_beneficiaire VARCHAR(255),
    identification VARCHAR(100),
    sexe VARCHAR(10) CHECK (sexe IN ('homme', 'femme', 'Autre')),
    age INT CHECK (age >= 0)
);
```

## Utilisation

Une fois que tout est configuré, vous pouvez exécuter le script pour récupérer les données depuis KoboToolbox et les insérer dans la base de données PostgreSQL.

```bash
python main.py
```

Le script va :
- Se connecter à l'API KoboToolbox et récupérer les données du formulaire spécifié.
- Insérer les réponses dans la table PostgreSQL.

## Structure du projet

```
├── .env               # Contient les variables d'environnement sensibles (non inclus dans le repo)
├── README.md          # Ce fichier
├── main.py            # Script principal pour l'extraction et l'insertion des données
└── requirements.txt   # Liste des dépendances Python
```


