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
<td>DFCA</td>
<td>XKY</td>
<td><a href="/wiki/Kaya_Airport" title="Kaya Airport">Kaya Airport</a></td>
<td><a href="/wiki/Kaya,_Burkina_Faso" title="Kaya, Burkina Faso">Kaya</a>
</td></tr>
<tr>
<td>DFCC</td>
<td>OUG</td>
<td><a href="/wiki/Ouahigouya_Airport" title="Ouahigouya Airport">Ouahigouya Airport</a></td>
<td><a href="/wiki/Ouahigouya" title="Ouahigouya">Ouahigouya</a>
</td></tr>
<tr>
<td>DFCJ</td>
<td>XDJ</td>
<td><a href="/wiki/Djibo_Airport" title="Djibo Airport">Djibo Airport</a></td>
<td><a href="/wiki/Djibo" title="Djibo">Djibo</a>
</td></tr>
<tr>
<td>DFCL</td>
<td>XLU</td>
<td><a href="/wiki/Leo_Airport" title="Leo Airport">Leo Airport</a></td>
<td><a href="/wiki/Leo,_Burkina_Faso" class="mw-redirect" title="Leo, Burkina Faso">Leo</a>
</td></tr>
<tr>
<td>DFCP</td>
<td>PUP</td>
<td><a href="/wiki/P%C3%B4_Airport" title="Pô Airport">Pô Airport</a></td>
<td><a href="/wiki/P%C3%B4" title="Pô">Pô</a>
</td></tr>
<tr>
<td>DFEA</td>
<td>XBO</td>
<td><a href="/wiki/Boulsa_Airport" title="Boulsa Airport">Boulsa Airport</a></td>
<td><a href="/wiki/Boulsa" title="Boulsa">Boulsa</a>
</td></tr>
<tr>
<td>DFEB</td>
<td>XBG</td>
<td><a href="/wiki/Bogande_Airport" title="Bogande Airport">Bogande Airport</a></td>
<td><a href="/wiki/Bogande" class="mw-redirect" title="Bogande">Bogande</a>
</td></tr>
<tr>
<td>DFED</td>
<td>DIP</td>
<td><a href="/wiki/Diapaga_Airport" title="Diapaga Airport">Diapaga Airport</a></td>
<td><a href="/wiki/Diapaga" title="Diapaga">Diapaga</a>
</td></tr>
<tr>
<td>DFEE</td>
<td>DOR</td>
<td><a href="/wiki/Dori_Airport" title="Dori Airport">Dori Airport</a></td>
<td><a href="/wiki/Dori,_Burkina_Faso" title="Dori, Burkina Faso">Dori</a>
</td></tr>
<tr>
<td>DFEF</td>
<td>FNG</td>
<td><a href="/wiki/Fada_N%27gourma_Airport" title="Fada N'gourma Airport">Fada N'gourma Airport</a></td>
<td><a href="/wiki/Fada_N%27gourma" title="Fada N'gourma">Fada N'gourma</a>
</td></tr>
<tr>
<td>DFEG</td>
<td>XGG</td>
<td><a href="/wiki/Gorom_Gorom_Airport" title="Gorom Gorom Airport">Gorom Gorom Airport</a></td>
<td><a href="/wiki/Gorom_Gorom" class="mw-redirect" title="Gorom Gorom">Gorom Gorom</a>
</td></tr>
<tr>
<td>DFEL</td>
<td>XKA</td>
<td><a href="/wiki/Kantchari_Airport" title="Kantchari Airport">Kantchari Airport</a></td>
<td><a href="/wiki/Kantchari" title="Kantchari">Kantchari</a>
</td></tr>
<tr>
<td>DFEM</td>
<td>TMQ</td>
<td><a href="/wiki/Tambao_Airport" title="Tambao Airport">Tambao Airport</a></td>
<td><a href="/wiki/Tambao" title="Tambao">Tambao</a>
</td></tr>
<tr>
<td>DFEP</td>
<td>XPA</td>
<td><a href="/wiki/Pama_Airport" title="Pama Airport">Pama Airport</a></td>
<td><a href="/wiki/Pama,_Burkina_Faso" title="Pama, Burkina Faso">Pama</a>
</td></tr>
<tr>
<td>DFES</td>
<td>XSE</td>
<td><a href="/wiki/Sebba_Airport" title="Sebba Airport">Sebba Airport</a></td>
<td><a href="/wiki/Sebba" title="Sebba">Sebba</a>
</td></tr>
<tr>
<td>DFET</td>
<td>TEG</td>
<td><a href="/wiki/Tenkodogo_Airport" title="Tenkodogo Airport">Tenkodogo Airport</a></td>
<td><a href="/wiki/Tenkodogo" title="Tenkodogo">Tenkodogo</a>
</td></tr>
<tr>
<td>DFEZ</td>
<td>XZA</td>
<td><a href="/wiki/Zabre_Airport" class="mw-redirect" title="Zabre Airport">Zabre Airport</a></td>
<td><a href="/wiki/Zabr%C3%A9" title="Zabré">Zabré</a>
</td></tr>
<tr>
<td>DFFD</td>
<td>OUA</td>
<td><a href="/wiki/Ouagadougou_Airport" class="mw-redirect" title="Ouagadougou Airport">Ouagadougou Airport</a></td>
<td><a href="/wiki/Ouagadougou" title="Ouagadougou">Ouagadougou</a>
</td></tr>
<tr>
<td>DFOB</td>
<td>BNR</td>
<td><a href="/wiki/Banfora_Airport" title="Banfora Airport">Banfora Airport</a></td>
<td><a href="/wiki/Banfora" title="Banfora">Banfora</a>
</td></tr>
<tr>
<td>DFOD</td>
<td>DGU</td>
<td><a href="/wiki/Dedougou_Airport" class="mw-redirect" title="Dedougou Airport">Dedougou Airport</a></td>
<td><a href="/wiki/Dedougou" class="mw-redirect" title="Dedougou">Dedougou</a>
</td></tr>
<tr>
<td>DFON</td>
<td>XNU</td>
<td><a href="/wiki/Nouna_Airport" title="Nouna Airport">Nouna Airport</a></td>
<td><a href="/wiki/Nouna" title="Nouna">Nouna</a>
</td></tr>
<tr>
<td>DFOO</td>
<td>BOY</td>
<td><a href="/wiki/Bobo_Dioulasso_Airport" title="Bobo Dioulasso Airport">Bobo Dioulasso Airport</a></td>
<td><a href="/wiki/Bobo_Dioulasso" class="mw-redirect" title="Bobo Dioulasso">Bobo Dioulasso</a>
</td></tr>
<tr>
<td>DFOT</td>
<td>TUQ</td>
<td><a href="/wiki/Tougan_Airport" title="Tougan Airport">Tougan Airport</a></td>
<td><a href="/wiki/Tougan" title="Tougan">Tougan</a>
</td></tr>
<tr>
<td>DFOU</td>
<td>XDE</td>
<td><a href="/wiki/Diebougou_Airport" class="mw-redirect" title="Diebougou Airport">Diebougou Airport</a></td>
<td><a href="/wiki/Diebougou" class="mw-redirect" title="Diebougou">Diebougou</a>
</td></tr>
<tr>
<td>DFOY</td>
<td>XAR</td>
<td><a href="/wiki/Aribinda_Airport" title="Aribinda Airport">Aribinda Airport</a></td>
<td><a href="/wiki/Aribinda" class="mw-redirect" title="Aribinda">Aribinda</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open('DF - Burkina Faso.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ICAO', 'IATA', 'Airport Name', 'Community']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    rows = table.find_all('tr')

    for row in rows[1:]:  # Ignorer la première ligne car c'est l'en-tête
        columns = row.find_all('td')
        icao = columns[0].text.strip()
        iata = columns[1].text.strip()
        airport_name = columns[2].text.strip()
        community = columns[3].text.strip()

        writer.writerow({'ICAO': icao, 'IATA': iata, 'Airport Name': airport_name, 'Community': community})

print("Le fichier CSV a été créé avec succès.")