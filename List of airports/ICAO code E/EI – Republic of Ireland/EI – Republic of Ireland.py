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
<td>EIAB</td>
<td></td>
<td><a href="/wiki/Abbeyshrule_Aerodrome" title="Abbeyshrule Aerodrome">Abbeyshrule Aerodrome</a></td>
<td><a href="/wiki/Abbeyshrule" title="Abbeyshrule">Abbeyshrule</a></td>
<td><a href="/wiki/County_Longford" title="County Longford">County Longford</a>
</td></tr>
<tr>
<td>EIBN</td>
<td>BYT</td>
<td><a href="/wiki/Bantry_Aerodrome" title="Bantry Aerodrome">Bantry Aerodrome</a></td>
<td><a href="/wiki/Bantry" title="Bantry">Bantry</a></td>
<td><a href="/wiki/County_Cork" title="County Cork">County Cork</a>
</td></tr>
<tr>
<td>EIBR</td>
<td></td>
<td><a href="/wiki/Birr_Aerodrome" title="Birr Aerodrome">Birr Aerodrome</a></td>
<td><a href="/wiki/Birr,_County_Offaly" title="Birr, County Offaly">Birr</a></td>
<td><a href="/wiki/County_Offaly" title="County Offaly">County Offaly</a>
</td></tr>
<tr>
<td>EICA</td>
<td>NNR</td>
<td><a href="/wiki/Connemara_Regional_Airport" class="mw-redirect" title="Connemara Regional Airport">Connemara Regional Airport</a></td>
<td><a href="/wiki/Inverin" title="Inverin">Inverin</a></td>
<td><a href="/wiki/Connemara" title="Connemara">Connemara</a>
</td></tr>
<tr>
<td>EICB</td>
<td></td>
<td><a href="/w/index.php?title=Castlebar_Airport&amp;action=edit&amp;redlink=1" class="new" title="Castlebar Airport (page does not exist)">Castlebar Airport</a></td>
<td><a href="/wiki/Castlebar" title="Castlebar">Castlebar</a></td>
<td><a href="/wiki/County_Mayo" title="County Mayo">County Mayo</a>
</td></tr>
<tr>
<td>EICK</td>
<td>ORK</td>
<td><a href="/wiki/Cork_International_Airport" class="mw-redirect" title="Cork International Airport">Cork International Airport</a></td>
<td><a href="/wiki/Cork_(city)" title="Cork (city)">Cork</a></td>
<td>
</td></tr>
<tr>
<td>EICL</td>
<td></td>
<td><a href="/wiki/Clonbullogue_Aerodrome" class="mw-redirect" title="Clonbullogue Aerodrome">Clonbullogue Aerodrome</a></td>
<td><a href="/wiki/Clonbullogue" title="Clonbullogue">Clonbullogue</a></td>
<td><a href="/wiki/County_Offaly" title="County Offaly">County Offaly</a>
</td></tr>
<tr>
<td>EICM</td>
<td>GWY</td>
<td><a href="/wiki/Galway_Airport" title="Galway Airport">Galway Airport</a></td>
<td><a href="/wiki/Carnmore" title="Carnmore">Carnmore</a></td>
<td><a href="/wiki/County_Galway" title="County Galway">County Galway</a>
</td></tr>
<tr>
<td>EICN</td>
<td></td>
<td><a href="/wiki/Coonagh_Airport" class="mw-redirect" title="Coonagh Airport">Coonagh Airport</a></td>
<td><a href="/wiki/Limerick" title="Limerick">Limerick</a></td>
<td><a href="/wiki/County_Limerick" title="County Limerick">County Limerick</a>
</td></tr>
<tr>
<td>EIDL</td>
<td>CFN</td>
<td><a href="/wiki/Donegal_Airport" title="Donegal Airport">Donegal Airport</a></td>
<td><a href="/w/index.php?title=Carrickfinn&amp;action=edit&amp;redlink=1" class="new" title="Carrickfinn (page does not exist)">Carrickfinn</a></td>
<td><a href="/wiki/County_Donegal" title="County Donegal">County Donegal</a>
</td></tr>
<tr>
<td>EIDW</td>
<td>DUB</td>
<td><a href="/wiki/Dublin_Airport" title="Dublin Airport">Dublin Airport</a></td>
<td><a href="/wiki/Dublin,_Ireland" class="mw-redirect" title="Dublin, Ireland">Dublin</a></td>
<td>
</td></tr>
<tr>
<td>EIIM</td>
<td>IOR</td>
<td><a href="/wiki/Inishmore_Aerodrome" title="Inishmore Aerodrome">Inishmore Aerodrome</a> (Kilronan Airport)</td>
<td><a href="/wiki/Kilronan" title="Kilronan">Kilronan</a></td>
<td><a href="/wiki/County_Galway" title="County Galway">County Galway</a>
</td></tr>
<tr>
<td>EIKL</td>
<td>KKY</td>
<td><a href="/wiki/Kilkenny_Airport" title="Kilkenny Airport">Kilkenny Airport</a></td>
<td><a href="/wiki/Kilkenny" title="Kilkenny">Kilkenny</a></td>
<td><a href="/wiki/County_Kilkenny" title="County Kilkenny">County Kilkenny</a>
</td></tr>
<tr>
<td>EIKN</td>
<td>NOC</td>
<td><a href="/wiki/Ireland_West_Airport_Knock" class="mw-redirect" title="Ireland West Airport Knock">Ireland West Airport Knock</a></td>
<td><a href="/wiki/Knock,_County_Mayo" title="Knock, County Mayo">Knock</a></td>
<td><a href="/wiki/County_Mayo" title="County Mayo">County Mayo</a>
</td></tr>
<tr>
<td>EIKY</td>
<td>KIR</td>
<td><a href="/wiki/Kerry_Airport" title="Kerry Airport">Kerry Airport</a></td>
<td><a href="/wiki/Farranfore" title="Farranfore">Farranfore</a></td>
<td><a href="/wiki/County_Kerry" title="County Kerry">County Kerry</a>
</td></tr>
<tr>
<td>EILT</td>
<td>LKY</td>
<td><a href="/w/index.php?title=Letterkenny_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Letterkenny Airfield (page does not exist)">Letterkenny Airfield</a></td>
<td><a href="/wiki/Letterkenny" title="Letterkenny">Letterkenny</a></td>
<td><a href="/wiki/County_Donegal" title="County Donegal">County Donegal</a>
</td></tr>
<tr>
<td>EIME</td>
<td></td>
<td><a href="/wiki/Casement_Aerodrome" title="Casement Aerodrome">Casement Aerodrome</a></td>
<td><a href="/wiki/Baldonnel,_Ireland" class="mw-redirect" title="Baldonnel, Ireland">Baldonnel</a></td>
<td>
</td></tr>
<tr>
<td>EIMH</td>
<td></td>
<td><a href="/w/index.php?title=Athboy_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Athboy Airfield (page does not exist)">Athboy Airfield</a></td>
<td><a href="/wiki/Athboy" title="Athboy">Athboy</a></td>
<td><a href="/wiki/County_Meath" title="County Meath">County Meath</a>
</td></tr>
<tr>
<td>EIMY</td>
<td></td>
<td><a href="/wiki/Moyne_Aerodrome" title="Moyne Aerodrome">Moyne Aerodrome</a></td>
<td><a href="/wiki/Thurles" title="Thurles">Thurles</a></td>
<td><a href="/wiki/County_Tipperary" title="County Tipperary">County Tipperary</a>
</td></tr>
<tr>
<td>EINN</td>
<td>SNN</td>
<td><a href="/wiki/Shannon_Airport" title="Shannon Airport">Shannon Airport</a></td>
<td><a href="/wiki/Shannon,_Ireland" class="mw-redirect" title="Shannon, Ireland">Shannon</a></td>
<td><a href="/wiki/County_Clare" title="County Clare">County Clare</a>
</td></tr>
<tr>
<td>EIRT</td>
<td></td>
<td><a href="/wiki/Rathcoole_Aerodrome" title="Rathcoole Aerodrome">Rathcoole Aerodrome</a></td>
<td><a href="/wiki/Rathcoole,_County_Cork" title="Rathcoole, County Cork">Rathcoole</a> (<i>Ráth Chúil</i>)</td>
<td><a href="/wiki/County_Cork" title="County Cork">County Cork</a> (<i>Contae Chorcaí</i>)
</td></tr>
<tr>
<td>EISG</td>
<td>SXL</td>
<td><a href="/wiki/Sligo_Airport" title="Sligo Airport">Sligo Airport</a></td>
<td><a href="/wiki/Strandhill" title="Strandhill">Strandhill</a>, near <a href="/wiki/Sligo_Town" class="mw-redirect" title="Sligo Town">Sligo</a></td>
<td>
</td></tr>
<tr>
<td>EIWF</td>
<td>WAT</td>
<td><a href="/wiki/Waterford_Airport" title="Waterford Airport">Waterford Airport</a></td>
<td><a href="/wiki/Waterford" title="Waterford">Waterford</a></td>
<td>
</td></tr>
<tr>
<td>EIWT</td>
<td>WST</td>
<td><a href="/wiki/Weston_Airport" title="Weston Airport">Weston Airport</a></td>
<td><a href="/wiki/Leixlip" title="Leixlip">Leixlip</a></td>
<td><a href="/wiki/County_Kildare" title="County Kildare">County Kildare</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EI – Republic of Ireland.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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