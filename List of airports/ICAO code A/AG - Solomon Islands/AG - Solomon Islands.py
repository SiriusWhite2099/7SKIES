import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_airports_by_ICAO_code:_A#AG_-_Solomon_Islands'

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_airports_by_ICAO_code:_A#AG_-_Solomon_Islands'

r = requests.get(url)

if r.ok:
    soup = BeautifulSoup(r.text, 'html.parser')

    # Utiliser des critères de recherche appropriés
    table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

    # Créer un fichier CSV en mode écriture avec l'encodage UTF-8
    with open('AG - Solomon Islands.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['ICAO', 'IATA', 'Airport_name', 'Community', 'Province_or_territory']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Écrire la première ligne avec les en-têtes
        writer.writeheader()

        if table:
            tbody = table.find('tbody')
            rows = tbody.find_all('tr')

            for row in rows[1:]:  # Commencer à partir de la deuxième ligne pour éviter les en-têtes
                cells = row.find_all('td')

                if len(cells) == 5:
                    ICAO = cells[0].text.strip()
                    IATA = cells[1].text.strip()
                    Airport_name = cells[2].text.strip()
                    Community = cells[3].text.strip()
                    Province_or_territory = cells[4].text.strip()

                    # Écrire les données dans le fichier CSV
                    writer.writerow({'ICAO': ICAO, 'IATA': IATA, 'Airport_name': Airport_name, 'Community': Community, 'Province_or_territory': Province_or_territory})
else:
    print('Erreur lors de la requête HTTP')


