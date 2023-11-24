import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_international_airports_by_country'

r = requests.get(url)

if r.ok:
    soup = BeautifulSoup(r.text, 'lxml')
    tables = soup.find_all('table', class_='wikitable')

    # Crée un fichier CSV en mode écriture avec l'encodage UTF-8
    with open('airport_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Code Pays', 'Nom du Pays', 'Nom de l\'Aéroport']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Écrit la première ligne avec les en-têtes
        writer.writeheader()

        for table in tables:
            rows = table.find_all('tr')

            for row in rows:
                cells = row.find_all('td')

                if len(cells) == 3:
                    code_pays = cells[2].text.strip()
                    nom_pays = cells[0].text.strip()
                    nom_aeroport = cells[1].text.strip()

                    # Écrit les données dans le fichier CSV
                    writer.writerow({'Code Pays': code_pays, 'Nom du Pays': nom_pays, 'Nom de l\'Aéroport': nom_aeroport})
else:
    print('Erreur lors de la requête HTTP')