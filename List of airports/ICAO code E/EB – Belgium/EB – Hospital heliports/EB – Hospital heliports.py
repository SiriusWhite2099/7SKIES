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
<td>EBAL</td>
<td></td>
<td><a href="/w/index.php?title=Aalst_Hospital_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Aalst Hospital Heliport (page does not exist)">Aalst Hospital Heliport</a></td>
<td><a href="/wiki/Aalst,_Belgium" title="Aalst, Belgium">Aalst</a>
</td></tr>
<tr>
<td>EBBA</td>
<td></td>
<td><a href="/wiki/Baudour_Heliport" title="Baudour Heliport">Baudour Heliport</a></td>
<td><a href="/wiki/Baudour" title="Baudour">Douvrain</a>
</td></tr>
<tr>
<td>EBEU</td>
<td></td>
<td><a href="/w/index.php?title=Universitair_Ziekenhuis_Antwerpen_Hospital_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Universitair Ziekenhuis Antwerpen Hospital Heliport (page does not exist)">Universitair Ziekenhuis Antwerpen Hospital Heliport</a></td>
<td><a href="/wiki/Edegem" title="Edegem">Edegem</a>
</td></tr>
<tr>
<td>EBGA</td>
<td></td>
<td><a href="/w/index.php?title=UZ_Leuven_Hospital_Heliport&amp;action=edit&amp;redlink=1" class="new" title="UZ Leuven Hospital Heliport (page does not exist)">UZ Leuven Hospital Heliport</a></td>
<td><a href="/wiki/Leuven" title="Leuven">Leuven</a>
</td></tr>
<tr>
<td>EBGE</td>
<td></td>
<td><a href="/w/index.php?title=Grand_H%C3%B4pital_de_Charleroi_(GHDC_Asbl)_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Grand Hôpital de Charleroi (GHDC Asbl) Heliport (page does not exist)">Grand Hôpital de Charleroi (GHDC Asbl) Heliport</a></td>
<td><a href="/wiki/Loverval" title="Loverval">Loverval</a>
</td></tr>
<tr>
<td>EBGT</td>
<td></td>
<td><a href="/wiki/Ghent/Industry_Zone_Heliport" title="Ghent/Industry Zone Heliport">Ghent/Industry Zone Heliport</a></td>
<td><a href="/wiki/Ghent" title="Ghent">Ghent</a>
</td></tr>
<tr>
<td>EBKG</td>
<td></td>
<td><a href="/wiki/AZ_Groeninge_Heliport" title="AZ Groeninge Heliport">AZ Groeninge Heliport</a></td>
<td><a href="/wiki/Kortrijk" title="Kortrijk">Kortrijk</a>
</td></tr>
<tr>
<td>EBLC</td>
<td></td>
<td><a href="/w/index.php?title=CHR_de_La_Citadelle_Hospital_Heliport&amp;action=edit&amp;redlink=1" class="new" title="CHR de La Citadelle Hospital Heliport (page does not exist)">CHR de La Citadelle Hospital Heliport</a></td>
<td><a href="/wiki/Li%C3%A8ge" title="Liège">Liège</a>
</td></tr>
<tr>
<td>EBLS</td>
<td></td>
<td><a href="/w/index.php?title=Centre_Hospitalier_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Centre Hospitalier Heliport (page does not exist)">Centre Hospitalier Heliport</a></td>
<td><a href="/wiki/Li%C3%A8ge" title="Liège">Liège</a>
</td></tr>
<tr>
<td>EBMD</td>
<td></td>
<td><a href="/w/index.php?title=Antwerp/Middelheim_Hospital_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Antwerp/Middelheim Hospital Heliport (page does not exist)">Antwerp/Middelheim Hospital Heliport</a></td>
<td><a href="/wiki/Antwerp_(district)" title="Antwerp (district)">Antwerp</a>
</td></tr>
<tr>
<td>EBMS</td>
<td></td>
<td><a href="/w/index.php?title=Centre_M%C3%A9dical_H%C3%A9liport%C3%A9_ASBL_(CMH)_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Centre Médical Héliporté ASBL (CMH) Heliport (page does not exist)">Centre Médical Héliporté ASBL (CMH) Heliport</a></td>
<td><a href="/wiki/Lierneux" title="Lierneux">Lierneux</a>
</td></tr>
<tr>
<td>EBMT</td>
<td></td>
<td><a href="/w/index.php?title=Centre_Hospitalier_Universitaire_A._V%C3%A9sale_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Centre Hospitalier Universitaire A. Vésale Heliport (page does not exist)">Centre Hospitalier Universitaire A. Vésale Heliport</a></td>
<td><a href="/wiki/Montigny-le-Tilleul" title="Montigny-le-Tilleul">Montigny-le-Tilleul</a>
</td></tr>
<tr>
<td>EBNB</td>
<td></td>
<td><a href="/w/index.php?title=Clinique_Saint-Luc_Bouge_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Clinique Saint-Luc Bouge Heliport (page does not exist)">Clinique Saint-Luc Bouge Heliport</a></td>
<td><a href="/wiki/Namur" title="Namur">Namur</a>
</td></tr>
<tr>
<td>EBSJ</td>
<td></td>
<td><a href="/w/index.php?title=Bruges/Sint-Pieters_Hospital_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Bruges/Sint-Pieters Hospital Heliport (page does not exist)">Bruges/Sint-Pieters Hospital Heliport</a></td>
<td><a href="/wiki/Sint-Pieters" title="Sint-Pieters">Sint-Pieters</a>
</td></tr>
<tr>
<td>EBSS</td>
<td></td>
<td><a href="/wiki/Sint-Lucas_Hospital_Heliport" title="Sint-Lucas Hospital Heliport">Sint-Lucas Hospital Heliport</a></td>
<td><a href="/wiki/Bruges" title="Bruges">Bruges</a>
</td></tr>
<tr>
<td>EBUB</td>
<td></td>
<td><a href="/w/index.php?title=Erasmus_Hospital_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Erasmus Hospital Heliport (page does not exist)">Erasmus Hospital Heliport</a></td>
<td><a href="/wiki/Anderlecht" title="Anderlecht">Anderlecht</a>
</td></tr>
<tr>
<td>EBUC</td>
<td></td>
<td><a href="/w/index.php?title=Cliniques_Universitaires_Saint-Luc_Hospital_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Cliniques Universitaires Saint-Luc Hospital Heliport (page does not exist)">Cliniques Universitaires Saint-Luc Hospital Heliport</a></td>
<td><a href="/wiki/Woluwe-Saint-Lambert" title="Woluwe-Saint-Lambert">Woluwe-Saint-Lambert</a>
</td></tr>
<tr>
<td>EBVS</td>
<td></td>
<td><a href="/wiki/Veurne/Sint-Augustinus_Heliport" title="Veurne/Sint-Augustinus Heliport">Veurne/Sint-Augustinus Heliport</a></td>
<td><a href="/wiki/Veurne" title="Veurne">Veurne</a>
</td></tr>
<tr>
<td>EBYP</td>
<td></td>
<td><a href="/w/index.php?title=Regionaal_Ziekenhuis_Jan_Yperman_VZW_Hospital_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Regionaal Ziekenhuis Jan Yperman VZW Hospital Heliport (page does not exist)">Regionaal Ziekenhuis Jan Yperman VZW Hospital Heliport</a></td>
<td><a href="/wiki/Ypres" title="Ypres">Ypres</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EB – Hospital heliports.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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