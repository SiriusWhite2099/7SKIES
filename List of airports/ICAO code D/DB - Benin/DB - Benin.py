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
</th>
<th width="*">Province or<br>territory&nbsp;&nbsp;
</th></tr>
<tr>
<td>DBBB</td>
<td>COO</td>
<td><a href="/wiki/Cadjehoun_Airport" title="Cadjehoun Airport">Cadjehoun Airport</a> (Cotonou Airport)</td>
<td><a href="/wiki/Cotonou" title="Cotonou">Cotonou</a>
</td></tr>
<tr>
<td>DBBC</td>
<td></td>
<td><a href="/wiki/Cana_Airport" title="Cana Airport">Cana Airport</a></td>
<td><a href="/wiki/Bohicon" title="Bohicon">Bohicon</a>
</td></tr>
<tr>
<td>DBBD</td>
<td>DJA</td>
<td><a href="/wiki/Djougou_Airport" title="Djougou Airport">Djougou Airport</a></td>
<td><a href="/wiki/Djougou" title="Djougou">Djougou</a>
</td></tr>
<tr>
<td>DBBK</td>
<td>KDC</td>
<td><a href="/wiki/Kandi_Airport" title="Kandi Airport">Kandi Airport</a></td>
<td><a href="/wiki/Kandi,_Benin" title="Kandi, Benin">Kandi</a>
</td></tr>
<tr>
<td>DBBN</td>
<td>NAE</td>
<td><a href="/wiki/Natitingou_Airport" class="mw-redirect" title="Natitingou Airport">Natitingou Airport</a></td>
<td><a href="/wiki/Natitingou" title="Natitingou">Natitingou</a>
</td></tr>
<tr>
<td>DBBO</td>
<td></td>
<td><a href="/wiki/Porga_Airport" title="Porga Airport">Porga Airport</a></td>
<td><a href="/wiki/Porga" title="Porga">Porga</a>
</td></tr>
<tr>
<td>DBBP</td>
<td>PKO</td>
<td><a href="/wiki/Parakou_Airport" title="Parakou Airport">Parakou Airport</a></td>
<td><a href="/wiki/Parakou" title="Parakou">Parakou</a>
</td></tr>
<tr>
<td>DBBR</td>
<td></td>
<td><a href="/wiki/Bembereke_Airport" title="Bembereke Airport">Bembereke Airport</a></td>
<td><a href="/wiki/Bembereke" class="mw-redirect" title="Bembereke">Bembereke</a>
</td></tr>
<tr>
<td>DBBS</td>
<td>SVF</td>
<td><a href="/wiki/Sav%C3%A9_Airport" title="Savé Airport">Savé Airport</a></td>
<td><a href="/wiki/Sav%C3%A9" class="mw-redirect" title="Savé">Savé</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open('DB - Benin.csv', mode='w', newline='', encoding='utf-8') as csv_file:
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