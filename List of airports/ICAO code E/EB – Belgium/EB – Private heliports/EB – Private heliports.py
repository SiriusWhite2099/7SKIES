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
<td>EBAK</td>
<td></td>
<td><a href="/w/index.php?title=Antwerp/Kiel_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Antwerp/Kiel Heliport (page does not exist)">Antwerp/Kiel Heliport</a></td>
<td><a href="/wiki/Antwerp" title="Antwerp">Antwerp</a>
</td></tr>
<tr>
<td>EBAS</td>
<td></td>
<td><a href="/w/index.php?title=Schilde/%27s-Gravenwezel_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Schilde/'s-Gravenwezel Heliport (page does not exist)">Schilde/'s-Gravenwezel Heliport</a></td>
<td><a href="/wiki/Schilde" title="Schilde">Schilde</a>
</td></tr>
<tr>
<td>EBBC</td>
<td></td>
<td><a href="/w/index.php?title=Brecht/Luyckx_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Brecht/Luyckx Heliport (page does not exist)">Brecht/Luyckx Heliport</a></td>
<td><a href="/wiki/Brecht,_Belgium" title="Brecht, Belgium">Brecht</a>
</td></tr>
<tr>
<td>EBBH</td>
<td></td>
<td><a href="/w/index.php?title=Brecht/Keysers_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Brecht/Keysers Heliport (page does not exist)">Brecht/Keysers Heliport</a></td>
<td><a href="/wiki/Brecht,_Belgium" title="Brecht, Belgium">Brecht</a>
</td></tr>
<tr>
<td>EBBM</td>
<td></td>
<td><a href="/w/index.php?title=Brakel/Michelbeke_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Brakel/Michelbeke Heliport (page does not exist)">Brakel/Michelbeke Heliport</a></td>
<td><a href="/wiki/Michelbeke" title="Michelbeke">Michelbeke</a>
</td></tr>
<tr>
<td>EBBV</td>
<td></td>
<td><a href="/w/index.php?title=Brecht/Vochten_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Brecht/Vochten Heliport (page does not exist)">Brecht/Vochten Heliport</a></td>
<td><a href="/wiki/Brecht,_Belgium" title="Brecht, Belgium">Brecht</a>
</td></tr>
<tr>
<td>EBCH</td>
<td></td>
<td><a href="/wiki/Shape_Pad_Heliport" class="mw-redirect" title="Shape Pad Heliport">Shape Pad Heliport</a></td>
<td><a href="/w/index.php?title=Les_Bruy%C3%A8res&amp;action=edit&amp;redlink=1" class="new" title="Les Bruyères (page does not exist)">Les Bruyères</a><sup id="cite_ref-3" class="reference"><a href="#cite_note-3">[3]</a></sup>
</td></tr>
<tr>
<td>EBDI</td>
<td></td>
<td><a href="/wiki/Diksmuide_Heliport" title="Diksmuide Heliport">Diksmuide Heliport</a></td>
<td><a href="/wiki/Diksmuide" title="Diksmuide">Diksmuide</a>
</td></tr>
<tr>
<td>EBDL</td>
<td></td>
<td><a href="/w/index.php?title=Dilsen-Stokkem/Lanklaar_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Dilsen-Stokkem/Lanklaar Heliport (page does not exist)">Dilsen-Stokkem/Lanklaar Heliport</a></td>
<td><a href="/wiki/Dilsen-Stokkem" title="Dilsen-Stokkem">Dilsen-Stokkem</a>
</td></tr>
<tr>
<td>EBDR</td>
<td></td>
<td><a href="/w/index.php?title=Antwerp/Commandant_Fourcault_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Antwerp/Commandant Fourcault Heliport (page does not exist)">Antwerp/Commandant Fourcault Heliport</a></td>
<td><a href="/wiki/Antwerp" title="Antwerp">Antwerp</a>
</td></tr>
<tr>
<td>EBDW</td>
<td></td>
<td><a href="/w/index.php?title=Diest/Webbekom_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Diest/Webbekom Heliport (page does not exist)">Diest/Webbekom Heliport</a></td>
<td><a href="/wiki/Diest" title="Diest">Diest</a>
</td></tr>
<tr>
<td>EBEB</td>
<td></td>
<td><a href="/w/index.php?title=Evergem/Belzele_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Evergem/Belzele Heliport (page does not exist)">Evergem/Belzele Heliport</a></td>
<td><a href="/wiki/Evergem" title="Evergem">Evergem</a>
</td></tr>
<tr>
<td>EBEN</td>
<td></td>
<td><a href="/w/index.php?title=Ranst/Engles_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Ranst/Engles Heliport (page does not exist)">Ranst/Engles Heliport</a></td>
<td><a href="/wiki/Ranst" title="Ranst">Ranst</a>
</td></tr>
<tr>
<td>EBFR</td>
<td></td>
<td><a href="/w/index.php?title=Francorchamps_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Francorchamps Heliport (page does not exist)">Francorchamps Heliport</a></td>
<td><a href="/wiki/Francorchamps" title="Francorchamps">Francorchamps</a>
</td></tr>
<tr>
<td>EBHA</td>
<td></td>
<td><a href="/w/index.php?title=Ham_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Ham Heliport (page does not exist)">Ham Heliport</a></td>
<td><a href="/wiki/Ham,_Belgium" title="Ham, Belgium">Ham</a>
</td></tr>
<tr>
<td>EBHL</td>
<td></td>
<td><a href="/w/index.php?title=Halen_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Halen Heliport (page does not exist)">Halen Heliport</a></td>
<td><a href="/wiki/Halen" title="Halen">Halen</a>
</td></tr>
<tr>
<td>EBHM</td>
<td></td>
<td><a href="/w/index.php?title=Hasselt/Maasland_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Hasselt/Maasland Heliport (page does not exist)">Hasselt/Maasland Heliport</a></td>
<td><a href="/wiki/Hasselt" title="Hasselt">Hasselt</a>
</td></tr>
<tr>
<td>EBHO</td>
<td></td>
<td><a href="/w/index.php?title=Holsbeek_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Holsbeek Heliport (page does not exist)">Holsbeek Heliport</a></td>
<td><a href="/wiki/Holsbeek" title="Holsbeek">Holsbeek</a>
</td></tr>
<tr>
<td>EBHT</td>
<td></td>
<td><a href="/w/index.php?title=Houthalen_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Houthalen Heliport (page does not exist)">Houthalen Heliport</a></td>
<td><a href="/wiki/Houthalen-Helchteren" title="Houthalen-Helchteren">Houthalen-Helchteren</a>
</td></tr>
<tr>
<td>EBKR</td>
<td></td>
<td><a href="/w/index.php?title=Kruishoutem/Sons_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Kruishoutem/Sons Heliport (page does not exist)">Kruishoutem/Sons Heliport</a></td>
<td><a href="/wiki/Kruishoutem" title="Kruishoutem">Kruishoutem</a>
</td></tr>
<tr>
<td>EBKU</td>
<td></td>
<td><a href="/wiki/Kuurne_Heliport" title="Kuurne Heliport">Kuurne Heliport</a></td>
<td><a href="/wiki/Kuurne" title="Kuurne">Kuurne</a><sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[4]</a></sup>
</td></tr>
<tr>
<td>EBKW</td>
<td></td>
<td><a href="/wiki/Knokke-Heist/Westkapelle_Heliport" title="Knokke-Heist/Westkapelle Heliport">Knokke-Heist/Westkapelle Heliport</a></td>
<td><a href="/wiki/Knokke-Heist" title="Knokke-Heist">Knokke-Heist</a>
</td></tr>
<tr>
<td>EBLM</td>
<td></td>
<td><a href="/w/index.php?title=Meulebeke_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Meulebeke Heliport (page does not exist)">Meulebeke Heliport</a></td>
<td><a href="/wiki/Meulebeke" title="Meulebeke">Meulebeke</a>
</td></tr>
<tr>
<td>EBLR</td>
<td></td>
<td><a href="/wiki/Reninge_Heliport" title="Reninge Heliport">Reninge Heliport</a></td>
<td><a href="/wiki/Reninge" title="Reninge">Reninge</a>
</td></tr>
<tr>
<td>EBLT</td>
<td></td>
<td><a href="/w/index.php?title=Lint_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Lint Heliport (page does not exist)">Lint Heliport</a></td>
<td><a href="/wiki/Lint,_Belgium" title="Lint, Belgium">Lint</a>
</td></tr>
<tr>
<td>EBLU</td>
<td></td>
<td><a href="/w/index.php?title=Lummen_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Lummen Heliport (page does not exist)">Lummen Heliport</a></td>
<td><a href="/wiki/Lummen" title="Lummen">Lummen</a>
</td></tr>
<tr>
<td>EBLY</td>
<td></td>
<td><a href="/w/index.php?title=Ranst/Lymar_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Ranst/Lymar Heliport (page does not exist)">Ranst/Lymar Heliport</a></td>
<td><a href="/wiki/Ranst" title="Ranst">Ranst</a>
</td></tr>
<tr>
<td>EBLZ</td>
<td></td>
<td><a href="/wiki/Zaffelare_Heliport" title="Zaffelare Heliport">Zaffelare Heliport</a></td>
<td><a href="/wiki/Lochristi" title="Lochristi">Lochristi</a><sup id="cite_ref-5" class="reference"><a href="#cite_note-5">[5]</a></sup>
</td></tr>
<tr>
<td>EBME</td>
<td></td>
<td><a href="/w/index.php?title=Meerbeek_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Meerbeek Heliport (page does not exist)">Meerbeek Heliport</a></td>
<td><a href="/wiki/Meerbeek" title="Meerbeek">Meerbeek</a>
</td></tr>
<tr>
<td>EBMW</td>
<td></td>
<td><a href="/w/index.php?title=Meise/Wolvertem_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Meise/Wolvertem Heliport (page does not exist)">Meise/Wolvertem Heliport</a></td>
<td><a href="/wiki/Meise" title="Meise">Meise</a>
</td></tr>
<tr>
<td>EBNH</td>
<td></td>
<td><a href="/w/index.php?title=Oostende_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Oostende Heliport (page does not exist)">Oostende Heliport</a></td>
<td><a href="/wiki/Ostend" title="Ostend">Ostend</a>
</td></tr>
<tr>
<td>EBNK</td>
<td></td>
<td><a href="/w/index.php?title=Nokere/Suys_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Nokere/Suys Heliport (page does not exist)">Nokere/Suys Heliport</a></td>
<td><a href="/wiki/Kruishoutem" title="Kruishoutem">Nokere</a>
</td></tr>
<tr>
<td>EBNP</td>
<td></td>
<td><a href="/w/index.php?title=Neerpelt/Tilburgs_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Neerpelt/Tilburgs Heliport (page does not exist)">Neerpelt/Tilburgs Heliport</a></td>
<td><a href="/wiki/Neerpelt" title="Neerpelt">Neerpelt</a>
</td></tr>
<tr>
<td>EBOB</td>
<td></td>
<td><a href="/w/index.php?title=Oud-Heverlee/Blanden_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Oud-Heverlee/Blanden Heliport (page does not exist)">Oud-Heverlee/Blanden Heliport</a></td>
<td><a href="/wiki/Oud-Heverlee" title="Oud-Heverlee">Oud-Heverlee</a>
</td></tr>
<tr>
<td>EBOO</td>
<td></td>
<td><a href="/w/index.php?title=Oostdijckbank_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Oostdijckbank Heliport (page does not exist)">Oostdijckbank Heliport</a>
</td></tr>
<tr>
<td>EBPW</td>
<td></td>
<td><a href="/w/index.php?title=Pecq/Warcoing_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Pecq/Warcoing Heliport (page does not exist)">Pecq/Warcoing Heliport</a></td>
<td><a href="/wiki/Pecq" title="Pecq">Pecq</a>
</td></tr>
<tr>
<td>EBRO</td>
<td></td>
<td><a href="/w/index.php?title=Ranst/Van_Den_Bosch_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Ranst/Van Den Bosch Heliport (page does not exist)">Ranst/Van Den Bosch Heliport</a></td>
<td><a href="/wiki/Ranst" title="Ranst">Ranst</a>
</td></tr>
<tr>
<td>EBRR</td>
<td></td>
<td><a href="/w/index.php?title=Roeselare/Rumbeke_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Roeselare/Rumbeke Heliport (page does not exist)">Roeselare/Rumbeke Heliport</a></td>
<td><a href="/wiki/Rumbeke" title="Rumbeke">Rumbeke</a>
</td></tr>
<tr>
<td>EBSW</td>
<td></td>
<td><a href="/w/index.php?title=Sint-Pieters-Leeuw_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Sint-Pieters-Leeuw Heliport (page does not exist)">Sint-Pieters-Leeuw Heliport</a></td>
<td><a href="/wiki/Sint-Pieters-Leeuw" title="Sint-Pieters-Leeuw">Sint-Pieters-Leeuw</a>
</td></tr>
<tr>
<td>EBTK</td>
<td></td>
<td><a href="/w/index.php?title=Tielen/Kasterlee_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Tielen/Kasterlee Heliport (page does not exist)">Tielen/Kasterlee Heliport</a></td>
<td><a href="/wiki/Kasterlee" title="Kasterlee">Kasterlee</a>
</td></tr>
<tr>
<td>EBVE</td>
<td></td>
<td><a href="/wiki/Oeren_Heliport" title="Oeren Heliport">Oeren Heliport</a></td>
<td><a href="/wiki/Veurne" title="Veurne">Veurne</a>
</td></tr>
<tr>
<td>EBVU</td>
<td></td>
<td><a href="/w/index.php?title=Rotselaar_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Rotselaar Heliport (page does not exist)">Rotselaar Heliport</a></td>
<td><a href="/wiki/Rotselaar" title="Rotselaar">Rotselaar</a>
</td></tr>
<tr>
<td>EBWA</td>
<td></td>
<td><a href="/w/index.php?title=Waasmunster_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Waasmunster Heliport (page does not exist)">Waasmunster Heliport</a></td>
<td><a href="/wiki/Waasmunster" title="Waasmunster">Waasmunster</a>
</td></tr>
<tr>
<td>EBWI</td>
<td></td>
<td><a href="/w/index.php?title=Wingene_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Wingene Heliport (page does not exist)">Wingene Heliport</a></td>
<td><a href="/wiki/Wingene" title="Wingene">Wingene</a>
</td></tr>
<tr>
<td>EBWZ</td>
<td></td>
<td><a href="/w/index.php?title=Wingene/Zwevezele_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Wingene/Zwevezele Heliport (page does not exist)">Wingene/Zwevezele Heliport</a></td>
<td><a href="/wiki/Wingene" title="Wingene">Wingene</a>
</td></tr>
<tr>
<td>EBZI</td>
<td></td>
<td><a href="/wiki/Zingem_Heliport" title="Zingem Heliport">Zingem Heliport</a></td>
<td><a href="/wiki/Zingem" title="Zingem">Zingem</a>
</td></tr>
<tr>
<td>EBZM</td>
<td></td>
<td><a href="/w/index.php?title=Zomergem_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Zomergem Heliport (page does not exist)">Zomergem Heliport</a></td>
<td><a href="/wiki/Zomergem" title="Zomergem">Zomergem</a>
</td></tr>
<tr>
<td>EBZO</td>
<td></td>
<td><a href="/w/index.php?title=Zonnebeke/Zandvoorde_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Zonnebeke/Zandvoorde Heliport (page does not exist)">Zonnebeke/Zandvoorde Heliport</a></td>
<td><a href="/wiki/Zandvoorde,_Zonnebeke" title="Zandvoorde, Zonnebeke">Zandvoorde</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EB – Private heliports.csv", mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ICAO', 'IATA', 'Airport Name', 'Community']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in table.find_all('tr')[1:]:
        columns = row.find_all(['td', 'th'])

        # Imprimer le contenu de la ligne
        print([column.text.strip() for column in columns])

        if len(columns) == len(fieldnames):
            icao = columns[0].text.strip()
            iata = columns[1].text.strip()
            airport_name = columns[2].text.strip()
            community = columns[3].text.strip()

            writer.writerow({'ICAO': icao, 'IATA': iata, 'Airport Name': airport_name, 'Community': community})
        else:
            print(f"Ignorer la ligne avec un nombre incorrect de colonnes: {row}")

print("Le fichier CSV a été créé avec succès.")