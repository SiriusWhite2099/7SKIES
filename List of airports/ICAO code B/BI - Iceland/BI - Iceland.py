from bs4 import BeautifulSoup
import csv

html_content = '''
<table class="wikitable" style="width:auto;">
<tbody><tr>
<th width="*"><a href="/wiki/ICAO_airport_code" title="ICAO airport code">ICAO</a>
</th>
<th width="*"><a href="/wiki/IATA_airport_code" title="IATA airport code">IATA</a>
</th>
<th width="*">Airport name
</th>
<th width="*">Community
</th></tr>
<tr>
<td>BIAR</td>
<td>AEY</td>
<td><a href="/wiki/Akureyri_Airport" title="Akureyri Airport">Akureyri Airport</a></td>
<td><a href="/wiki/Akureyri" title="Akureyri">Akureyri</a>
</td></tr>
<tr>
<td>BIBA</td>
<td></td>
<td><a href="/wiki/Bakki_Airport" title="Bakki Airport">Bakki Airport</a></td>
<td><a href="/w/index.php?title=Bakki&amp;action=edit&amp;redlink=1" class="new" title="Bakki (page does not exist)">Bakki</a>
</td></tr>
<tr>
<td>BIBD</td>
<td>BIU</td>
<td><a href="/wiki/B%C3%ADldudalur_Airport" title="Bíldudalur Airport">Bíldudalur Airport</a></td>
<td><a href="/wiki/B%C3%ADldudalur" title="Bíldudalur">Bíldudalur</a>
</td></tr>
<tr>
<td>BIBK</td>
<td>BJD</td>
<td><a href="/w/index.php?title=Bakkafjordur_Airport&amp;action=edit&amp;redlink=1" class="new" title="Bakkafjordur Airport (page does not exist)">Bakkafjordur Airport</a></td>
<td><a href="/wiki/Bakkafj%C3%B6r%C3%B0ur" title="Bakkafjörður">Bakkafjörður</a>
</td></tr>
<tr>
<td>BIBL</td>
<td>BLO</td>
<td><a href="/wiki/Bl%C3%B6ndu%C3%B3s_Airport" title="Blönduós Airport">Blönduós Airport</a></td>
<td><a href="/wiki/Bl%C3%B6ndu%C3%B3s" title="Blönduós">Blönduós</a>
</td></tr>
<tr>
<td>BIBR</td>
<td></td>
<td><a href="/w/index.php?title=B%C3%BA%C3%B0ardalur_Airport&amp;action=edit&amp;redlink=1" class="new" title="Búðardalur Airport (page does not exist)">Búðardalur Airport</a></td>
<td><a href="/wiki/B%C3%BA%C3%B0ardalur" title="Búðardalur">Búðardalur</a>
</td></tr>
<tr>
<td>BIDV</td>
<td>DJU</td>
<td><a href="/wiki/Djupivogur_Airport" class="mw-redirect" title="Djupivogur Airport">Djupivogur Airport</a></td>
<td><a href="/wiki/Djupivogur" class="mw-redirect" title="Djupivogur">Djupivogur</a>
</td></tr>
<tr>
<td>BIEG</td>
<td>EGS</td>
<td><a href="/wiki/Egilssta%C3%B0ir_Airport" title="Egilsstaðir Airport">Egilsstaðir Airport</a></td>
<td><a href="/wiki/Egilssta%C3%B0ir" title="Egilsstaðir">Egilsstaðir</a>
</td></tr>
<tr>
<td>BIGJ</td>
<td>GJR</td>
<td><a href="/wiki/Gj%C3%B6gur_Airport" title="Gjögur Airport">Gjögur Airport</a></td>
<td><a href="/w/index.php?title=Gj%C3%B6gur&amp;action=edit&amp;redlink=1" class="new" title="Gjögur (page does not exist)">Gjögur</a>
</td></tr>
<tr>
<td>BIGR</td>
<td>GRY</td>
<td><a href="/wiki/Gr%C3%ADmsey_Airport" title="Grímsey Airport">Grímsey Airport</a></td>
<td><a href="/wiki/Gr%C3%ADmsey" title="Grímsey">Grímsey</a>
</td></tr>
<tr>
<td>BIHN</td>
<td>HFN</td>
<td><a href="/wiki/Hornafj%C3%B6r%C3%B0ur_Airport" title="Hornafjörður Airport">Hornafjörður Airport</a></td>
<td><a href="/wiki/H%C3%B6fn" title="Höfn">Höfn</a>
</td></tr>
<tr>
<td>BIHU</td>
<td>HZK</td>
<td><a href="/wiki/H%C3%BAsav%C3%ADk_Airport" title="Húsavík Airport">Húsavík Airport</a></td>
<td><a href="/wiki/H%C3%BAsav%C3%ADk" title="Húsavík">Húsavík</a>
</td></tr>
<tr>
<td>BIIS</td>
<td>IFJ</td>
<td><a href="/wiki/%C3%8Dsafj%C3%B6r%C3%B0ur_Airport" title="Ísafjörður Airport">Ísafjörður Airport</a></td>
<td><a href="/wiki/%C3%8Dsafj%C3%B6r%C3%B0ur" title="Ísafjörður">Ísafjörður</a>
</td></tr>
<tr>
<td>BIKF</td>
<td>KEF</td>
<td><a href="/wiki/Keflav%C3%ADk_International_Airport" title="Keflavík International Airport">Keflavík International Airport</a> (Flugstöð Leifs Eiríkssonar)</td>
<td><a href="/wiki/Keflav%C3%ADk" title="Keflavík">Keflavík</a>
</td></tr>
<tr>
<td>BIKP</td>
<td>OPA</td>
<td><a href="/wiki/Kopasker_Airport" class="mw-redirect" title="Kopasker Airport">Kopasker Airport</a></td>
<td><a href="/wiki/K%C3%B3pasker" title="Kópasker">Kópasker</a>
</td></tr>
<tr>
<td>BIKR</td>
<td>SAK</td>
<td><a href="/wiki/Sau%C3%B0%C3%A1rkr%C3%B3kur_Airport" title="Sauðárkrókur Airport">Sauðárkrókur Airport</a></td>
<td><a href="/wiki/Sau%C3%B0%C3%A1rkr%C3%B3kur" title="Sauðárkrókur">Sauðárkrókur</a>
</td></tr>
<tr>
<td>BINF</td>
<td>NOR</td>
<td><a href="/wiki/Nordfjordur_Airport" class="mw-redirect" title="Nordfjordur Airport">Nordfjordur Airport</a></td>
<td><a href="/wiki/Neskaupsta%C3%B0ur" title="Neskaupstaður">Nordfjordur</a>
</td></tr>
<tr>
<td>BIPA</td>
<td>PFJ</td>
<td><a href="/wiki/Patreksfj%C3%B6r%C3%B0ur_Airport" title="Patreksfjörður Airport">Patreksfjörður Airport</a></td>
<td><a href="/wiki/Patreksfj%C3%B6r%C3%B0ur" title="Patreksfjörður">Patreksfjörður</a>
</td></tr>
<tr>
<td>BIRF</td>
<td>OLI</td>
<td><a href="/wiki/Rif_Airport" title="Rif Airport">Rif Airport</a></td>
<td><a href="/wiki/%C3%93lafsv%C3%ADk" title="Ólafsvík">Ólafsvík</a>
</td></tr>
<tr>
<td>BIRG</td>
<td>RFN</td>
<td><a href="/wiki/Raufarh%C3%B6fn_Airport" title="Raufarhöfn Airport">Raufarhöfn Airport</a></td>
<td><a href="/wiki/Raufarh%C3%B6fn" title="Raufarhöfn">Raufarhöfn</a>
</td></tr>
<tr>
<td>BIRK</td>
<td>RKV</td>
<td><a href="/wiki/Reykjav%C3%ADk_Airport" title="Reykjavík Airport">Reykjavík Airport</a></td>
<td><a href="/wiki/Reykjav%C3%ADk" title="Reykjavík">Reykjavík</a>
</td></tr>
<tr>
<td>BISF</td>
<td></td>
<td><a href="/wiki/Selfoss_Airport" title="Selfoss Airport">Selfoss Airport</a></td>
<td><a href="/wiki/Selfoss_(town)" title="Selfoss (town)">Selfoss</a>
</td></tr>
<tr>
<td>BISI</td>
<td>SIJ</td>
<td><a href="/wiki/Siglufj%C3%B6r%C3%B0ur_Airport" title="Siglufjörður Airport">Siglufjörður Airport</a></td>
<td><a href="/wiki/Siglufj%C3%B6r%C3%B0ur" title="Siglufjörður">Siglufjörður</a>
</td></tr>
<tr>
<td>BIST</td>
<td>SYK</td>
<td><a href="/wiki/Stykkish%C3%B3lmur_Airport" title="Stykkishólmur Airport">Stykkishólmur Airport</a></td>
<td><a href="/wiki/Stykkish%C3%B3lmur" title="Stykkishólmur">Stykkishólmur</a>
</td></tr>
<tr>
<td>BITE</td>
<td>TEY</td>
<td><a href="/wiki/Thingeyri_Airport" class="mw-redirect" title="Thingeyri Airport">Thingeyri Airport</a></td>
<td><a href="/wiki/%C3%9Eingeyri" class="mw-redirect" title="Þingeyri">Þingeyri</a>
</td></tr>
<tr>
<td>BITN</td>
<td>THO</td>
<td><a href="/wiki/Thorshofn_Airport" class="mw-redirect" title="Thorshofn Airport">Thorshofn Airport</a></td>
<td><a href="/wiki/%C3%9E%C3%B3rsh%C3%B6fn" title="Þórshöfn">Þórshöfn</a>
</td></tr>
<tr>
<td>BIVM</td>
<td>VEY</td>
<td><a href="/wiki/Vestmannaeyjar_Airport" title="Vestmannaeyjar Airport">Vestmannaeyjar Airport</a></td>
<td><a href="/wiki/Vestmannaeyjar" title="Vestmannaeyjar">Vestmannaeyjar</a>
</td></tr>
<tr>
<td>BIVO</td>
<td>VPN</td>
<td><a href="/wiki/Vopnafj%C3%B6r%C3%B0ur_Airport" title="Vopnafjörður Airport">Vopnafjörður Airport</a></td>
<td><a href="/wiki/Vopnafj%C3%B6r%C3%B0ur" title="Vopnafjörður">Vopnafjörður</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open('BI - Iceland.csv', mode='w', newline='', encoding='utf-8') as csv_file:
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