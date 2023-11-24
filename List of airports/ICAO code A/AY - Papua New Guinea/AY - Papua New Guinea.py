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
<td>AYAA</td>
<td>RNA</td>
<td><a href="/w/index.php?title=Ama_Airport&amp;action=edit&amp;redlink=1" class="new" title="Ama Airport (page does not exist)">Ama Airport</a></td>
<td><a href="/w/index.php?title=Ama,_Papua_New_Guinea&amp;action=edit&amp;redlink=1" class="new" title="Ama, Papua New Guinea (page does not exist)">Ama</a></td>
<td><a href="/w/index.php?title=Ama,_Papua_New_Guinea&amp;action=edit&amp;redlink=1" class="new" title="Ama, Papua New Guinea (page does not exist)">Ama</a>
</td></tr>
<tr>
<td>AYBK</td>
<td>ATD</td>
<td><a href="/wiki/Bulolo_Airport" title="Bulolo Airport">Bulolo Airport</a></td>
<td><a href="/wiki/Bulolo" title="Bulolo">Bulolo</a></td>
<td><a href="/wiki/Bulolo" title="Bulolo">Bulolo</a>
</td></tr>
<tr>
<td>AYDU</td>
<td>VEV</td>
<td><a href="/wiki/Daru_Airport" title="Daru Airport">Daru Airport</a></td>
<td><a href="/wiki/Daru" title="Daru">Daru</a>
</td></tr>
<tr>
<td>AYGA</td>
<td>BPF</td>
<td><a href="/wiki/Gurney_Airport" title="Gurney Airport">Gurney Airport</a></td>
<td><a href="/wiki/Alotau" title="Alotau">Alotau</a>
</td></tr>
<tr>
<td>AYHK</td>
<td>HKN</td>
<td><a href="/wiki/Hoskins_Airport" title="Hoskins Airport">Hoskins Airport</a></td>
<td><a href="/wiki/Kimbe" title="Kimbe">Kimbe</a></td>
<td><a href="/wiki/Kimbe" title="Kimbe">Kimbe</a>
</td></tr>
<tr>
<td>AYIQ</td>
<td>LSA</td>
<td><a href="/wiki/Losuia_Airport" title="Losuia Airport">Losuia Airport</a></td>
<td><a href="/wiki/Kiriwina" title="Kiriwina">Kiriwina</a>
</td></tr>
<tr>
<td>AYKK</td>
<td>KRI</td>
<td><a href="/wiki/Kikori_Airport" title="Kikori Airport">Kikori Airport</a></td>
<td><a href="/wiki/Kikori" title="Kikori">Kikori</a>
</td></tr>
<tr>
<td>AYKM</td>
<td>KZF</td>
<td><a href="/w/index.php?title=Kaintiba_Airport&amp;action=edit&amp;redlink=1" class="new" title="Kaintiba Airport (page does not exist)">Kaintiba Airport</a></td>
<td><a href="/w/index.php?title=Kaintiba&amp;action=edit&amp;redlink=1" class="new" title="Kaintiba (page does not exist)">Kaintiba</a>
</td></tr>
<tr>
<td>AYKY</td>
<td></td>
<td><a href="/wiki/Kunaye_Airport" class="mw-redirect" title="Kunaye Airport">Kunaye Airport</a></td>
<td><a href="/w/index.php?title=Kunaye&amp;action=edit&amp;redlink=1" class="new" title="Kunaye (page does not exist)">Kunaye</a>
</td></tr>
<tr>
<td>AYLA</td>
<td>MAG</td>
<td><a href="/wiki/Madang_Airport" title="Madang Airport">Madang Airport</a></td>
<td><a href="/wiki/Madang" title="Madang">Madang</a>
</td></tr>
<tr>
<td>AYMN</td>
<td>MDU</td>
<td><a href="/wiki/Mendi_Airport" title="Mendi Airport">Mendi Airport</a></td>
<td><a href="/wiki/Mendi" title="Mendi">Mendi</a>
</td></tr>
<tr>
<td>AYMO</td>
<td>MXH</td>
<td><a href="/wiki/Moro_Airport" title="Moro Airport">Moro Airport</a></td>
<td><a href="/wiki/Moro,_Papua_New_Guinea" title="Moro, Papua New Guinea">Moro</a>
</td></tr>
<tr>
<td>AYNZ</td>
<td>LAE</td>
<td><a href="/wiki/Lae_Nadzab_Airport" title="Lae Nadzab Airport">Lae Nadzab Airport</a></td>
<td><a href="/wiki/Lae" title="Lae">Lae</a></td>
<td><a href="/w/index.php?title=Nabzab&amp;action=edit&amp;redlink=1" class="new" title="Nabzab (page does not exist)">Nabzab</a>
</td></tr>
<tr>
<td>AYPY</td>
<td>POM</td>
<td>Jacksons International Airport</td>
<td>Port Moresby
</td>
<td>
</td></tr>
<tr>
<td>AYRB
</td>
<td>RAB
</td>
<td>Rabaul Airport (old) <span style="font-size:85%;">(destroyed)</span>
</td>
<td><a href="/wiki/Rabaul,_New_Britain" class="mw-redirect" title="Rabaul, New Britain">Rabaul, New Britain</a>
</td>
<td>
</td></tr>
<tr>
<td>AYTB</td>
<td>TBG</td>
<td><a href="/wiki/Tabubil_Airport" title="Tabubil Airport">Tabubil Airport</a></td>
<td><a href="/wiki/Tabubil" title="Tabubil">Tabubil</a></td>
<td><a href="/w/index.php?title=Tabulil&amp;action=edit&amp;redlink=1" class="new" title="Tabulil (page does not exist)">Tabulil</a>
</td></tr>
<tr>
<td>AYTK</td>
<td>TRJ</td>
<td><a href="/w/index.php?title=Tarakbits_Airport&amp;action=edit&amp;redlink=1" class="new" title="Tarakbits Airport (page does not exist)">Tarakbits Airport</a></td>
<td><a href="/w/index.php?title=Tarakbits&amp;action=edit&amp;redlink=1" class="new" title="Tarakbits (page does not exist)">Tarakbits</a>
</td></tr>
<tr>
<td>AYWD</td>
<td>WBM</td>
<td><a href="/wiki/Wapenamanda_Airport" title="Wapenamanda Airport">Wapenamanda Airport</a></td>
<td><a href="/wiki/Wapenamanda" class="mw-redirect" title="Wapenamanda">Wapenamanda</a>
</td></tr>
<tr>
<td>AYWK</td>
<td>WWK</td>
<td><a href="/wiki/Wewak_International_Airport" class="mw-redirect" title="Wewak International Airport">Wewak International Airport</a></td>
<td><a href="/wiki/Wewak" title="Wewak">Wewak</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

