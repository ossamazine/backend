# Étape 1: Utiliser l'image officielle Python comme base
FROM python:3.9-slim

# Étape 2: Créer /dev/null manuellement
RUN mknod -m 666 /dev/null c 1 3

# Étape 3: Installer les utilitaires manquants
RUN apt-get update && apt-get install -y --no-install-recommends \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

# Étape 4: Définir le répertoire de travail
WORKDIR /app

# Étape 5: Copier le fichier des dépendances
COPY auth-service/requirements.txt . 

# Étape 6: Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 7: Copier le code source de l'application
COPY auth-service/ . 

# Étape 8: Exposer le port 8001
EXPOSE 8000

# Étape 9: Lancer l'application avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
