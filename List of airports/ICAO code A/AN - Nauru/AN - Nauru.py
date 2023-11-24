from bs4 import BeautifulSoup
import csv

html_content = '''
<table class="wikitable" style="width:auto;">
<tbody><tr>
<th width="*"><a href="/wiki/ICAO_airport_code" title="ICAO airport code">ICAO</a>&nbsp;&nbsp;
</th>
<th width="*"><a href="/wiki/IATA_airport_code" title="IATA airport code">IATA</a>&nbsp;&nbsp;
</th>
<th width="*">Airport name&nbsp;&nbsp;
</th>
<th width="*">Community&nbsp;&nbsp;
</th></tr>
<tr>
<td>ANAU</td>
<td>–</td>
<td><a href="/wiki/Nauru" title="Nauru">Nauru</a></td>
<td><a href="/wiki/Flight_information_region" title="Flight information region">Flight Information Region</a></td>
<td>–
</td></tr>
<tr>
<td>ANYN</td>
<td>INU</td>
<td><a href="/wiki/Nauru_International_Airport" title="Nauru International Airport">Nauru International Airport</a></td>
<td><a href="/wiki/Yaren_District" title="Yaren District">Yaren</a></td>
<td>–
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

# Utiliser des critères de recherche appropriés
table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

# Créer un fichier CSV en mode écriture avec l'encodage UTF-8
with open('AN - Nauru.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ICAO', 'IATA', 'Airport_name', 'Community']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Écrire la première ligne avec les en-têtes
    writer.writeheader()

    if table:
        rows = table.find_all('tr')

        for row in rows[1:]:  # Commencer à partir de la deuxième ligne pour éviter les en-têtes
            cells = row.find_all(['td', 'th'])

            if len(cells) == 5:
                ICAO = cells[0].text.strip()
                IATA = cells[1].text.strip()
                Airport_name = cells[2].text.strip()
                Community = cells[3].text.strip()

                # Écrire les données dans le fichier CSV
                writer.writerow({'ICAO': ICAO, 'IATA': IATA, 'Airport_name': Airport_name, 'Community': Community})