# Utiliser des critères de recherche appropriés
table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

# Créer un fichier CSV en mode écriture avec l'encodage UTF-8
with open('AY - Papua New Guinea.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ICAO', 'IATA', 'Airport_name', 'Community', 'Province_or_territory']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Écrire la première ligne avec les en-têtes
    writer.writeheader()

    if table:
        rows = table.find_all('tr')

        for row in rows[1:]:  # Commencer à partir de la deuxième ligne pour éviter les en-têtes
            cells = row.find_all(['td', 'th'])

            ICAO = cells[0].text.strip()
            IATA = cells[1].text.strip()
            Airport_name = cells[2].text.strip()
            Community = cells[3].text.strip()
            Province_or_territory = cells[4].text.strip() if len(cells) == 5 else ''

            # Écrire les données dans le fichier CSV
            writer.writerow({'ICAO': ICAO, 'IATA': IATA, 'Airport_name': Airport_name, 'Community': Community, 'Province_or_territory': Province_or_territory})

# Afficher les données au format souhaité
print("ICAO\tIATA\tAirport name\tCommunity\tProvince or territory")
with open('AY - Papua New Guinea.csv', mode='r', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(f"{row['ICAO']}\t{row['IATA']}\t{row['Airport_name']}\t{row['Community']}\t{row['Province_or_territory']}")