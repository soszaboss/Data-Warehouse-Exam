# Data Warehouse Exam

## Prérequis

- Python 3.11+
- PostgreSQL (ou SQLite pour test)
- MinIO (pour le stockage objet)
- Docker & Docker Compose

## Installation locale

1. **Cloner le dépôt**
   ```bash
   git clone <votre-url-git>
   cd examen_entrepot
   ```
2. **Créer et activer un environnement virtuel**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. **Installer les dépendances**
   ```powershell
   pip install -e .
   ```

## Utilisation avec Docker

1. **Construire et lancer les services**
   ```bash
   docker-compose build
   docker-compose up
   ```
   Cela démarre PostgreSQL, MinIO et exécute automatiquement le pipeline ETL via le service `app`.

2. **Structure du service Docker**
   - Les fichiers CSV sont téléchargés depuis la plateforme dans `app/utils/download.py`.
   - Ils sont directement insérés dans les buckets MinIO depuis ce même fichier.
   - Les données sont ensuite injectées dans la base PostgreSQL : le script lit les fichiers, nettoie avec pandas et insère via SQLAlchemy en une seule méthode optimisée.

## Workflow du projet

1. **Téléchargement des données**
   - Les fichiers CSV sont récupérés depuis des URLs externes.
   - Ils sont stockés localement dans le dossier `app/data/`.

2. **Upload sur MinIO**
   - Les fichiers sont envoyés dans le bucket MinIO `inflation-data` via le SDK Python.

3. **Injection dans la base de données**
   - Les fichiers sont lus avec pandas.
   - Nettoyage et harmonisation des colonnes.
   - Insertion dans la base PostgreSQL via SQLAlchemy (méthode optimisée, sans boucle).

## Configuration de l'environnement

Créez un fichier `.env` à la racine du projet ou dans `app/` avec :

```
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/nom_de_votre_db
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=your-access-key
MINIO_SECRET_KEY=your-secret-key
MINIO_BUCKET=inflation-data
```

## Lancement avec Docker

Pour exécuter le pipeline ETL avec Docker :

1. **Construire l’image et lancer les services**
   ```bash
   docker-compose build --no-cache app
   docker-compose up
   ```

2. **Le service `app` lance automatiquement le script d’insertion**
   - Le script principal (`run_insert.py`) est exécuté dès le démarrage du conteneur.
   - Les fichiers CSV sont téléchargés, envoyés sur MinIO, puis injectés dans la base PostgreSQL.

3. **Pour relancer le pipeline manuellement**
   - Arrête les services :
     ```bash
     docker-compose down
     ```
   - Relance le pipeline :
     ```bash
     docker-compose up app
     ```

**Remarque :**  
- Toutes les dépendances et configurations sont gérées automatiquement dans le conteneur.
- Vérifie les logs du service `app` pour suivre l’avancement du pipeline.

---

Ajoute cette section après "Lancement du pipeline ETL" pour clarifier l’utilisation avec Docker.## Lancement avec Docker

Pour exécuter le pipeline ETL avec Docker :

1. **Construire l’image et lancer les services**
   ```bash
   docker-compose build
   docker-compose up
   ```

2. **Le service `app` lance automatiquement le script d’insertion**
   - Le script principal (`run_insert.py`) est exécuté dès le démarrage du conteneur.
   - Les fichiers CSV sont téléchargés, envoyés sur MinIO, puis injectés dans la base PostgreSQL.

3. **Pour relancer le pipeline manuellement**
   - Arrête les services :
     ```bash
     docker-compose down
     ```
   - Relance le pipeline :
     ```bash
     docker-compose up app
     ```

**Remarque :**  
- Toutes les dépendances et configurations sont gérées automatiquement dans le conteneur.
- Vérifie les logs du service `app` pour suivre l’avancement du pipeline.

---

## Lancement du pipeline ETL en local

- **En local** :  
  ```powershell
  eltfire
  ```
- **Avec Docker** :  
  Le pipeline s’exécute automatiquement au démarrage du service `app`.

## Dépendances principales

- SQLAlchemy
- Alembic
- psycopg
- pandas
- minio
- typer/click

## Conseils

- Toujours activer l'environnement virtuel avant toute commande locale.
- Adapter le fichier `.env` à votre environnement.
- Pour toute migration, bien vérifier la cohérence entre les modèles et la base.

---

## Auteurs
- Kamal Moussa MOUSTOIFA BEN
-  Juste Aimé Vianney ZEHBIKA NDONG
-   Mouhamadou Bamba Kane
