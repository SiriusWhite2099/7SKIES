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
<td>EFAH</td>
<td></td>
<td><a href="/wiki/Ahmosuo_Airport" class="mw-redirect" title="Ahmosuo Airport">Ahmosuo Airport</a></td>
<td><a href="/wiki/Oulu" title="Oulu">Oulu</a>
</td></tr>
<tr>
<td>EFAL</td>
<td></td>
<td><a href="/wiki/Alavus_Airport" class="mw-redirect" title="Alavus Airport">Alavus Airport</a></td>
<td><a href="/wiki/Alavus" title="Alavus">Alavus</a>
</td></tr>
<tr>
<td>EFET</td>
<td>ENF</td>
<td><a href="/wiki/Enonteki%C3%B6_Airport" title="Enontekiö Airport">Enontekiö Airport</a></td>
<td><a href="/wiki/Enonteki%C3%B6" title="Enontekiö">Enontekiö</a>
</td></tr>
<tr>
<td>EFEU</td>
<td></td>
<td><a href="/wiki/Eura_Airport" class="mw-redirect" title="Eura Airport">Eura Airport</a></td>
<td><a href="/wiki/Eura" title="Eura">Eura</a>
</td></tr>
<tr>
<td>EFFO</td>
<td></td>
<td><a href="/wiki/Forssa_Airport" class="mw-redirect" title="Forssa Airport">Forssa Airport</a></td>
<td><a href="/wiki/Forssa" title="Forssa">Forssa</a>
</td></tr>
<tr>
<td>EFHA</td>
<td>KEV</td>
<td><a href="/wiki/Halli_Airport" title="Halli Airport">Halli Airport</a></td>
<td><a href="/wiki/Kuorevesi" title="Kuorevesi">Kuorevesi</a>
</td></tr>
<tr>
<td>EFHE</td>
<td></td>
<td><a href="/wiki/Hernesaari_Heliport" title="Hernesaari Heliport">Hernesaari Heliport</a></td>
<td><a href="/wiki/Helsinki" title="Helsinki">Helsinki</a>
</td></tr>
<tr>
<td>EFHF</td>
<td>HEM</td>
<td><a href="/wiki/Helsinki-Malmi_Airport" title="Helsinki-Malmi Airport">Helsinki-Malmi Airport</a></td>
<td><a href="/wiki/Helsinki" title="Helsinki">Helsinki</a>
</td></tr>
<tr>
<td>EFHK</td>
<td>HEL</td>
<td><a href="/wiki/Helsinki-Vantaa_Airport" class="mw-redirect" title="Helsinki-Vantaa Airport">Helsinki-Vantaa Airport</a></td>
<td><a href="/wiki/Vantaa" title="Vantaa">Vantaa</a>
</td></tr>
<tr>
<td>EFHM</td>
<td></td>
<td><a href="/wiki/H%C3%A4meenkyr%C3%B6_Airport" class="mw-redirect" title="Hämeenkyrö Airport">Hämeenkyrö Airport</a></td>
<td><a href="/wiki/H%C3%A4meenkyr%C3%B6" title="Hämeenkyrö">Hämeenkyrö</a>
</td></tr>
<tr>
<td>EFHN</td>
<td></td>
<td><a href="/wiki/Hanko_Airport" class="mw-redirect" title="Hanko Airport">Hanko Airport</a> (<a href="/wiki/Hang%C3%B6_Airport" class="mw-redirect" title="Hangö Airport">Hangö Airport</a>)</td>
<td><a href="/wiki/Hanko,_Finland" title="Hanko, Finland">Hanko</a> (<a href="/wiki/Hang%C3%B6" class="mw-redirect" title="Hangö">Hangö</a>)
</td></tr>
<tr>
<td>EFHV</td>
<td>HYV</td>
<td><a href="/wiki/Hyvink%C3%A4%C3%A4_Airport" class="mw-redirect" title="Hyvinkää Airport">Hyvinkää Airport</a></td>
<td><a href="/wiki/Hyvink%C3%A4%C3%A4" title="Hyvinkää">Hyvinkää</a>
</td></tr>
<tr>
<td>EFIK</td>
<td></td>
<td><a href="/w/index.php?title=Kiikala_Airport&amp;action=edit&amp;redlink=1" class="new" title="Kiikala Airport (page does not exist)">Kiikala Airport</a></td>
<td><a href="/wiki/Kiikala" title="Kiikala">Kiikala</a>
</td></tr>
<tr>
<td>EFIM</td>
<td></td>
<td><a href="/wiki/Immola_Airport" class="mw-redirect" title="Immola Airport">Immola Airport</a></td>
<td><a href="/wiki/Imatra" title="Imatra">Imatra</a>
</td></tr>
<tr>
<td>EFIT</td>
<td>KTQ</td>
<td><a href="/wiki/Kitee_Airport" class="mw-redirect" title="Kitee Airport">Kitee Airport</a></td>
<td><a href="/wiki/Kitee" title="Kitee">Kitee</a>
</td></tr>
<tr>
<td>EFIV</td>
<td>IVL</td>
<td><a href="/wiki/Ivalo_Airport" title="Ivalo Airport">Ivalo Airport</a></td>
<td><a href="/wiki/Ivalo" title="Ivalo">Ivalo</a> / <a href="/wiki/Inari,_Finland" title="Inari, Finland">Inari</a>
</td></tr>
<tr>
<td>EFJM</td>
<td></td>
<td><a href="/wiki/J%C3%A4mij%C3%A4rvi_Airport" class="mw-redirect" title="Jämijärvi Airport">Jämijärvi Airport</a></td>
<td><a href="/wiki/J%C3%A4mij%C3%A4rvi" title="Jämijärvi">Jämijärvi</a>
</td></tr>
<tr>
<td>EFJO</td>
<td>JOE</td>
<td><a href="/wiki/Joensuu_Airport" title="Joensuu Airport">Joensuu Airport</a></td>
<td><a href="/wiki/Joensuu" title="Joensuu">Joensuu</a> / <a href="/wiki/Liperi" title="Liperi">Liperi</a>
</td></tr>
<tr>
<td>EFJY</td>
<td>JYV</td>
<td><a href="/wiki/Jyv%C3%A4skyl%C3%A4_Airport" title="Jyväskylä Airport">Jyväskylä Airport</a></td>
<td><a href="/wiki/Jyv%C3%A4skyl%C3%A4n_maalaiskunta" title="Jyväskylän maalaiskunta">Jyväskylän maalaiskunta</a>
</td></tr>
<tr>
<td>EFKA</td>
<td>KAU</td>
<td><a href="/wiki/Kauhava_Airport" class="mw-redirect" title="Kauhava Airport">Kauhava Airport</a></td>
<td><a href="/wiki/Kauhava" title="Kauhava">Kauhava</a>
</td></tr>
<tr>
<td>EFKE</td>
<td>KEM</td>
<td><a href="/wiki/Kemi-Tornio_Airport" title="Kemi-Tornio Airport">Kemi-Tornio Airport</a></td>
<td><a href="/wiki/Kemi" title="Kemi">Kemi</a> / <a href="/wiki/Tornio" title="Tornio">Tornio</a>
</td></tr>
<tr>
<td>EFKH</td>
<td></td>
<td><a href="/wiki/Kuhmo_Airfield" title="Kuhmo Airfield">Kuhmo Airfield</a></td>
<td><a href="/wiki/Kuhmo" title="Kuhmo">Kuhmo</a>
</td></tr>
<tr>
<td>EFKI</td>
<td>KAJ</td>
<td><a href="/wiki/Kajaani_Airport" title="Kajaani Airport">Kajaani Airport</a></td>
<td><a href="/wiki/Kajaani" title="Kajaani">Kajaani</a>
</td></tr>
<tr>
<td>EFKJ</td>
<td>KHJ</td>
<td><a href="/wiki/Kauhajoki_Airport" class="mw-redirect" title="Kauhajoki Airport">Kauhajoki Airport</a></td>
<td><a href="/wiki/Kauhajoki" title="Kauhajoki">Kauhajoki</a>
</td></tr>
<tr>
<td>EFKK</td>
<td>KOK</td>
<td><a href="/wiki/Kokkola-Pietarsaari_Airport" title="Kokkola-Pietarsaari Airport">Kokkola-Pietarsaari Airport</a></td>
<td><a href="/wiki/Kronoby" title="Kronoby">Kronoby</a>
</td></tr>
<tr>
<td>EFKM</td>
<td></td>
<td><a href="/wiki/Kemij%C3%A4rvi_Airport" class="mw-redirect" title="Kemijärvi Airport">Kemijärvi Airport</a></td>
<td><a href="/wiki/Kemij%C3%A4rvi" title="Kemijärvi">Kemijärvi</a>
</td></tr>
<tr>
<td>EFKO</td>
<td></td>
<td><a href="/wiki/Kalajoki_Airport" class="mw-redirect" title="Kalajoki Airport">Kalajoki Airport</a></td>
<td><a href="/wiki/Kalajoki" title="Kalajoki">Kalajoki</a>
</td></tr>
<tr>
<td>EFKS</td>
<td>KAO</td>
<td><a href="/wiki/Kuusamo_Airport" title="Kuusamo Airport">Kuusamo Airport</a></td>
<td><a href="/wiki/Kuusamo" title="Kuusamo">Kuusamo</a>
</td></tr>
<tr>
<td>EFKT</td>
<td>KTT</td>
<td><a href="/wiki/Kittil%C3%A4_Airport" title="Kittilä Airport">Kittilä Airport</a></td>
<td><a href="/wiki/Kittil%C3%A4" title="Kittilä">Kittilä</a>
</td></tr>
<tr>
<td>EFKU</td>
<td>KUO</td>
<td><a href="/wiki/Kuopio_Airport" title="Kuopio Airport">Kuopio Airport</a></td>
<td><a href="/wiki/Kuopio" title="Kuopio">Kuopio</a> / <a href="/wiki/Siilinj%C3%A4rvi" title="Siilinjärvi">Siilinjärvi</a>
</td></tr>
<tr>
<td>EFKV</td>
<td></td>
<td><a href="/wiki/Kivij%C3%A4rvi_Airport" class="mw-redirect" title="Kivijärvi Airport">Kivijärvi Airport</a></td>
<td><a href="/wiki/Kivij%C3%A4rvi" title="Kivijärvi">Kivijärvi</a>
</td></tr>
<tr>
<td>EFKY</td>
<td></td>
<td><a href="/wiki/Kymi_Airport" class="mw-redirect" title="Kymi Airport">Kymi Airport</a></td>
<td><a href="/wiki/Kymi,_Finland" title="Kymi, Finland">Kymi</a>
</td></tr>
<tr>
<td>EFLA</td>
<td></td>
<td><a href="/w/index.php?title=Vesivehmaa_Airport&amp;action=edit&amp;redlink=1" class="new" title="Vesivehmaa Airport (page does not exist)">Vesivehmaa Airport</a></td>
<td><a href="/wiki/Lahti" title="Lahti">Lahti</a>
</td></tr>
<tr>
<td>EFLP</td>
<td>LPP</td>
<td><a href="/wiki/Lappeenranta_Airport" title="Lappeenranta Airport">Lappeenranta Airport</a></td>
<td><a href="/wiki/Lappeenranta" title="Lappeenranta">Lappeenranta</a>
</td></tr>
<tr>
<td>EFMA</td>
<td>MHQ</td>
<td><a href="/wiki/Mariehamn_Airport" title="Mariehamn Airport">Mariehamn Airport</a></td>
<td><a href="/wiki/Mariehamn" title="Mariehamn">Mariehamn</a>
</td></tr>
<tr>
<td>EFME</td>
<td></td>
<td><a href="/w/index.php?title=Menkij%C3%A4rvi_Airport&amp;action=edit&amp;redlink=1" class="new" title="Menkijärvi Airport (page does not exist)">Menkijärvi Airport</a></td>
<td><a href="/wiki/Alaj%C3%A4rvi" title="Alajärvi">Alajärvi</a>
</td></tr>
<tr>
<td>EFMI</td>
<td>MIK</td>
<td><a href="/wiki/Mikkeli_Airport" title="Mikkeli Airport">Mikkeli Airport</a></td>
<td><a href="/wiki/Mikkeli" title="Mikkeli">Mikkeli</a>
</td></tr>
<tr>
<td>EFNU</td>
<td></td>
<td><a href="/w/index.php?title=Nummela_Airport&amp;action=edit&amp;redlink=1" class="new" title="Nummela Airport (page does not exist)">Nummela Airport</a></td>
<td><a href="/wiki/Nummela_(Vihti)" title="Nummela (Vihti)">Nummela</a>
</td></tr>
<tr>
<td>EFOU</td>
<td>OUL</td>
<td><a href="/wiki/Oulu_Airport" title="Oulu Airport">Oulu Airport</a></td>
<td><a href="/wiki/Oulunsalo" title="Oulunsalo">Oulunsalo</a>
</td></tr>
<tr>
<td>EFPI</td>
<td></td>
<td><a href="/w/index.php?title=Piikaj%C3%A4rvi_Airport&amp;action=edit&amp;redlink=1" class="new" title="Piikajärvi Airport (page does not exist)">Piikajärvi Airport</a></td>
<td><a href="/wiki/Kokem%C3%A4ki" title="Kokemäki">Kokemäki</a>
</td></tr>
<tr>
<td>EFPK</td>
<td></td>
<td><a href="/wiki/Pieks%C3%A4m%C3%A4ki_Airport" class="mw-redirect" title="Pieksämäki Airport">Pieksämäki Airport</a></td>
<td><a href="/wiki/Pieks%C3%A4m%C3%A4ki" title="Pieksämäki">Pieksämäki</a>
</td></tr>
<tr>
<td>EFPO</td>
<td>POR</td>
<td><a href="/wiki/Pori_Airport" title="Pori Airport">Pori Airport</a></td>
<td><a href="/wiki/Pori" title="Pori">Pori</a>
</td></tr>
<tr>
<td>EFPR</td>
<td></td>
<td><a href="/w/index.php?title=Pyht%C3%A4%C3%A4_Redstone&amp;action=edit&amp;redlink=1" class="new" title="Pyhtää Redstone (page does not exist)">Pyhtää Redstone</a></td>
<td><a href="/wiki/Pyht%C3%A4%C3%A4" title="Pyhtää">Pyhtää</a>
</td></tr>
<tr>
<td>EFPU</td>
<td></td>
<td><a href="/wiki/Pudasj%C3%A4rvi_Airport" class="mw-redirect" title="Pudasjärvi Airport">Pudasjärvi Airport</a></td>
<td><a href="/wiki/Pudasj%C3%A4rvi" title="Pudasjärvi">Pudasjärvi</a>
</td></tr>
<tr>
<td>EFPY</td>
<td></td>
<td><a href="/wiki/Pyh%C3%A4salmi_Airport" class="mw-redirect" title="Pyhäsalmi Airport">Pyhäsalmi Airport</a></td>
<td><a href="/wiki/Pyh%C3%A4salmi" class="mw-redirect" title="Pyhäsalmi">Pyhäsalmi</a>
</td></tr>
<tr>
<td>EFRH</td>
<td></td>
<td><a href="/wiki/Pattijoki_Airport" class="mw-redirect" title="Pattijoki Airport">Pattijoki Airport</a></td>
<td><a href="/wiki/Raahe" title="Raahe">Raahe</a>
</td></tr>
<tr>
<td>EFRN</td>
<td></td>
<td><a href="/wiki/Rantasalmi_Airport" class="mw-redirect" title="Rantasalmi Airport">Rantasalmi Airport</a></td>
<td><a href="/wiki/Rantasalmi" title="Rantasalmi">Rantasalmi</a>
</td></tr>
<tr>
<td>EFRO</td>
<td>RVN</td>
<td><a href="/wiki/Rovaniemi_Airport" title="Rovaniemi Airport">Rovaniemi Airport</a></td>
<td><a href="/wiki/Rovaniemi" title="Rovaniemi">Rovaniemi</a>
</td></tr>
<tr>
<td>EFRU</td>
<td></td>
<td><a href="/wiki/Ranua_Airport" class="mw-redirect" title="Ranua Airport">Ranua Airport</a></td>
<td><a href="/wiki/Ranua" title="Ranua">Ranua</a>
</td></tr>
<tr>
<td>EFRV</td>
<td></td>
<td><a href="/wiki/Kiuruvesi_Airport" class="mw-redirect" title="Kiuruvesi Airport">Kiuruvesi Airport</a></td>
<td><a href="/wiki/Kiuruvesi" title="Kiuruvesi">Kiuruvesi</a>
</td></tr>
<tr>
<td>EFRY</td>
<td></td>
<td><a href="/wiki/R%C3%A4ysk%C3%A4l%C3%A4_Airport" class="mw-redirect" title="Räyskälä Airport">Räyskälä Airport</a></td>
<td><a href="/wiki/Loppi" title="Loppi">Loppi</a>
</td></tr>
<tr>
<td>EFSA</td>
<td>SVL</td>
<td><a href="/wiki/Savonlinna_Airport" title="Savonlinna Airport">Savonlinna Airport</a></td>
<td><a href="/wiki/Savonlinna" title="Savonlinna">Savonlinna</a>
</td></tr>
<tr>
<td>EFSE</td>
<td></td>
<td><a href="/w/index.php?title=Sel%C3%A4np%C3%A4%C3%A4_Airport&amp;action=edit&amp;redlink=1" class="new" title="Selänpää Airport (page does not exist)">Selänpää Airport</a></td>
<td><a href="/wiki/Kouvola" title="Kouvola">Kouvola</a>
</td></tr>
<tr>
<td>EFSI</td>
<td>SJY</td>
<td><a href="/wiki/Sein%C3%A4joki_Airport" title="Seinäjoki Airport">Seinäjoki Airport</a></td>
<td><a href="/wiki/Sein%C3%A4joki" title="Seinäjoki">Seinäjoki</a> / <a href="/wiki/Ilmajoki" title="Ilmajoki">Ilmajoki</a>
</td></tr>
<tr>
<td>EFSO</td>
<td>SOT</td>
<td><a href="/wiki/Sodankyl%C3%A4_Airport" class="mw-redirect" title="Sodankylä Airport">Sodankylä Airport</a></td>
<td><a href="/wiki/Sodankyl%C3%A4" title="Sodankylä">Sodankylä</a>
</td></tr>
<tr>
<td>EFTP</td>
<td>TMP</td>
<td><a href="/wiki/Tampere-Pirkkala_Airport" class="mw-redirect" title="Tampere-Pirkkala Airport">Tampere-Pirkkala Airport</a></td>
<td><a href="/wiki/Tampere" title="Tampere">Tampere</a> / <a href="/wiki/Pirkkala" title="Pirkkala">Pirkkala</a>
</td></tr>
<tr>
<td>EFTS</td>
<td></td>
<td><a href="https://fi.wikipedia.org/wiki/Teiskon_lentokentt%C3%A4" class="extiw" title="fi:Teiskon lentokenttä">Teisko Airport</a></td>
<td><a href="/wiki/Tampere" title="Tampere">Tampere</a>
</td></tr>
<tr>
<td>EFTU</td>
<td>TKU</td>
<td><a href="/wiki/Turku_Airport" title="Turku Airport">Turku Airport</a></td>
<td><a href="/wiki/Turku" title="Turku">Turku</a>
</td></tr>
<tr>
<td>EFUT</td>
<td>UTI</td>
<td><a href="/wiki/Utti_Airport" class="mw-redirect" title="Utti Airport">Utti Airport</a></td>
<td><a href="/wiki/Utti" title="Utti">Utti</a> / <a href="/wiki/Valkeala" title="Valkeala">Valkeala</a>
</td></tr>
<tr>
<td>EFVA</td>
<td>VAA</td>
<td><a href="/wiki/Vaasa_Airport" title="Vaasa Airport">Vaasa Airport</a></td>
<td><a href="/wiki/Vaasa" title="Vaasa">Vaasa</a>
</td></tr>
<tr>
<td>EFVR</td>
<td>VRK</td>
<td><a href="/wiki/Varkaus_Airport" title="Varkaus Airport">Varkaus Airport</a></td>
<td><a href="/wiki/Varkaus" title="Varkaus">Varkaus</a> / <a href="/wiki/Joroinen" title="Joroinen">Joroinen</a>
</td></tr>
<tr>
<td>EFYL</td>
<td>YLI</td>
<td><a href="/wiki/Ylivieska_Airport" class="mw-redirect" title="Ylivieska Airport">Ylivieska Airport</a></td>
<td><a href="/wiki/Ylivieska" title="Ylivieska">Ylivieska</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EF – Finland.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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