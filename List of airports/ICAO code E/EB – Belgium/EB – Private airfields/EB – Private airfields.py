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
<td>EBBT</td>
<td></td>
<td><a href="/wiki/Brasschaat_Airfield" title="Brasschaat Airfield">Brasschaat Airfield</a></td>
<td><a href="/wiki/Brasschaat" title="Brasschaat">Brasschaat</a>
</td></tr>
<tr>
<td>EBCF</td>
<td></td>
<td><a href="/wiki/Cerfontaine_Airfield" title="Cerfontaine Airfield">Cerfontaine Airfield</a></td>
<td><a href="/wiki/Cerfontaine,_Belgium" title="Cerfontaine, Belgium">Cerfontaine</a>
</td></tr>
<tr>
<td>EBGB</td>
<td></td>
<td><a href="/wiki/Grimbergen_Airfield" title="Grimbergen Airfield">Grimbergen Airfield</a></td>
<td><a href="/wiki/Tienen" title="Tienen">Grimbergen</a>
</td></tr>
<tr>
<td>EBGG</td>
<td></td>
<td><a href="/wiki/Overboelare_Airfield" title="Overboelare Airfield">Overboelare Airfield</a></td>
<td><a href="/wiki/Geraardsbergen" title="Geraardsbergen">Geraardsbergen</a>/Overboelare
</td></tr>
<tr>
<td>EBHN</td>
<td></td>
<td><a href="/wiki/Hoevenen_Airfield" title="Hoevenen Airfield">Hoevenen Airfield</a></td>
<td><a href="/wiki/Stabroek" title="Stabroek">Hoevenen</a>
</td></tr>
<tr>
<td>EBKH</td>
<td></td>
<td><a href="/wiki/Balen-Keiheuvel_Aerodrome" title="Balen-Keiheuvel Aerodrome">Balen-Keiheuvel Aerodrome</a></td>
<td><a href="/wiki/Balen" title="Balen">Balen</a>
</td></tr>
<tr>
<td>EBLE</td>
<td></td>
<td><a href="/wiki/Leopoldsburg/Beverlo_Airfield" title="Leopoldsburg/Beverlo Airfield">Leopoldsburg/Beverlo Airfield</a></td>
<td><a href="/wiki/Leopoldsburg" title="Leopoldsburg">Leopoldsburg</a>/<a href="/wiki/Beringen,_Belgium" title="Beringen, Belgium">Beverlo</a>
</td></tr>
<tr>
<td>EBMO</td>
<td></td>
<td><a href="/wiki/Moorsele_Airfield" title="Moorsele Airfield">Moorsele Airfield</a></td>
<td><a href="/wiki/Wevelgem" title="Wevelgem">Moorsele</a>
</td></tr>
<tr>
<td>EBNM</td>
<td></td>
<td><a href="/wiki/Namur-Suarl%C3%A9e_Airfield" title="Namur-Suarlée Airfield">Namur-Suarlée Airfield</a></td>
<td><a href="/wiki/Namur" title="Namur">Namur</a>
</td></tr>
<tr>
<td>EBSG</td>
<td></td>
<td><a href="/wiki/Saint-Ghislain_Airfield" title="Saint-Ghislain Airfield">Saint-Ghislain Airfield</a></td>
<td><a href="/wiki/Saint-Ghislain" title="Saint-Ghislain">Saint-Ghislain</a>
</td></tr>
<tr>
<td>EBSH</td>
<td></td>
<td><a href="/wiki/Saint-Hubert_Airfield" title="Saint-Hubert Airfield">Saint-Hubert Airfield</a></td>
<td><a href="/wiki/Saint-Hubert,_Belgium" title="Saint-Hubert, Belgium">Saint-Hubert</a>
</td></tr>
<tr>
<td>EBSL</td>
<td></td>
<td><a href="/wiki/Zutendaal_Air_Base" title="Zutendaal Air Base">Zutendaal Air Base</a></td>
<td><a href="/wiki/Zutendaal" title="Zutendaal">Zutendaal</a>
</td></tr>
<tr>
<td>EBSP</td>
<td></td>
<td><a href="/wiki/Spa-La_Sauveni%C3%A8re_Airfield" title="Spa-La Sauvenière Airfield">Spa-La Sauvenière Airfield</a></td>
<td><a href="/wiki/Spa,_Belgium" title="Spa, Belgium">Spa</a>
</td></tr>
<tr>
<td>EBST</td>
<td></td>
<td><a href="/wiki/Sint-Truiden_/_Brustem_Airfield" title="Sint-Truiden / Brustem Airfield">Sint-Truiden / Brustem Airfield</a></td>
<td>Brustem/<a href="/wiki/Sint-Truiden" title="Sint-Truiden">Sint-Truiden</a>
</td></tr>
<tr>
<td>EBTN</td>
<td></td>
<td><a href="/wiki/Goetsenhoven_Airfield" title="Goetsenhoven Airfield">Goetsenhoven Airfield</a></td>
<td><a href="/wiki/Goetsenhoven" class="mw-redirect" title="Goetsenhoven">Goetsenhoven</a>
</td></tr>
<tr>
<td>EBTX</td>
<td></td>
<td><a href="/wiki/Verviers-Theux_Airfield" title="Verviers-Theux Airfield">Verviers-Theux Airfield</a></td>
<td><a href="/wiki/Theux" title="Theux">Theux</a>
</td></tr>
<tr>
<td>EBTY</td>
<td></td>
<td><a href="/wiki/Maubray_Airfield" title="Maubray Airfield">Maubray Airfield</a></td>
<td><a href="/wiki/Tournai" title="Tournai">Tournai</a>
</td></tr>
<tr>
<td>EBZH</td>
<td></td>
<td><a href="/wiki/Kiewit_Airfield" title="Kiewit Airfield">Kiewit Airfield</a></td>
<td><a href="/wiki/Hasselt" title="Hasselt">Hasselt</a>
</td></tr>
<tr>
<td>EBZR</td>
<td>OBL</td>
<td><a href="/wiki/Oostmalle_Airfield" title="Oostmalle Airfield">Oostmalle Airfield</a></td>
<td><a href="/wiki/Zoersel" title="Zoersel">Zoersel</a>/<a href="/wiki/Oostmalle" title="Oostmalle">Oostmalle</a>
</td></tr>
<tr>
<td>EBZW</td>
<td></td>
<td><a href="/wiki/Zwartberg_Airfield" title="Zwartberg Airfield">Zwartberg Airfield</a></td>
<td><a href="/wiki/Genk" title="Genk">Genk</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EB – Private airfields.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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