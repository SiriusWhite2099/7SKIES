from bs4 import BeautifulSoup
import csv

html_content = '''
<table class="wikitable" style="width:auto;">
<tbody><tr>
<th width="*"><a href="/wiki/ICAO_airport_code" title="ICAO airport code">ICAO</a>
</th>
<th width="*"><a href="/wiki/IATA_airport_code" title="IATA airport code">IATA</a>
</th>
<th width="*">Airport name
</th>
<th width="*">Community
</th></tr>
<tr>
<td>BKPR</td>
<td>PRN</td>
<td><a href="/wiki/Pristina_International_Airport" title="Pristina International Airport">Pristina International Airport</a> (Pristina International Airport <a href="/wiki/Adem_Jashari" title="Adem Jashari">Adem Jashari</a>)</td>
<td><a href="/wiki/Pristina" title="Pristina">Pristina</a>
</td></tr></tbody></table>
'''
soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open('BK - Kosovo.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ICAO', 'IATA', 'Airport Name', 'Community']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    rows = table.find_all('tr')

    for row in rows[1:]:  # Ignorer la première ligne car c'est l'en-tête
        columns = row.find_all('td')
        icao = columns[0].text.strip()
        iata = columns[1].text.strip()
        airport_name = columns[2].text.strip()
        community = columns[3].text.strip()

        writer.writerow({'ICAO': icao, 'IATA': iata, 'Airport Name': airport_name, 'Community': community})

print("Le fichier CSV a été créé avec succès.")
