# Étape 1: Utiliser l'image officielle Python comme base
FROM python:3.9-slim

# Étape 2: Installer les utilitaires manquants
RUN apt-get update && apt-get install -y --no-install-recommends \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

# Étape 3: Définir le répertoire de travail
WORKDIR /app

# Étape 4: Copier le fichier des dépendances
COPY auth-service/requirements.txt . 
# Assurez-vous que le fichier se trouve dans ce dossier

# Étape 5: Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 6: Copier le code source de l'application
COPY auth-service/ . 
# Assurez-vous que tous les fichiers sont dans ce dossier

# Étape 7: Exposer le port 8001
EXPOSE 8000

# Étape 8: Lancer l'application avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
