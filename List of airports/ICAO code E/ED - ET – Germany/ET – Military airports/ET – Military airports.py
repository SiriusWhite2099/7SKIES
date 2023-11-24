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
<td>ETAD</td>
<td>SPM</td>
<td><a href="/wiki/Spangdahlem_Air_Base" title="Spangdahlem Air Base">Spangdahlem Air Base</a></td>
<td><a href="/wiki/Spangdahlem" title="Spangdahlem">Spangdahlem</a>
</td></tr>
<tr>
<td>ETAR</td>
<td>RMS</td>
<td><a href="/wiki/Ramstein_Air_Base" title="Ramstein Air Base">Ramstein Air Base</a></td>
<td><a href="/wiki/Ramstein-Miesenbach" title="Ramstein-Miesenbach">Ramstein</a>
</td></tr>
<tr>
<td><s>ETBB</s></td>
<td></td>
<td><s><a href="/wiki/Cologne_Butzweilerhof_Airport" title="Cologne Butzweilerhof Airport">Cologne Butzweilerhof Airport</a></s></td>
<td><s><a href="/wiki/Cologne" title="Cologne">Cologne</a></s></td>
<td></td>
<td>closed
</td></tr>
<tr>
<td>ETEB</td>
<td></td>
<td><a href="/wiki/Ansbach_Army_Heliport" class="mw-redirect" title="Ansbach Army Heliport">Ansbach Army Heliport</a></td>
<td><a href="/wiki/Ansbach" title="Ansbach">Ansbach</a>
</td></tr>
<tr>
<td><s>ETEJ</s></td>
<td></td>
<td><s><a href="/wiki/Bamberg-Breitenau_Airfield" title="Bamberg-Breitenau Airfield">Bamberg-Breitenau Airfield</a></s></td>
<td><s><a href="/wiki/Bamberg" title="Bamberg">Bamberg</a></s></td>
<td></td>
<td>see EDQA
</td></tr>
<tr>
<td>ETEK</td>
<td></td>
<td><a href="/wiki/Baumholder_Army_Airfield" title="Baumholder Army Airfield">Baumholder Army Airfield</a></td>
<td><a href="/wiki/Baumholder" title="Baumholder">Baumholder</a>
</td></tr>
<tr>
<td>ETHA</td>
<td></td>
<td><a href="/wiki/Altenstadt_Air_Base" title="Altenstadt Air Base">Altenstadt Air Base</a></td>
<td><a href="/wiki/Altenstadt,_Upper_Bavaria" title="Altenstadt, Upper Bavaria">Altenstadt</a>
</td></tr>
<tr>
<td>ETHB</td>
<td></td>
<td><a href="/wiki/B%C3%BCckeburg_Air_Base" title="Bückeburg Air Base">Bückeburg Air Base</a></td>
<td><a href="/wiki/B%C3%BCckeburg" title="Bückeburg">Bückeburg</a>
</td></tr>
<tr>
<td>ETHC</td>
<td>ZCN</td>
<td><a href="/wiki/Celle_Air_Base" title="Celle Air Base">Celle Air Base</a></td>
<td><a href="/wiki/Celle" title="Celle">Celle</a>
</td></tr>
<tr>
<td>ETHE</td>
<td>ZPQ</td>
<td><a href="/wiki/Rheine-Bentlage_Air_Base" title="Rheine-Bentlage Air Base">Rheine-Bentlage Air Base</a></td>
<td><a href="/wiki/Rheine" title="Rheine">Rheine</a>
</td></tr>
<tr>
<td>ETHF</td>
<td>FRZ</td>
<td><a href="/wiki/Fritzlar_Air_Base" title="Fritzlar Air Base">Fritzlar Air Base</a></td>
<td><a href="/wiki/Fritzlar" title="Fritzlar">Fritzlar</a>
</td></tr>
<tr>
<td>ETHL</td>
<td></td>
<td><a href="/wiki/Laupheim_Air_Base" title="Laupheim Air Base">Laupheim Air Base</a></td>
<td><a href="/wiki/Laupheim" title="Laupheim">Laupheim</a>
</td></tr>
<tr>
<td><s>ETHM</s></td>
<td></td>
<td><s><a href="/wiki/Mendig_Air_Base" title="Mendig Air Base">Mendig Air Base</a></s></td>
<td><a href="/wiki/Mendig" title="Mendig">Mendig</a></td>
<td></td>
<td>now Mendig Airfield - EDRE
</td></tr>
<tr>
<td>ETHN</td>
<td></td>
<td><a href="/wiki/Niederstetten_Air_Base" title="Niederstetten Air Base">Niederstetten Air Base</a></td>
<td><a href="/wiki/Niederstetten" title="Niederstetten">Niederstetten</a>
</td></tr>
<tr>
<td>ETHR</td>
<td></td>
<td><a href="/wiki/Roth_Air_Base" title="Roth Air Base">Roth Air Base</a></td>
<td><a href="/wiki/Roth_bei_N%C3%BCrnberg" class="mw-redirect" title="Roth bei Nürnberg">Roth</a>
</td></tr>
<tr>
<td>ETHS</td>
<td></td>
<td><a href="/wiki/Fa%C3%9Fberg_Air_Base" title="Faßberg Air Base">Faßberg Air Base</a></td>
<td><a href="/wiki/Fa%C3%9Fberg" title="Faßberg">Faßberg</a>
</td></tr>
<tr>
<td>ETHT</td>
<td></td>
<td><a href="/wiki/Cottbus_Air_Base" title="Cottbus Air Base">Cottbus Air Base</a></td>
<td><a href="/wiki/Cottbus" title="Cottbus">Cottbus</a>
</td></tr>
<tr>
<td>ETIC</td>
<td></td>
<td><a href="/wiki/Grafenw%C3%B6hr_Army_Airfield" title="Grafenwöhr Army Airfield">Grafenwöhr Army Airfield</a></td>
<td><a href="/wiki/Grafenw%C3%B6hr" title="Grafenwöhr">Grafenwöhr</a>
</td></tr>
<tr>
<td><s>ETID</s></td>
<td></td>
<td><s><a href="/wiki/Hanau_Army_Airfield" title="Hanau Army Airfield">Hanau Army Airfield</a></s></td>
<td><s><a href="/wiki/Erlensee" title="Erlensee">Erlensee</a></s></td>
<td><s><a href="/wiki/Hessen" class="mw-redirect" title="Hessen">Hessen</a></s></td>
<td>formerly <a href="/w/index.php?title=Fliegerhorst_Langendiebach&amp;action=edit&amp;redlink=1" class="new" title="Fliegerhorst Langendiebach (page does not exist)">Fliegerhorst Langendiebach</a>; closed in 2007
</td></tr>
<tr>
<td>ETIH</td>
<td></td>
<td><a href="/wiki/Hohenfels_Army_Airfield" title="Hohenfels Army Airfield">Hohenfels Army Airfield</a></td>
<td><a href="/wiki/Hohenfels,_Bavaria" title="Hohenfels, Bavaria">Hohenfels</a>
</td></tr>
<tr>
<td><s>ETIN</s></td>
<td><s>KZG</s></td>
<td><s><a href="/wiki/Kitzingen_Airport" title="Kitzingen Airport">Kitzingen Airport</a></s></td>
<td><s><a href="/wiki/Kitzingen" title="Kitzingen">Kitzingen</a></s></td>
<td><s><a href="/wiki/Bavaria" title="Bavaria">Bavaria</a></s></td>
<td>formerly <a href="/wiki/Kitzingen_Army_Airfield" title="Kitzingen Army Airfield">Kitzingen Army Airfield</a>; closed in 2007
</td></tr>
<tr>
<td>ETMN</td>
<td>FCN</td>
<td><a href="/wiki/Sea-Airport_Cuxhaven/Nordholz" title="Sea-Airport Cuxhaven/Nordholz">Sea-Airport Cuxhaven/Nordholz</a> (<a href="/wiki/Nordholz_Naval_Airbase" title="Nordholz Naval Airbase">Nordholz Naval Airbase</a>)</td>
<td><a href="/wiki/Nordholz" title="Nordholz">Nordholz</a>
</td></tr>
<tr>
<td>ETND</td>
<td></td>
<td><a href="/wiki/Diepholz_Air_Base" title="Diepholz Air Base">Diepholz Air Base</a></td>
<td><a href="/wiki/Diepholz" title="Diepholz">Diepholz</a>
</td></tr>
<tr>
<td>ETNG</td>
<td>GKE</td>
<td><a href="/wiki/NATO_Air_Base_Geilenkirchen" title="NATO Air Base Geilenkirchen">NATO Air Base Geilenkirchen</a></td>
<td><a href="/wiki/Geilenkirchen" title="Geilenkirchen">Geilenkirchen</a>
</td></tr>
<tr>
<td>ETNH</td>
<td></td>
<td><a href="/wiki/Hohn_Air_Base" title="Hohn Air Base">Hohn Air Base</a></td>
<td><a href="/wiki/Hohn,_Schleswig-Holstein" title="Hohn, Schleswig-Holstein">Hohn</a>
</td></tr>
<tr>
<td>ETNJ</td>
<td></td>
<td><a href="/wiki/Jever_Air_Base" title="Jever Air Base">Jever Air Base</a></td>
<td><a href="/wiki/Schortens" title="Schortens">Schortens</a>
</td></tr>
<tr>
<td>ETNK</td>
<td></td>
<td><a href="/w/index.php?title=Wahn_Air_Base&amp;action=edit&amp;redlink=1" class="new" title="Wahn Air Base (page does not exist)">Wahn Air Base</a></td>
<td><a href="/wiki/Cologne" title="Cologne">Cologne</a>/<a href="/wiki/Bonn" title="Bonn">Bonn</a></td>
<td></td>
<td>military part of <a href="/wiki/Cologne_Bonn_Airport" title="Cologne Bonn Airport">Cologne Bonn Airport</a>
</td></tr>
<tr>
<td>ETNL</td>
<td>RLG</td>
<td><a href="/wiki/Rostock_Laage_Airport" class="mw-redirect" title="Rostock Laage Airport">Rostock Laage Airport</a></td>
<td><a href="/wiki/Rostock" title="Rostock">Rostock</a>
</td></tr>
<tr>
<td>ETNN</td>
<td></td>
<td><a href="/wiki/N%C3%B6rvenich_Air_Base" title="Nörvenich Air Base">Nörvenich Air Base</a></td>
<td><a href="/wiki/N%C3%B6rvenich" title="Nörvenich">Nörvenich</a>
</td></tr>
<tr>
<td>ETNP</td>
<td></td>
<td><a href="/wiki/Rheine-Hopsten_Air_Base" title="Rheine-Hopsten Air Base">Rheine-Hopsten Air Base</a></td>
<td><a href="/wiki/Rheine" title="Rheine">Rheine</a>
</td></tr>
<tr>
<td>ETNS</td>
<td>WBG</td>
<td><a href="/wiki/Schleswig_Air_Base" title="Schleswig Air Base">Schleswig Air Base</a></td>
<td><a href="/wiki/Schleswig" class="mw-redirect" title="Schleswig">Schleswig</a>
</td></tr>
<tr>
<td>ETNT</td>
<td></td>
<td><a href="/wiki/Wittmundhafen_Air_Base" title="Wittmundhafen Air Base">Wittmundhafen Air Base</a></td>
<td><a href="/wiki/Wittmund" title="Wittmund">Wittmund</a>
</td></tr>
<tr>
<td><s>ETNU</s></td>
<td><s>FNB</s></td>
<td><s><a href="/wiki/Neubrandenburg_Airport" title="Neubrandenburg Airport">Neubrandenburg Airport</a></s></td>
<td><a href="/wiki/Neubrandenburg" title="Neubrandenburg">Neubrandenburg</a></td>
<td></td>
<td>see EDBN
</td></tr>
<tr>
<td>ETNW</td>
<td></td>
<td><a href="/wiki/Wunstorf_Air_Base" title="Wunstorf Air Base">Wunstorf Air Base</a></td>
<td><a href="/wiki/Wunstorf" title="Wunstorf">Wunstorf</a>
</td></tr>
<tr>
<td>ETOR</td>
<td></td>
<td><a href="/wiki/Coleman_Army_Airfield" title="Coleman Army Airfield">Coleman Army Airfield</a></td>
<td><a href="/wiki/Mannheim" title="Mannheim">Mannheim</a>
</td></tr>
<tr>
<td>ETOU</td>
<td>WIE</td>
<td><a href="/wiki/Wiesbaden_Army_Airfield" class="mw-redirect" title="Wiesbaden Army Airfield">Wiesbaden Army Airfield</a></td>
<td><a href="/wiki/Wiesbaden" title="Wiesbaden">Wiesbaden</a>
</td></tr>
<tr>
<td>ETSA</td>
<td></td>
<td><a href="/wiki/Landsberg-Lech_Air_Base" title="Landsberg-Lech Air Base">Landsberg-Lech Air Base</a></td>
<td><a href="/wiki/Landsberg_am_Lech" title="Landsberg am Lech">Landsberg am Lech</a>
</td></tr>
<tr>
<td>ETSB</td>
<td></td>
<td><a href="/wiki/B%C3%BCchel_Air_Base" title="Büchel Air Base">Büchel Air Base</a></td>
<td><a href="/wiki/B%C3%BCchel_(municipality)" title="Büchel (municipality)">Büchel</a> / <a href="/wiki/Cochem" title="Cochem">Cochem</a>
</td></tr>
<tr>
<td>ETSE</td>
<td></td>
<td><a href="/wiki/Erding_Air_Base" title="Erding Air Base">Erding Air Base</a></td>
<td><a href="/wiki/Erding" title="Erding">Erding</a>
</td></tr>
<tr>
<td><s>ETSF</s></td>
<td><s>FEL</s></td>
<td><s><a href="/wiki/F%C3%BCrstenfeldbruck_Air_Base" title="Fürstenfeldbruck Air Base">Fürstenfeldbruck Air Base</a></s></td>
<td><a href="/wiki/F%C3%BCrstenfeldbruck" title="Fürstenfeldbruck">Fürstenfeldbruck</a></td>
<td></td>
<td>closed 2010
</td></tr>
<tr>
<td>ETSH</td>
<td></td>
<td><a href="/wiki/Holzdorf_Air_Base" title="Holzdorf Air Base">Holzdorf Air Base</a></td>
<td><a href="/wiki/Jessen_(Elster)" title="Jessen (Elster)">Jessen (Elster)</a>
</td></tr>
<tr>
<td>ETSI</td>
<td>IGS</td>
<td><a href="/wiki/Ingolstadt_Manching_Airport" title="Ingolstadt Manching Airport">Ingolstadt Manching Airport</a></td>
<td><a href="/wiki/Ingolstadt" title="Ingolstadt">Ingolstadt</a>
</td></tr>
<tr>
<td>ETSK</td>
<td></td>
<td><a href="/wiki/Kaufbeuren_Air_Base" title="Kaufbeuren Air Base">Kaufbeuren Air Base</a></td>
<td><a href="/wiki/Kaufbeuren" title="Kaufbeuren">Kaufbeuren</a>
</td></tr>
<tr>
<td>ETSL</td>
<td></td>
<td><a href="/wiki/Lechfeld_Air_Base" title="Lechfeld Air Base">Lechfeld Air Base</a></td>
<td><a href="/wiki/Lechfeld" class="mw-redirect" title="Lechfeld">Lechfeld</a>
</td></tr>
<tr>
<td>ETSN</td>
<td>NEU</td>
<td><a href="/wiki/Neuburg_Air_Base" title="Neuburg Air Base">Neuburg Air Base</a></td>
<td><a href="/wiki/Neuburg_an_der_Donau" title="Neuburg an der Donau">Neuburg</a>
</td></tr>
<tr>
<td>ETUL</td>
<td>LRC</td>
<td><a href="/wiki/RAF_Laarbruch" title="RAF Laarbruch">RAF Laarbruch</a></td>
<td><a href="/wiki/Weeze" title="Weeze">Weeze</a></td>
<td></td>
<td>closed in 1999; now <a href="/wiki/Weeze_Airport" title="Weeze Airport">Weeze Airport</a>; see EDLV
</td></tr>
<tr>
<td>ETUO</td>
<td>GUT</td>
<td><a href="/wiki/RAF_G%C3%BCtersloh" title="RAF Gütersloh">RAF Gütersloh</a></td>
<td><a href="/wiki/G%C3%BCtersloh" title="Gütersloh">Gütersloh</a></td>
<td></td>
<td>closed in 1993
</td></tr>
<tr>
<td>ETUR</td>
<td>BGN</td>
<td><a href="/wiki/RAF_Br%C3%BCggen" class="mw-redirect" title="RAF Brüggen">RAF Brüggen</a></td>
<td><a href="/wiki/Br%C3%BCggen,_Germany" title="Brüggen, Germany">Brüggen</a></td>
<td></td>
<td>closed in 2001
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("ET – Military airports.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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