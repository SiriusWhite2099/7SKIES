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
<td>DXAK</td>
<td></td>
<td><a href="/wiki/Akpaka_Airport" title="Akpaka Airport">Akpaka Airport</a></td>
<td><a href="/wiki/Atakpame" class="mw-redirect" title="Atakpame">Atakpame</a>
</td></tr>
<tr>
<td>DXDP</td>
<td></td>
<td><a href="/wiki/Djangou_Airport" title="Djangou Airport">Djangou Airport</a></td>
<td><a href="/wiki/Dapaong" title="Dapaong">Dapaong</a>
</td></tr>
<tr>
<td>DXKP</td>
<td></td>
<td><a href="/wiki/Kolokope_Airport" title="Kolokope Airport">Kolokope Airport</a></td>
<td><a href="/w/index.php?title=Anie,_Togo&amp;action=edit&amp;redlink=1" class="new" title="Anie, Togo (page does not exist)">Anie</a>
</td></tr>
<tr>
<td>DXMG</td>
<td></td>
<td><a href="/wiki/Sansann%C3%A9-Mango_Airport" title="Sansanné-Mango Airport">Sansanné-Mango Airport</a></td>
<td><a href="/wiki/Sansann%C3%A9-Mango" class="mw-redirect" title="Sansanné-Mango">Sansanné-Mango</a>
</td></tr>
<tr>
<td>DXNG</td>
<td>LRL</td>
<td><a href="/wiki/Niamtougou_International_Airport" title="Niamtougou International Airport">Niamtougou International Airport</a></td>
<td><a href="/wiki/Niamtougou" title="Niamtougou">Niamtougou</a>
</td></tr>
<tr>
<td>DXSK</td>
<td></td>
<td><a href="/wiki/Sokode_Airport" class="mw-redirect" title="Sokode Airport">Sokode Airport</a></td>
<td><a href="/wiki/Sokode" class="mw-redirect" title="Sokode">Sokode</a>
</td></tr>
<tr>
<td>DXXX</td>
<td>LFW</td>
<td><a href="/wiki/Lom%C3%A9-Tokoin_Airport" class="mw-redirect" title="Lomé-Tokoin Airport">Lomé-Tokoin Airport</a></td>
<td><a href="/wiki/Lom%C3%A9" title="Lomé">Lomé</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("DX - Togo.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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