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
<td>EHAL</td>
<td></td>
<td><a href="/wiki/Ameland_Airport" title="Ameland Airport">Ameland Airport</a></td>
<td><a href="/wiki/Ballum" title="Ballum">Ballum</a>
</td></tr>
<tr>
<td>EHAM</td>
<td>AMS</td>
<td><a href="/wiki/Amsterdam_Airport_Schiphol" title="Amsterdam Airport Schiphol">Amsterdam Airport Schiphol</a></td>
<td><a href="/wiki/Haarlemmermeer" title="Haarlemmermeer">Haarlemmermeer</a>, near <a href="/wiki/Amsterdam" title="Amsterdam">Amsterdam</a>
</td></tr>
<tr>
<td>EHBD</td>
<td></td>
<td><a href="/wiki/Budel_Airport" class="mw-redirect" title="Budel Airport">Budel Airport</a></td>
<td><a href="/wiki/Weert" title="Weert">Weert</a>
</td></tr>
<tr>
<td>EHBK</td>
<td>MST</td>
<td><a href="/wiki/Maastricht_Aachen_Airport" title="Maastricht Aachen Airport">Maastricht Aachen Airport</a></td>
<td><a href="/wiki/Beek" title="Beek">Beek</a>
</td></tr>
<tr>
<td>EHDL</td>
<td></td>
<td><a href="/wiki/Deelen_Airbase" class="mw-redirect" title="Deelen Airbase">Deelen Airbase</a></td>
<td><a href="/wiki/Deelen" title="Deelen">Deelen</a>
</td></tr>
<tr>
<td>EHDP</td>
<td></td>
<td><a href="/wiki/Lieutenant_General_Best_Barracks" title="Lieutenant General Best Barracks">De Peel Airbase</a></td>
<td><a href="/wiki/Venray" title="Venray">Venray</a>
</td></tr>
<tr>
<td>EHDR</td>
<td></td>
<td><a href="/wiki/Drachten_Airfield" title="Drachten Airfield">Drachten Airfield</a></td>
<td><a href="/wiki/Drachten" title="Drachten">Drachten</a>
</td></tr>
<tr>
<td>EHEH</td>
<td>EIN</td>
<td><a href="/wiki/Eindhoven_Airport" title="Eindhoven Airport">Eindhoven Airport</a></td>
<td><a href="/wiki/Eindhoven" title="Eindhoven">Eindhoven</a>
</td></tr>
<tr>
<td>EHGG</td>
<td>GRQ</td>
<td><a href="/wiki/Groningen_Airport_Eelde" title="Groningen Airport Eelde">Groningen Airport Eelde</a></td>
<td><a href="/wiki/Eelde" title="Eelde">Eelde</a>
</td></tr>
<tr>
<td>EHGR</td>
<td>GLZ</td>
<td><a href="/wiki/Gilze-Rijen_Airbase" class="mw-redirect" title="Gilze-Rijen Airbase">Gilze-Rijen Airbase</a></td>
<td><a href="/wiki/Gilze" class="mw-redirect" title="Gilze">Gilze</a> and <a href="/wiki/Rijen" title="Rijen">Rijen</a>
</td></tr>
<tr>
<td>EHHE</td>
<td></td>
<td><a href="/w/index.php?title=Eemshaven_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Eemshaven Heliport (page does not exist)">Eemshaven Heliport</a>
</td></tr>
<tr>
<td>EHHO</td>
<td></td>
<td><a href="/wiki/Hoogeveen_Airfield" class="mw-redirect" title="Hoogeveen Airfield">Hoogeveen Airfield</a></td>
<td><a href="/wiki/Hoogeveen" title="Hoogeveen">Hoogeveen</a>
</td></tr>
<tr>
<td>EHHV</td>
<td></td>
<td><a href="/wiki/Hilversum_Airfield" title="Hilversum Airfield">Hilversum Airfield</a></td>
<td><a href="/wiki/Hilversum" title="Hilversum">Hilversum</a>
</td></tr>
<tr>
<td>EHKD</td>
<td>DHR</td>
<td><a href="/wiki/De_Kooy_Airfield" title="De Kooy Airfield">De Kooy Airfield</a></td>
<td><a href="/wiki/De_Kooy" title="De Kooy">De Kooy</a>
</td></tr>
<tr>
<td>EHLE</td>
<td>LEY</td>
<td><a href="/wiki/Lelystad_Airport" title="Lelystad Airport">Lelystad Airport</a></td>
<td><a href="/wiki/Lelystad" title="Lelystad">Lelystad</a>
</td></tr>
<tr>
<td>EHLW</td>
<td>LWR</td>
<td><a href="/wiki/Leeuwarden_Air_Base" title="Leeuwarden Air Base">Leeuwarden Air Base</a></td>
<td><a href="/wiki/Leeuwarden" title="Leeuwarden">Leeuwarden</a>
</td></tr>
<tr>
<td>EHMM
</td>
<td>
</td>
<td><a href="/wiki/Vliegveld_Middenmeer" class="mw-redirect" title="Vliegveld Middenmeer">Vliegveld Middenmeer</a>
</td>
<td><a href="/wiki/Middenmeer" title="Middenmeer">Middenmeer</a>
</td></tr>
<tr>
<td>EHMZ</td>
<td></td>
<td><a href="/wiki/Midden-Zeeland_Airport" title="Midden-Zeeland Airport">Midden-Zeeland Airport</a></td>
<td><a href="/wiki/Middelburg,_Zeeland" title="Middelburg, Zeeland">Middelburg</a></td>
<td><a href="/wiki/Zeeland" title="Zeeland">Zeeland</a>
</td></tr>
<tr>
<td>EHND</td>
<td></td>
<td><a href="/wiki/Numansdorp_Airfield" title="Numansdorp Airfield">Numansdorp Airfield</a></td>
<td><a href="/wiki/Numansdorp" title="Numansdorp">Numansdorp</a>
</td></tr>
<tr>
<td>EHOW</td>
<td></td>
<td><a href="/wiki/Oostwold_Airport" title="Oostwold Airport">Oostwold Airport</a></td>
<td><a href="/wiki/Scheemda" title="Scheemda">Scheemda</a>
</td></tr>
<tr>
<td>EHRD</td>
<td>RTM</td>
<td><a href="/wiki/Rotterdam_The_Hague_Airport" title="Rotterdam The Hague Airport">Rotterdam The Hague Airport</a></td>
<td><a href="/wiki/Rotterdam" title="Rotterdam">Rotterdam</a>
</td></tr>
<tr>
<td><s>EHSB</s></td>
<td>SSB</td>
<td><a href="/wiki/Soesterberg_Air_Base" title="Soesterberg Air Base">Soesterberg Air Base</a></td>
<td><a href="/wiki/Soesterberg" title="Soesterberg">Soesterberg</a></td>
<td></td>
<td>closed in 2015 as transferred into National Military Museum
</td></tr>
<tr>
<td>EHSE</td>
<td></td>
<td><a href="/wiki/Breda_International_Airport" title="Breda International Airport">Breda International Airport</a></td>
<td><a href="/wiki/Hoeven" title="Hoeven">Hoeven</a>
</td></tr>
<tr>
<td>EHST</td>
<td></td>
<td><a href="/wiki/Stadskanaal_Airfield" title="Stadskanaal Airfield">Stadskanaal Airfield</a></td>
<td><a href="/wiki/Stadskanaal" title="Stadskanaal">Stadskanaal</a>
</td></tr>
<tr>
<td>EHTE</td>
<td></td>
<td><a href="/wiki/Teuge_International_Airport" class="mw-redirect" title="Teuge International Airport">Teuge International Airport</a></td>
<td><a href="/wiki/Deventer" title="Deventer">Deventer</a>
</td></tr>
<tr>
<td>EHTL</td>
<td></td>
<td><a href="/wiki/Terlet_Airfield" title="Terlet Airfield">Terlet Airfield</a></td>
<td><a href="/wiki/Terlet" class="mw-redirect" title="Terlet">Terlet</a>
</td></tr>
<tr>
<td>EHTW</td>
<td>ENS</td>
<td><a href="/wiki/Enschede_Airport_Twente" title="Enschede Airport Twente">Enschede Airport Twente</a></td>
<td><a href="/wiki/Enschede" title="Enschede">Enschede</a>
</td></tr>
<tr>
<td>EHTX</td>
<td></td>
<td><a href="/wiki/Texel_International_Airport" title="Texel International Airport">Texel International Airport</a></td>
<td><a href="/wiki/Texel" title="Texel">Texel</a>
</td></tr>
<tr>
<td><s>EHVB</s></td>
<td></td>
<td><a href="/wiki/Valkenburg_Airbase" class="mw-redirect" title="Valkenburg Airbase">Valkenburg Airbase</a></td>
<td><a href="/wiki/Valkenburg_(South_Holland)" class="mw-redirect" title="Valkenburg (South Holland)">Valkenburg</a></td>
<td></td>
<td>closed circa 2000
</td></tr>
<tr>
<td><s>EHVE</s></td>
<td></td>
<td><s><a href="/wiki/TrafficPort_Venlo" title="TrafficPort Venlo">TrafficPort Venlo</a></s></td>
<td><a href="/wiki/Venlo" title="Venlo">Venlo</a></td>
<td></td>
<td>closed
</td></tr>
<tr>
<td>EHVK</td>
<td>UDE</td>
<td><a href="/wiki/Volkel_Airbase" class="mw-redirect" title="Volkel Airbase">Volkel Airbase</a></td>
<td><a href="/wiki/Uden" title="Uden">Uden</a>
</td></tr>
<tr>
<td>EHWO</td>
<td>WOE</td>
<td><a href="/wiki/Woensdrecht_Air_Base" title="Woensdrecht Air Base">Woensdrecht Air Base</a></td>
<td><a href="/wiki/Woensdrecht" title="Woensdrecht">Woensdrecht</a>
</td></tr>
<tr>
<td><s>EHYB</s></td>
<td></td>
<td><a href="/wiki/Ypenburg_Airport" title="Ypenburg Airport">Ypenburg Airport</a></td>
<td><a href="/wiki/The_Hague" title="The Hague">The Hague</a></td>
<td></td>
<td>closed 1991
</td></tr>
<tr>
<td>EHYP</td>
<td></td>
<td><a href="/wiki/IJmuiden_Heliport" title="IJmuiden Heliport">IJmuiden Heliport</a></td>
<td><a href="/wiki/IJmuiden" title="IJmuiden">IJmuiden</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EH – Netherlands.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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