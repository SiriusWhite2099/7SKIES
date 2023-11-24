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
<td>DRRA</td>
<td></td>
<td><a href="/wiki/Tessaoua_Airport" title="Tessaoua Airport">Tessaoua Airport</a></td>
<td><a href="/wiki/Tessaoua" title="Tessaoua">Tessaoua</a>
</td></tr>
<tr>
<td>DRRC</td>
<td></td>
<td><a href="/wiki/Dogondoutchi_Airport" title="Dogondoutchi Airport">Dogondoutchi Airport</a></td>
<td><a href="/wiki/Dogondoutchi" title="Dogondoutchi">Dogondoutchi</a>
</td></tr>
<tr>
<td>DRRD</td>
<td></td>
<td><a href="/wiki/Dosso_Airport" title="Dosso Airport">Dosso Airport</a></td>
<td><a href="/wiki/Dosso,_Niger" title="Dosso, Niger">Dosso</a>
</td></tr>
<tr>
<td>DRRE</td>
<td></td>
<td><a href="/wiki/T%C3%A9ra_Airport" title="Téra Airport">Téra Airport</a></td>
<td><a href="/wiki/T%C3%A9ra" title="Téra">Téra</a>
</td></tr>
<tr>
<td>DRRG</td>
<td></td>
<td><a href="/wiki/Gaya_Airport_(Niger)" title="Gaya Airport (Niger)">Gaya Airport</a></td>
<td><a href="/wiki/Gaya,_Niger" title="Gaya, Niger">Gaya</a>
</td></tr>
<tr>
<td>DRRL</td>
<td></td>
<td><a href="/wiki/Tillabery_Airport" class="mw-redirect" title="Tillabery Airport">Tillabery Airport</a></td>
<td><a href="/wiki/Tillabery" class="mw-redirect" title="Tillabery">Tillabery</a>
</td></tr>
<tr>
<td>DRRM</td>
<td>MFQ</td>
<td><a href="/wiki/Maradi_Airport" title="Maradi Airport">Maradi Airport</a></td>
<td><a href="/wiki/Maradi,_Niger" title="Maradi, Niger">Maradi</a>
</td></tr>
<tr>
<td>DRRN</td>
<td>NIM</td>
<td><a href="/wiki/Diori_Hamani_International_Airport" title="Diori Hamani International Airport">Diori Hamani International Airport</a></td>
<td><a href="/wiki/Niamey" title="Niamey">Niamey</a>
</td></tr>
<tr>
<td>DRRP</td>
<td></td>
<td><a href="/wiki/La_Tapoa_Airport" title="La Tapoa Airport">La Tapoa Airport</a></td>
<td><a href="/wiki/La_Tapoa" title="La Tapoa">La Tapoa</a>
</td></tr>
<tr>
<td>DRRT</td>
<td>THZ</td>
<td><a href="/wiki/Tahoua_Airport" title="Tahoua Airport">Tahoua Airport</a></td>
<td><a href="/wiki/Tahoua" title="Tahoua">Tahoua</a>
</td></tr>
<tr>
<td>DRRU</td>
<td></td>
<td><a href="/wiki/Ouallam_Airport" title="Ouallam Airport">Ouallam Airport</a></td>
<td><a href="/wiki/Ouallam" title="Ouallam">Ouallam</a>
</td></tr>
<tr>
<td>DRZA</td>
<td>AJY</td>
<td><a href="/wiki/Mano_Dayak_International_Airport" title="Mano Dayak International Airport">Mano Dayak International Airport</a></td>
<td><a href="/wiki/Agades" class="mw-redirect" title="Agades">Agades</a> South
</td></tr>
<tr>
<td>DRZD</td>
<td></td>
<td><a href="/wiki/Dirkou_Airport" title="Dirkou Airport">Dirkou Airport</a></td>
<td><a href="/wiki/Dirkou" title="Dirkou">Dirkou</a>
</td></tr>
<tr>
<td>DRZF</td>
<td></td>
<td><a href="/wiki/Diffa_Airport" title="Diffa Airport">Diffa Airport</a></td>
<td><a href="/wiki/Diffa" title="Diffa">Diffa</a>
</td></tr>
<tr>
<td>DRZG</td>
<td></td>
<td><a href="/wiki/Goure_Airport" title="Goure Airport">Goure Airport</a></td>
<td><a href="/wiki/Goure" title="Goure">Goure</a>
</td></tr>
<tr>
<td>DRZI</td>
<td></td>
<td><a href="/wiki/Iferouane_Airport" title="Iferouane Airport">Iferouane Airport</a></td>
<td><a href="/wiki/Iferouane" title="Iferouane">Iferouane</a>
</td></tr>
<tr>
<td>DRZL</td>
<td>RLT</td>
<td><a href="/wiki/Arlit_Airport" title="Arlit Airport">Arlit Airport</a></td>
<td><a href="/wiki/Arlit" title="Arlit">Arlit</a>
</td></tr>
<tr>
<td>DRZM</td>
<td></td>
<td><a href="/wiki/Maine-Soroa_Airport" title="Maine-Soroa Airport">Maine-Soroa Airport</a></td>
<td><a href="/wiki/Maine-Soroa" class="mw-redirect" title="Maine-Soroa">Maine-Soroa</a>
</td></tr>
<tr>
<td>DRZR</td>
<td>ZND</td>
<td><a href="/wiki/Zinder_Airport" title="Zinder Airport">Zinder Airport</a></td>
<td><a href="/wiki/Zinder" title="Zinder">Zinder</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("DR - Niger.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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