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
<td>DIAO</td>
<td>ABO</td>
<td><a href="/wiki/Aboisso_Airport" title="Aboisso Airport">Aboisso Airport</a></td>
<td><a href="/wiki/Aboisso" title="Aboisso">Aboisso</a>
</td></tr>
<tr>
<td>DIAP</td>
<td>ABJ</td>
<td><a href="/wiki/Port_Bouet_Airport" class="mw-redirect" title="Port Bouet Airport">Port Bouet Airport</a> (Felix Houphouet Boigny International Airport)</td>
<td><a href="/wiki/Abidjan" title="Abidjan">Abidjan</a>
</td></tr>
<tr>
<td>DIAU</td>
<td>OGO</td>
<td><a href="/wiki/Abengourou_Airport" title="Abengourou Airport">Abengourou Airport</a></td>
<td><a href="/wiki/Abengourou" title="Abengourou">Abengourou</a>
</td></tr>
<tr>
<td>DIBI</td>
<td>BXI</td>
<td><a href="/wiki/Boundiali_Airport" title="Boundiali Airport">Boundiali Airport</a></td>
<td><a href="/wiki/Boundiali" title="Boundiali">Boundiali</a>
</td></tr>
<tr>
<td>DIBK</td>
<td>BYK</td>
<td><a href="/wiki/Bouake_Airport" class="mw-redirect" title="Bouake Airport">Bouake Airport</a></td>
<td><a href="/wiki/Bouake" class="mw-redirect" title="Bouake">Bouake</a>
</td></tr>
<tr>
<td>DIBN</td>
<td>BQO</td>
<td><a href="/wiki/Tehini_Airport" title="Tehini Airport">Tehini Airport</a></td>
<td><a href="/wiki/Bouna,_C%C3%B4te_d%27Ivoire" class="mw-redirect" title="Bouna, Côte d'Ivoire">Bouna</a>
</td></tr>
<tr>
<td>DIBU</td>
<td>BDK</td>
<td><a href="/wiki/Soko_Airport" title="Soko Airport">Soko Airport</a></td>
<td><a href="/wiki/Bondoukou" title="Bondoukou">Bondoukou</a>
</td></tr>
<tr>
<td>DIDK</td>
<td>DIM</td>
<td><a href="/wiki/Dimbokro_Airport" title="Dimbokro Airport">Dimbokro Airport</a></td>
<td><a href="/wiki/Dimbokro" title="Dimbokro">Dimbokro</a>
</td></tr>
<tr>
<td>DIDL</td>
<td>DJO</td>
<td><a href="/wiki/Daloa_Airport" title="Daloa Airport">Daloa Airport</a></td>
<td><a href="/wiki/Daloa" title="Daloa">Daloa</a>
</td></tr>
<tr>
<td>DIDV</td>
<td>DIV</td>
<td><a href="/wiki/Divo_Airport" title="Divo Airport">Divo Airport</a></td>
<td><a href="/wiki/Divo,_C%C3%B4te_d%27Ivoire" class="mw-redirect" title="Divo, Côte d'Ivoire">Divo</a>
</td></tr>
<tr>
<td>DIFK</td>
<td>FEK</td>
<td><a href="/wiki/Ferkessedougou_Airport" class="mw-redirect" title="Ferkessedougou Airport">Ferkessedougou Airport</a></td>
<td><a href="/wiki/Ferkessedougou" class="mw-redirect" title="Ferkessedougou">Ferkessedougou</a>
</td></tr>
<tr>
<td>DIGA</td>
<td>GGN</td>
<td><a href="/wiki/Gagnoa_Airport" title="Gagnoa Airport">Gagnoa Airport</a></td>
<td><a href="/wiki/Gagnoa" title="Gagnoa">Gagnoa</a>
</td></tr>
<tr>
<td>DIGL</td>
<td>GGO</td>
<td><a href="/wiki/Guiglo_Airport" title="Guiglo Airport">Guiglo Airport</a></td>
<td><a href="/wiki/Guiglo" title="Guiglo">Guiglo</a>
</td></tr>
<tr>
<td>DIKO</td>
<td>HGO</td>
<td><a href="/wiki/Korhogo_Airport" title="Korhogo Airport">Korhogo Airport</a></td>
<td><a href="/wiki/Korhogo" title="Korhogo">Korhogo</a>
</td></tr>
<tr>
<td>DIMN</td>
<td>MJC</td>
<td><a href="/wiki/Man_Airport" title="Man Airport">Man Airport</a></td>
<td><a href="/wiki/Man,_Ivory_Coast" title="Man, Ivory Coast">Man</a>
</td></tr>
<tr>
<td>DIOD</td>
<td>KEO</td>
<td><a href="/wiki/Odienne_Airport" class="mw-redirect" title="Odienne Airport">Odienne Airport</a></td>
<td><a href="/wiki/Odienne" class="mw-redirect" title="Odienne">Odienne</a>
</td></tr>
<tr>
<td>DIOF</td>
<td>OFI</td>
<td><a href="/wiki/Ouango_Fitini_Airport" title="Ouango Fitini Airport">Ouango Fitini Airport</a></td>
<td><a href="/w/index.php?title=Ouango_Fitini&amp;action=edit&amp;redlink=1" class="new" title="Ouango Fitini (page does not exist)">Ouango Fitini</a>
</td></tr>
<tr>
<td>DISG</td>
<td>SEO</td>
<td><a href="/wiki/Seguela_Airport" class="mw-redirect" title="Seguela Airport">Seguela Airport</a></td>
<td><a href="/wiki/S%C3%A9gu%C3%A9la_Department" title="Séguéla Department">Seguela</a>
</td></tr>
<tr>
<td>DISP</td>
<td>SPY</td>
<td><a href="/wiki/San_P%C3%A9dro_Airport" title="San Pédro Airport">San Pédro Airport</a></td>
<td><a href="/wiki/San_P%C3%A9dro" class="mw-redirect" title="San Pédro">San Pédro</a>
</td></tr>
<tr>
<td>DISS</td>
<td>ZSS</td>
<td><a href="/wiki/Sassandra_Airport" title="Sassandra Airport">Sassandra Airport</a></td>
<td><a href="/wiki/Sassandra" title="Sassandra">Sassandra</a>
</td></tr>
<tr>
<td>DITB</td>
<td>TXU</td>
<td><a href="/wiki/Tabou_Airport" title="Tabou Airport">Tabou Airport</a></td>
<td><a href="/wiki/Tabou_Department" title="Tabou Department">Tabou</a>
</td></tr>
<tr>
<td>DITM</td>
<td>TOZ</td>
<td><a href="/wiki/Mahana_Airport" title="Mahana Airport">Mahana Airport</a></td>
<td><a href="/wiki/Touba,_C%C3%B4te_d%27Ivoire" class="mw-redirect" title="Touba, Côte d'Ivoire">Touba</a>
</td></tr>
<tr>
<td>DIYO</td>
<td>ASK</td>
<td><a href="/wiki/Yamoussoukro_Airport" class="mw-redirect" title="Yamoussoukro Airport">Yamoussoukro Airport</a></td>
<td><a href="/wiki/Yamoussoukro" title="Yamoussoukro">Yamoussoukro</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("DI - Côte d'Ivoire (Ivory Coast).csv", mode='w', newline='', encoding='utf-8') as csv_file:
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