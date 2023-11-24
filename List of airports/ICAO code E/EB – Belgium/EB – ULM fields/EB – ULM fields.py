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
<td>EBAM</td>
<td></td>
<td><a href="/wiki/Amougies_Airfield" title="Amougies Airfield">Amougies Airfield</a></td>
<td><a href="/wiki/Mont-de-l%27Enclus" title="Mont-de-l'Enclus">Amougies</a>
</td></tr>
<tr>
<td>EBAR</td>
<td></td>
<td><a href="/wiki/Arlon-Sterpenich_Aerodrome" title="Arlon-Sterpenich Aerodrome">Arlon-Sterpenich Aerodrome</a></td>
<td><a href="/wiki/Arlon" title="Arlon">Arlon</a>
</td></tr>
<tr>
<td>EBAV</td>
<td></td>
<td><a href="/wiki/Avernas-le-Bauduin_Airfield" title="Avernas-le-Bauduin Airfield">Avernas-le-Bauduin Airfield</a></td>
<td><a href="/wiki/Hannut" title="Hannut">Hannut</a>
</td></tr>
<tr>
<td>EBBN</td>
<td></td>
<td><a href="/wiki/B%C3%BCllingen_Airfield" title="Büllingen Airfield">Büllingen Airfield</a></td>
<td><a href="/wiki/B%C3%BCllingen" title="Büllingen">Büllingen</a>
</td></tr>
<tr>
<td>EBBY</td>
<td></td>
<td><a href="/w/index.php?title=Baisy-Thy_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Baisy-Thy Airfield (page does not exist)">Baisy-Thy Airfield</a></td>
<td><a href="/wiki/Genappe" title="Genappe">Genappe</a>
</td></tr>
<tr>
<td>EBBZ</td>
<td></td>
<td><a href="/w/index.php?title=Buzet_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Buzet Airfield (page does not exist)">Buzet Airfield</a></td>
<td><a href="/wiki/Pont-%C3%A0-Celles" title="Pont-à-Celles">Pont-à-Celles</a>
</td></tr>
<tr>
<td>EBIS</td>
<td></td>
<td><a href="/wiki/Ath/Isi%C3%A8res_Airfield" title="Ath/Isières Airfield">Ath/Isières Airfield</a></td>
<td><a href="/wiki/Ath" title="Ath">Ath</a>
</td></tr>
<tr>
<td>EBLN</td>
<td></td>
<td><a href="/wiki/Liernu_Airfield" title="Liernu Airfield">Liernu Airfield</a></td>
<td><a href="/wiki/%C3%89ghez%C3%A9e" title="Éghezée">Éghezée</a>
</td></tr>
<tr>
<td>EBMG</td>
<td></td>
<td><a href="/w/index.php?title=Doische-Matagne_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Doische-Matagne Airfield (page does not exist)">Doische-Matagne Airfield</a></td>
<td><a href="/wiki/Doische" title="Doische">Doische</a>
</td></tr>
<tr>
<td>EBML</td>
<td></td>
<td><a href="/wiki/Maillen_Airfield" title="Maillen Airfield">Maillen Airfield</a></td>
<td><a href="/wiki/Assesse" title="Assesse">Assesse</a>
</td></tr>
<tr>
<td>EBNE</td>
<td></td>
<td><a href="/w/index.php?title=Neerpelt_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Neerpelt Airfield (page does not exist)">Neerpelt Airfield</a></td>
<td><a href="/wiki/Neerpelt" title="Neerpelt">Neerpelt</a>
</td></tr>
<tr>
<td>EBOR</td>
<td></td>
<td><a href="/w/index.php?title=Orchimont_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Orchimont Airfield (page does not exist)">Orchimont Airfield</a></td>
<td><a href="/wiki/Vresse-sur-Semois" title="Vresse-sur-Semois">Vresse-sur-Semois</a>
</td></tr>
<tr>
<td>EBZU</td>
<td></td>
<td><a href="/wiki/Zuienkerke_Airfield" title="Zuienkerke Airfield">Zuienkerke Airfield</a></td>
<td><a href="/wiki/Zuienkerke" title="Zuienkerke">Zuienkerke</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EB – ULM fields.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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