# Multi-stage build pour le service eltfire
FROM python:3.11-slim AS builder

WORKDIR /app

# Installer les dépendances système minimales
RUN apt-get update && apt-get install -y build-essential gcc && rm -rf /var/lib/apt/lists/*

# Copier uniquement les fichiers nécessaires pour installer les dépendances
COPY ../../../../pyproject.toml ./

# Installer les dépendances dans un dossier temporaire
RUN pip install --user --upgrade pip && pip install --user --no-cache-dir .

# Étape finale : image minimale
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copier le code source du service
COPY ../../../../app ./app
COPY ../../../../pyproject.toml ./

# Copier les dépendances installées par l'utilisateur
ENV PATH="/root/.local/bin:$PATH"

# Installer les dépendances runtime (aucun build)
RUN pip install --user --no-cache-dir .

# Variables d'environnement pour le service
ENV PYTHONUNBUFFERED=1

# Commande de démarrage
ENTRYPOINT ["eltfire"]
