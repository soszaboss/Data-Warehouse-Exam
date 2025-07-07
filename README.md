# Data Warehouse Exam fait par Kamal Moustoifa Ben et Mouhamadou Bamba Kane

Projet d'examen d'entrepôt de données : ingestion, stockage, migration et traitement de données économiques (inflation, consommation, etc.) avec Python, SQLAlchemy, Alembic, MinIO et PostgreSQL.

## Prérequis

- Python 3.11+
- PostgreSQL (ou SQLite pour test)
- MinIO (pour le stockage objet)
- [pip](https://pip.pypa.io/en/stable/)

## Installation

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

## Configuration de l'environnement

Créer un fichier `.env` à la racine du projet (ou dans `app/` selon votre structure) avec le contenu suivant :

```
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/nom_de_votre_db
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=your-access-key
MINIO_SECRET_KEY=your-secret-key
MINIO_BUCKET=inflation-data
```

Adaptez les valeurs à votre configuration.

## Migration de la base de données

1. **Initialiser Alembic (si ce n'est pas déjà fait)**
   ```powershell
   alembic init app/alembic
   ```
2. **Configurer `alembic.ini`**
   - `script_location = %(here)s/app/alembic`
   - `sqlalchemy.url =` (laisser vide, la variable d'environnement sera utilisée)

3. **Créer une migration après modification des modèles**
   ```powershell
   alembic revision --autogenerate -m "ajout ou modification de champs"
   ```

4. **Appliquer la migration**
   ```powershell
   alembic upgrade head
   ```

## Lancement du script principal

Pour lancer le pipeline ETL complet (téléchargement, upload MinIO, insertion base, etc.) :

```powershell
eltfire
```

Le script va :
- Télécharger les fichiers de données
- Les uploader sur MinIO
- Insérer les données dans la base PostgreSQL

## Structure du projet

```
examen_entrepot/
│   pyproject.toml
│   README.md
│   .env
│
├── app/
│   ├── commands/
│   ├── database/
│   ├── utils/
│   ├── data/
│   └── alembic/
│
└── ...
```

## Dépendances principales
- SQLAlchemy
- Alembic
- psycopg
- pandas
- minio
- typer/click

## Conseils
- Toujours activer l'environnement virtuel avant toute commande.
- Adapter le fichier `.env` à votre environnement local.
- Pour toute migration, bien vérifier la cohérence entre les modèles et la base.

---

**Auteur :** Kamal Moussa MOUSTOIFA BEN
