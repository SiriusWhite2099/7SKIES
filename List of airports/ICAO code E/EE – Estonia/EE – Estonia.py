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
<td>EECL</td>
<td></td>
<td><a href="/wiki/Linnahall_Heliport" class="mw-redirect" title="Linnahall Heliport">Linnahall Heliport</a></td>
<td><a href="/wiki/Tallinn" title="Tallinn">Tallinn</a>
</td></tr>
<tr>
<td>EEEI</td>
<td></td>
<td><a href="/wiki/%C3%84mari_Air_Base" title="Ämari Air Base">Ämari Air Base</a></td>
<td><a href="/wiki/%C3%84mari" title="Ämari">Ämari</a>
</td></tr>
<tr>
<td>EEHU</td>
<td></td>
<td><a href="/wiki/Haapsalu_Airfield" class="mw-redirect" title="Haapsalu Airfield">Haapsalu Airfield</a></td>
<td><a href="/wiki/Haapsalu" title="Haapsalu">Haapsalu</a>
</td></tr>
<tr>
<td>EEJI</td>
<td></td>
<td><a href="/wiki/J%C3%B5hvi_Airfield" title="Jõhvi Airfield">Jõhvi Airfield</a></td>
<td><a href="/wiki/J%C3%B5hvi" title="Jõhvi">Jõhvi</a>
</td></tr>
<tr>
<td>EEKA</td>
<td>KDL</td>
<td><a href="/wiki/K%C3%A4rdla_Airport" title="Kärdla Airport">Kärdla Airport</a></td>
<td><a href="/wiki/K%C3%A4rdla" title="Kärdla">Kärdla</a>
</td></tr>
<tr>
<td>EEKE</td>
<td>URE</td>
<td><a href="/wiki/Kuressaare_Airport" title="Kuressaare Airport">Kuressaare Airport</a></td>
<td><a href="/wiki/Kuressaare" title="Kuressaare">Kuressaare</a>
</td></tr>
<tr>
<td>EEKU</td>
<td></td>
<td><a href="/wiki/Kihnu_Airfield" title="Kihnu Airfield">Kihnu Airfield</a></td>
<td><a href="/wiki/Kihnu" title="Kihnu">Kihnu</a>
</td></tr>
<tr>
<td>EELU</td>
<td></td>
<td><a href="/wiki/Lyckholm_Airfield" title="Lyckholm Airfield">Lyckholm Airfield</a></td>
<td><a href="/wiki/Saare,_L%C3%A4%C3%A4ne_County" title="Saare, Lääne County">Saare</a>
</td></tr>
<tr>
<td>EENI</td>
<td></td>
<td><a href="/wiki/Nurmsi_Airfield" title="Nurmsi Airfield">Nurmsi Airfield</a></td>
<td><a href="/wiki/Nurmsi,_J%C3%A4rva_County" title="Nurmsi, Järva County">Nurmsi</a>
</td></tr>
<tr>
<td>EENA</td>
<td></td>
<td><a href="/wiki/Narva_Airfield" title="Narva Airfield">Narva Airfield</a></td>
<td><a href="/wiki/Narva" title="Narva">Narva</a>
</td></tr>
<tr>
<td>EEPR</td>
<td></td>
<td><a href="/wiki/Piirissaare_Airfield" title="Piirissaare Airfield">Piirissaare Airfield</a></td>
<td><a href="/wiki/Piirissaar" title="Piirissaar">Piirissaar</a>
</td></tr>
<tr>
<td>EEPU</td>
<td>EPU</td>
<td><a href="/wiki/P%C3%A4rnu_Airport" title="Pärnu Airport">Pärnu Airport</a></td>
<td><a href="/wiki/P%C3%A4rnu" title="Pärnu">Pärnu</a>
</td></tr>
<tr>
<td>EERA</td>
<td></td>
<td><a href="/wiki/Rapla_Airfield" title="Rapla Airfield">Rapla Airfield</a></td>
<td><a href="/wiki/Rapla" title="Rapla">Rapla</a>
</td></tr>
<tr>
<td>EERI</td>
<td></td>
<td><a href="/wiki/Ridali_Airfield" title="Ridali Airfield">Ridali Airfield</a></td>
<td><a href="/wiki/Ridali" class="mw-redirect" title="Ridali">Ridali</a>
</td></tr>
<tr>
<td>EERU</td>
<td></td>
<td><a href="/wiki/Ruhnu_Airfield" title="Ruhnu Airfield">Ruhnu Airfield</a></td>
<td><a href="/wiki/Ruhnu" title="Ruhnu">Ruhnu</a>
</td></tr>
<tr>
<td>EETA</td>
<td></td>
<td><a href="/wiki/Tapa_Airfield" title="Tapa Airfield">Tapa Airfield</a></td>
<td><a href="/wiki/Tapa,_Estonia" title="Tapa, Estonia">Tapa</a>
</td></tr>
<tr>
<td>EETN</td>
<td>TLL</td>
<td><a href="/wiki/Lennart_Meri_Tallinn_Airport" class="mw-redirect" title="Lennart Meri Tallinn Airport">Lennart Meri Tallinn Airport</a></td>
<td><a href="/wiki/Tallinn" title="Tallinn">Tallinn</a>
</td></tr>
<tr>
<td>EETR</td>
<td></td>
<td><a href="/wiki/Raadi_Airfield" title="Raadi Airfield">Raadi Airfield</a></td>
<td><a href="/wiki/Tartu" title="Tartu">Tartu</a>
</td></tr>
<tr>
<td>EETU</td>
<td>TAY</td>
<td><a href="/wiki/Tartu_Airport" title="Tartu Airport">Tartu Airport</a></td>
<td><a href="/wiki/Tartu" title="Tartu">Tartu</a>
</td></tr>
<tr>
<td>EEVI</td>
<td></td>
<td><a href="/wiki/Viljandi_Airfield" title="Viljandi Airfield">Viljandi Airfield</a></td>
<td><a href="/wiki/Viljandi" title="Viljandi">Viljandi</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EE – Estonia.csv", mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ICAO', 'IATA', 'Airport Name', 'Community', 'Province or Territory', 'Notes']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in table.find_all('tr')[1:]:
        columns = row.find_all(['td', 'th'])
        row_data = {}

        for i, column in enumerate(columns):
            row_data[fieldnames[i]] = column.text.strip() if column.text.strip() else None

        writer.writerow(row_data)

print("Le fichier CSV a été créé avec succès.")