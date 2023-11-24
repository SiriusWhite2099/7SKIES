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
<td>EBBE</td>
<td></td>
<td><a href="/wiki/Beauvechain_Air_Base" title="Beauvechain Air Base">Beauvechain Air Base</a></td>
<td><a href="/wiki/Beauvechain" title="Beauvechain">Beauvechain</a>
</td></tr>
<tr>
<td>EBBL</td>
<td></td>
<td><a href="/wiki/Kleine_Brogel_Air_Base" title="Kleine Brogel Air Base">Kleine Brogel Air Base</a></td>
<td><a href="/wiki/Peer,_Belgium" title="Peer, Belgium">Kleine Brogel</a>
</td></tr>
<tr>
<td>EBBX</td>
<td></td>
<td><a href="/wiki/Jehonville_Air_Base" title="Jehonville Air Base">Jehonville Air Base</a></td>
<td><a href="/wiki/Bertrix" title="Bertrix">Bertrix</a>
</td></tr>
<tr>
<td>EBCV</td>
<td></td>
<td><a href="/wiki/Chi%C3%A8vres_Air_Base" title="Chièvres Air Base">Chièvres Air Base</a></td>
<td><a href="/wiki/Chi%C3%A8vres" title="Chièvres">Chièvres</a>
</td></tr>
<tr>
<td>EBDT</td>
<td></td>
<td><a href="/wiki/Schaffen_Air_Base" title="Schaffen Air Base">Schaffen Air Base</a></td>
<td><a href="/wiki/Diest" title="Diest">Schaffen</a>
</td></tr>
<tr>
<td>EBFN</td>
<td></td>
<td><a href="/wiki/Koksijde_Air_Base" title="Koksijde Air Base">Koksijde Air Base</a></td>
<td><a href="/wiki/Koksijde" title="Koksijde">Koksijde</a>
</td></tr>
<tr>
<td>EBFS</td>
<td></td>
<td><a href="/wiki/Florennes_Air_Base" title="Florennes Air Base">Florennes Air Base</a></td>
<td><a href="/wiki/Florennes" title="Florennes">Florennes</a>
</td></tr>
<tr>
<td>EBLB</td>
<td></td>
<td><a href="/wiki/Elsenborn-Butgenbach_Air_Base" title="Elsenborn-Butgenbach Air Base">Elsenborn-Butgenbach Air Base</a></td>
<td><a href="/wiki/B%C3%BCtgenbach" title="Bütgenbach">Elsenborn</a><sup id="cite_ref-2" class="reference"><a href="#cite_note-2">[2]</a></sup>
</td></tr>
<tr>
<td>EBMB</td>
<td>BRU</td>
<td><a href="/wiki/Melsbroek_Air_Base" title="Melsbroek Air Base">Melsbroek Air Base</a></td>
<td><a href="/wiki/City_of_Brussels" title="City of Brussels">Brussels</a>/<a href="/wiki/Zaventem" title="Zaventem">Zaventem</a>
</td></tr>
<tr>
<td>EBSU</td>
<td></td>
<td><a href="/wiki/Saint-Hubert_Air_Base" title="Saint-Hubert Air Base">Saint-Hubert Air Base</a></td>
<td><a href="/wiki/Saint-Hubert,_Belgium" title="Saint-Hubert, Belgium">Saint-Hubert</a>
</td></tr>
<tr>
<td>EBUL</td>
<td></td>
<td><a href="/wiki/Ursel_Air_Base" title="Ursel Air Base">Ursel Air Base</a></td>
<td><a href="/wiki/Ursel" title="Ursel">Ursel</a>
</td></tr>
<tr>
<td>EBWE</td>
<td></td>
<td><a href="/wiki/Weelde_Air_Base" title="Weelde Air Base">Weelde Air Base</a></td>
<td><a href="/wiki/Weelde" title="Weelde">Weelde</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EB – Military airports.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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