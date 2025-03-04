import requests
from bs4 import BeautifulSoup
import pandas as pd


class BaseScraper:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        """Envoie une requête et retourne le HTML."""
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Erreur {response.status_code} lors de l'accès à {self.url}")
            return None

    def save_to_csv(self, data, filename):
        """Sauvegarde les données en CSV."""
        df = pd.DataFrame(data)
        df.to_csv(f"data/{filename}.csv", index=False)
        print(f"Données enregistrées dans {filename}.csv")
