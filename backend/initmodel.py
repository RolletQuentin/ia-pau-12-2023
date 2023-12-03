import gdown
import zipfile
import os

url = f'https://drive.google.com/uc?id=178iHF_1Q9BzOU-hrwT6V-Ii59ifGMne4'
gdown.download(url, 'cc.fr.50.zip', quiet=False)


# Extraction du fichier ZIP
with zipfile.ZipFile('cc.fr.50.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

# Suppression du fichier ZIP aprÃ¨s extraction
os.remove('cc.fr.50.zip')
