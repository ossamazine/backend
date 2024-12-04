# Étape 1: Utiliser l'image officielle Python
FROM python:3.9-slim

# Étape 2: Mettre à jour et installer des utilitaires nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

# Étape 3: Créer /dev/null si nécessaire (cela ne devrait pas être nécessaire si coreutils est installé correctement)
RUN if [ ! -e /dev/null ]; then mknod -m 666 /dev/null c 1 3; fi

# Étape 4: Définir le répertoire de travail
WORKDIR /app

# Étape 5: Copier le fichier des dépendances
COPY auth-service/requirements.txt .

# Étape 6: Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 7: Copier tout le code source
COPY auth-service/ .

# Étape 8: Exposer le port 8000
EXPOSE 8000

# Étape 9: Lancer l'application avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
