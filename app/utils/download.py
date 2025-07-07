import os

import requests

from minio_uploader.file_uploader import MinioFileUploader


class DownloadData:

    def __init__(self):
        # Dictionnaire contenant les noms de fichiers et leurs URL respectives
        self.URLS = {
            "gdp": "https://datahub.io/core/inflation/r/inflation-gdp.csv",
            "consumer": "https://datahub.io/core/inflation/r/inflation-consumer.csv"
        }

        self.uploader = MinioFileUploader()  # Instance du téléchargeur de fichiers MinIO

        # Chemin absolu du répertoire contenant ce fichier Python
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Répertoire de destination des fichiers téléchargés (un dossier "data" à côté du dossier contenant ce script)
        self.DATA_DIR = os.path.join(os.path.dirname(self.BASE_DIR), 'data')

        # Crée le dossier 'data' s’il n’existe pas
        os.makedirs(self.DATA_DIR, exist_ok=True)

        self.download()  # Appelle la méthode pour télécharger les fichiers
        
    def download(self):
        # Parcourt chaque fichier à télécharger
        for name, url in self.URLS.items():
            response = requests.get(url)  # Envoie une requête HTTP GET vers l’URL

            # Construit le chemin complet du fichier de sortie (ex: data/gdp.csv)
            path = os.path.join(self.DATA_DIR, f"{name}.csv")

            # Écrit le contenu du fichier téléchargé dans un fichier local en binaire
            with open(path, "wb") as f:
                f.write(response.content)
            self.uploader.upload_file(
                bucket_name="inflation-data",
                source_file=path,
                destination_file=f"{name}.csv"
            )

