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
<td>DTKA</td>
<td>TBJ</td>
<td><a href="/wiki/Tabarka%E2%80%93Ain_Draham_International_Airport" class="mw-redirect" title="Tabarka–Ain Draham International Airport">Tabarka–Ain Draham International Airport</a></td>
<td><a href="/wiki/Tabarka" title="Tabarka">Tabarka</a>
</td></tr>
<tr>
<td>DTMB</td>
<td>MIR</td>
<td><a href="/wiki/Monastir_-_Habib_Bourguiba_International_Airport" class="mw-redirect" title="Monastir - Habib Bourguiba International Airport">Monastir - Habib Bourguiba International Airport</a></td>
<td><a href="/wiki/Monastir,_Tunisia" title="Monastir, Tunisia">Monastir</a>
</td></tr>
<tr>
<td>DTNH</td>
<td>NBE</td>
<td><a href="/wiki/Enfidha_%E2%80%93_Hammamet_International_Airport" class="mw-redirect" title="Enfidha – Hammamet International Airport">Enfidha – Hammamet International Airport</a></td>
<td><a href="/wiki/Enfidha" title="Enfidha">Enfidha</a>
</td></tr>
<tr>
<td>DTTA</td>
<td>TUN</td>
<td><a href="/wiki/Tunis_-_Carthage_International_Airport" class="mw-redirect" title="Tunis - Carthage International Airport">Tunis - Carthage International Airport</a></td>
<td><a href="/wiki/Tunis" title="Tunis">Tunis</a>
</td></tr>
<tr>
<td>DTTB</td>
<td>OIZ</td>
<td><a href="/wiki/Bizerte-Sidi_Ahmed_Air_Base" title="Bizerte-Sidi Ahmed Air Base">Bizerte-Sidi Ahmed Air Base</a></td>
<td><a href="/wiki/Bizerte" title="Bizerte">Bizerte</a>
</td></tr>
<tr>
<td>DTTF</td>
<td>GAF</td>
<td><a href="/wiki/Gafsa_-_Ksar_International_Airport" class="mw-redirect" title="Gafsa - Ksar International Airport">Gafsa - Ksar International Airport</a></td>
<td><a href="/wiki/Gafsa" title="Gafsa">Gafsa</a>
</td></tr>
<tr>
<td>DTTG</td>
<td>GAE</td>
<td><a href="/wiki/Gab%C3%A8s_-_Matmata_International_Airport" class="mw-redirect" title="Gabès - Matmata International Airport">Gabès - Matmata International Airport</a></td>
<td><a href="/wiki/Gab%C3%A8s" title="Gabès">Gabès</a>
</td></tr>
<tr>
<td>DTTJ</td>
<td>DJE</td>
<td><a href="/wiki/Djerba_-_Zarzis_International_Airport" class="mw-redirect" title="Djerba - Zarzis International Airport">Djerba - Zarzis International Airport</a></td>
<td><a href="/wiki/Djerba" title="Djerba">Djerba</a>
</td></tr>
<tr>
<td>DTTX</td>
<td>SFA</td>
<td><a href="/wiki/Thyna/El_Maou_Airport" class="mw-redirect" title="Thyna/El Maou Airport">Thyna/El Maou Airport</a></td>
<td><a href="/wiki/Sfax" title="Sfax">Sfax</a>
</td></tr>
<tr>
<td>DTTZ</td>
<td>TOE</td>
<td><a href="/wiki/Tozeur_-_Nefta_International_Airport" class="mw-redirect" title="Tozeur - Nefta International Airport">Tozeur - Nefta International Airport</a></td>
<td><a href="/wiki/Tozeur" title="Tozeur">Tozeur</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("DT - Tunisia.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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