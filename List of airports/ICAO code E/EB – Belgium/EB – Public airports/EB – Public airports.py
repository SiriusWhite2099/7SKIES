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
</th>
<th width="*">Notes&nbsp;&nbsp;
</th></tr>
<tr>
<td>EBAW</td>
<td>ANR</td>
<td><a href="/wiki/Antwerp_International_Airport" title="Antwerp International Airport">Antwerp International Airport</a></td>
<td><a href="/wiki/Antwerp" title="Antwerp">Antwerp</a>/<a href="/wiki/Deurne,_Belgium" title="Deurne, Belgium">Deurne</a>
</td></tr>
<tr>
<td>EBBR</td>
<td>BRU</td>
<td><a href="/wiki/Brussels_Airport" title="Brussels Airport">Brussels Airport</a></td>
<td><a href="/wiki/City_of_Brussels" title="City of Brussels">Brussels</a>/<a href="/wiki/Zaventem" title="Zaventem">Zaventem</a>
</td></tr>
<tr>
<td>EBCI</td>
<td>CRL</td>
<td><a href="/wiki/Brussels_South_Charleroi_Airport" title="Brussels South Charleroi Airport">Brussels South Charleroi Airport</a></td>
<td><a href="/wiki/Charleroi" title="Charleroi">Charleroi</a>
</td></tr>
<tr>
<td>EBKT</td>
<td>KJK</td>
<td><a href="/wiki/Flanders_International_Airport" title="Flanders International Airport">Flanders International Airport</a></td>
<td><a href="/wiki/Kortrijk" title="Kortrijk">Kortrijk</a>/<a href="/wiki/Wevelgem" title="Wevelgem">Wevelgem</a>
</td></tr>
<tr>
<td>EBLG</td>
<td>LGG</td>
<td><a href="/wiki/Li%C3%A8ge_Airport" title="Liège Airport">Liège Airport</a></td>
<td><a href="/wiki/Li%C3%A8ge" title="Liège">Liège</a>
</td></tr>
<tr>
<td>EBOS</td>
<td>OST</td>
<td><a href="/wiki/Ostend%E2%80%93Bruges_International_Airport" title="Ostend–Bruges International Airport">Ostend–Bruges International Airport</a></td>
<td><a href="/wiki/Bruges" title="Bruges">Bruges</a>/<a href="/wiki/Ostend" title="Ostend">Ostend</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EB – Public airports.csv", mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ICAO', 'IATA', 'Airport Name', 'Community']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    rows = table.find_all('tr')

    for row in rows[1:]:  # Ignorer la première ligne car c'est l'en-tête
        columns = row.find_all('td')

        # Vérifier que la ligne a le nombre attendu de colonnes
        if len(columns) == len(fieldnames):
            icao = columns[0].text.strip()
            iata = columns[1].text.strip()
            airport_name = columns[2].text.strip()
            community = columns[3].text.strip()

            writer.writerow({'ICAO': icao, 'IATA': iata, 'Airport Name': airport_name, 'Community': community})
        else:
            print(f"Ignorer la ligne avec un nombre incorrect de colonnes: {row}")

print("Le fichier CSV a été créé avec succès.")