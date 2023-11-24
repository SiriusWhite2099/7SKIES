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
<td>DGAA</td>
<td>ACC</td>
<td><a href="/wiki/Kotoka_International_Airport" title="Kotoka International Airport">Kotoka International Airport</a></td>
<td><a href="/wiki/Accra" title="Accra">Accra</a>
</td></tr>
<tr>
<td>DGAH</td>
<td>HZO</td>
<td><a href="/wiki/Ho_Airport" title="Ho Airport">Ho Airport</a></td>
<td><a href="/wiki/Ho,_Ghana" title="Ho, Ghana">Ho</a>
</td></tr>
<tr>
<td>DGLE</td>
<td>TML</td>
<td><a href="/wiki/Tamale_Airport" class="mw-redirect" title="Tamale Airport">Tamale Airport</a></td>
<td><a href="/wiki/Tamale,_Ghana" title="Tamale, Ghana">Tamale</a>
</td></tr>
<tr>
<td>DGLN</td>
<td></td>
<td><a href="/wiki/Navrongo_Airport" title="Navrongo Airport">Navrongo Airport</a></td>
<td><a href="/wiki/Navrongo" title="Navrongo">Navrongo</a>
</td></tr>
<tr>
<td>DGLW</td>
<td>WZA</td>
<td><a href="/wiki/Wa_Airport" title="Wa Airport">Wa Airport</a></td>
<td><a href="/wiki/Wa,_Ghana" title="Wa, Ghana">Wa</a>
</td></tr>
<tr>
<td>DGLY</td>
<td></td>
<td><a href="/wiki/Yendi_Airport" title="Yendi Airport">Yendi Airport</a></td>
<td><a href="/wiki/Yendi" title="Yendi">Yendi</a>
</td></tr>
<tr>
<td>DGSI</td>
<td>KMS</td>
<td><a href="/wiki/Kumasi_Airport" title="Kumasi Airport">Kumasi Airport</a></td>
<td><a href="/wiki/Kumasi" title="Kumasi">Kumasi</a>
</td></tr>
<tr>
<td>DGSN</td>
<td>NYI</td>
<td><a href="/wiki/Sunyani_Airport" title="Sunyani Airport">Sunyani Airport</a></td>
<td><a href="/wiki/Sunyani" title="Sunyani">Sunyani</a>
</td></tr>
<tr>
<td>DGSO</td>
<td></td>
<td><a href="/wiki/Obuasi_Airport" title="Obuasi Airport">Obuasi Airport</a></td>
<td><a href="/wiki/Obuasi" title="Obuasi">Obuasi</a>
</td></tr>
<tr>
<td>DGTK</td>
<td>TKD</td>
<td><a href="/wiki/Takoradi_Airport" title="Takoradi Airport">Takoradi Airport</a></td>
<td><a href="/wiki/Takoradi" class="mw-redirect" title="Takoradi">Takoradi</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open('DG - Ghana.csv', mode='w', newline='', encoding='utf-8') as csv_file:
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

