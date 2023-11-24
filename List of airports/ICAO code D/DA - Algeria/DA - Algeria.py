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
<td>DAAB</td>
<td>QLD</td>
<td><a href="/wiki/Blida_Airport" title="Blida Airport">Blida Airport</a></td>
<td><a href="/wiki/Blida" title="Blida">Blida</a>
</td></tr>
<tr>
<td>DAAD</td>
<td>BUJ</td>
<td><a href="/wiki/Bou_Saada_Airport" title="Bou Saada Airport">Bou Saada Airport</a></td>
<td><a href="/wiki/Bou_Saada" class="mw-redirect" title="Bou Saada">Bou Saada</a>
</td></tr>
<tr>
<td>DAAE</td>
<td>BJA</td>
<td><a href="/wiki/Soummam_Airport" class="mw-redirect" title="Soummam Airport">Soummam Airport</a></td>
<td><a href="/wiki/Bejaia" class="mw-redirect" title="Bejaia">Bejaia</a>
</td></tr>
<tr>
<td>DAAG</td>
<td>ALG</td>
<td><a href="/wiki/Houari_Boumedienne_Airport" class="mw-redirect" title="Houari Boumedienne Airport">Houari Boumedienne Airport</a></td>
<td><a href="/wiki/Algiers" title="Algiers">Algiers</a>
</td></tr>
<tr>
<td>DAAJ</td>
<td>DJG</td>
<td><a href="/wiki/Tiska_Airport" class="mw-redirect" title="Tiska Airport">Tiska Airport</a></td>
<td><a href="/wiki/Djanet" title="Djanet">Djanet</a>
</td></tr>
<tr>
<td>DAAK</td>
<td>QFD</td>
<td><a href="/wiki/Boufarik_Airport" title="Boufarik Airport">Boufarik Airport</a></td>
<td><a href="/wiki/Boufarik" title="Boufarik">Boufarik</a>
</td></tr>
<tr>
<td>DAAP</td>
<td>VVZ</td>
<td><a href="/wiki/Illizi_Airport" class="mw-redirect" title="Illizi Airport">Illizi Airport</a></td>
<td><a href="/wiki/Illizi" title="Illizi">Illizi</a>
</td></tr>
<tr>
<td>DAAS</td>
<td>QSF</td>
<td><a href="/wiki/Ain_Arnat_Airport" title="Ain Arnat Airport">Ain Arnat Airport</a></td>
<td><a href="/wiki/Setif" class="mw-redirect" title="Setif">Setif</a>
</td></tr>
<tr>
<td>DAAT</td>
<td>TMR</td>
<td><a href="/wiki/Tamanrasset_Airport" class="mw-redirect" title="Tamanrasset Airport">Tamanrasset Airport</a></td>
<td><a href="/wiki/Tamanrasset" title="Tamanrasset">Tamanrasset</a>
</td></tr>
<tr>
<td>DAAV</td>
<td>GJL</td>
<td><a href="/wiki/Jijel_Ferhat_Abbas_Airport" title="Jijel Ferhat Abbas Airport">Jijel Ferhat Abbas Airport</a></td>
<td><a href="/wiki/Jijel" title="Jijel">Jijel</a>
</td></tr>
<tr>
<td>DAAY</td>
<td>MZW</td>
<td><a href="/wiki/Mecheria_Airport" class="mw-redirect" title="Mecheria Airport">Mecheria Airport</a></td>
<td><a href="/wiki/Mecheria" class="mw-redirect" title="Mecheria">Mecheria</a>
</td></tr>
<tr>
<td>DAAZ</td>
<td>QZN</td>
<td><a href="/wiki/Relizane_Airport" title="Relizane Airport">Relizane Airport</a></td>
<td><a href="/wiki/Relizane" title="Relizane">Relizane</a>
</td></tr>
<tr>
<td>DABB</td>
<td>AAE</td>
<td><a href="/wiki/Rabah_Bitat_Airport" title="Rabah Bitat Airport">Rabah Bitat Airport</a></td>
<td><a href="/wiki/Annaba" title="Annaba">Annaba</a>
</td></tr>
<tr>
<td>DABC</td>
<td>CZL</td>
<td><a href="/wiki/Mohamed_Boudiaf_International_Airport" title="Mohamed Boudiaf International Airport">Mohamed Boudiaf International Airport</a></td>
<td><a href="/wiki/Constantine,_Algeria" title="Constantine, Algeria">Constantine</a>
</td></tr>
<tr>
<td>DABP</td>
<td>SKI</td>
<td><a href="/wiki/Skikda_Airport" title="Skikda Airport">Skikda Airport</a></td>
<td><a href="/wiki/Skikda" title="Skikda">Skikda</a>
</td></tr>
<tr>
<td>DABS</td>
<td>TEE</td>
<td><a href="/wiki/T%C3%A9bessa_Airport" class="mw-redirect" title="Tébessa Airport">Tébessa Airport</a></td>
<td><a href="/wiki/T%C3%A9bessa" title="Tébessa">Tébessa</a>
</td></tr>
<tr>
<td>DABT</td>
<td>BLJ</td>
<td><a href="/wiki/Batna_Airport" class="mw-redirect" title="Batna Airport">Batna Airport</a></td>
<td><a href="/wiki/Batna_City" class="mw-redirect" title="Batna City">Batna</a>
</td></tr>
<tr>
<td>DAFH</td>
<td>HRM</td>
<td><a href="/wiki/Hassi_R%27Mel_Airport" title="Hassi R'Mel Airport">Hassi R'Mel Airport</a></td>
<td><a href="/wiki/Hassi_R%27Mel" title="Hassi R'Mel">Hassi R'Mel</a>
</td></tr>
<tr>
<td>DAFI</td>
<td>QDJ</td>
<td><a href="/wiki/Tsletsi_Airport" title="Tsletsi Airport">Tsletsi Airport</a></td>
<td><a href="/wiki/Djelfa" title="Djelfa">Djelfa</a>
</td></tr>
<tr>
<td>DAOB</td>
<td>TID</td>
<td><a href="/wiki/Bou_Chekif_Airport" class="mw-redirect" title="Bou Chekif Airport">Bou Chekif Airport</a></td>
<td><a href="/wiki/Tiaret" title="Tiaret">Tiaret</a>
</td></tr>
<tr>
<td>DAOF</td>
<td>TIN</td>
<td><a href="/wiki/Tindouf_Airport" class="mw-redirect" title="Tindouf Airport">Tindouf Airport</a></td>
<td><a href="/wiki/Tindouf" title="Tindouf">Tindouf</a>
</td></tr>
<tr>
<td>DAOI</td>
<td>CFK</td>
<td><a href="/wiki/Chlef_International_Airport" title="Chlef International Airport">Chlef International Airport</a></td>
<td><a href="/wiki/Chlef" title="Chlef">Chlef</a>
</td></tr>
<tr>
<td>DAOL</td>
<td>TAF</td>
<td><a href="/wiki/Oran_Tafaraoui_Airport" class="mw-redirect" title="Oran Tafaraoui Airport">Oran Tafaraoui Airport</a></td>
<td><a href="/wiki/Oran" title="Oran">Oran</a>
</td></tr>
<tr>
<td>DAON</td>
<td>TLM</td>
<td><a href="/wiki/Zenata_Airport" class="mw-redirect" title="Zenata Airport">Zenata Airport</a></td>
<td><a href="/wiki/Tlemcen" title="Tlemcen">Tlemcen</a>
</td></tr>
<tr>
<td>DAOO</td>
<td>ORN</td>
<td><a href="/wiki/Es_Senia_Airport" class="mw-redirect" title="Es Senia Airport">Es Senia Airport</a></td>
<td><a href="/wiki/Oran" title="Oran">Oran</a>
</td></tr>
<tr>
<td>DAOR</td>
<td>CBH</td>
<td><a href="/wiki/B%C3%A9char_Ouakda_Airport" class="mw-redirect" title="Béchar Ouakda Airport">Béchar Ouakda Airport</a></td>
<td><a href="/wiki/B%C3%A9char" title="Béchar">Béchar</a>
</td></tr>
<tr>
<td>DAOS</td>
<td>BFW</td>
<td><a href="/wiki/Sidi_Bel_Abb%C3%A8s_Airport" title="Sidi Bel Abbès Airport">Sidi Bel Abbès Airport</a></td>
<td><a href="/wiki/Sidi_Bel_Abb%C3%A8s" title="Sidi Bel Abbès">Sidi Bel Abbès</a>
</td></tr>
<tr>
<td>DAOV</td>
<td>MUW</td>
<td><a href="/wiki/Ghriss_Airport" title="Ghriss Airport">Ghriss Airport</a></td>
<td><a href="/wiki/Ghriss" title="Ghriss">Ghriss</a>
</td></tr>
<tr>
<td>DATG</td>
<td>INF</td>
<td><a href="/wiki/In_Guezzam_Airport" title="In Guezzam Airport">In Guezzam Airport</a></td>
<td><a href="/wiki/In_Guezzam" title="In Guezzam">In Guezzam</a>
</td></tr>
<tr>
<td>DATM</td>
<td>BMW</td>
<td><a href="/wiki/Bordj_Mokhtar_Airport" class="mw-redirect" title="Bordj Mokhtar Airport">Bordj Mokhtar Airport</a></td>
<td><a href="/wiki/Bordj_Mokhtar" class="mw-redirect" title="Bordj Mokhtar">Bordj Mokhtar</a>
</td></tr>
<tr>
<td>DAUA</td>
<td>AZR</td>
<td><a href="/wiki/Touat_Cheikh_Sidi_Mohamed_Belkebir_Airport" class="mw-redirect" title="Touat Cheikh Sidi Mohamed Belkebir Airport">Touat Cheikh Sidi Mohamed Belkebir Airport</a></td>
<td><a href="/wiki/Adrar,_Algeria" title="Adrar, Algeria">Adrar</a>
</td></tr>
<tr>
<td>DAUB</td>
<td>BSK</td>
<td><a href="/wiki/Biskra_Airport" title="Biskra Airport">Biskra Airport</a></td>
<td><a href="/wiki/Biskra" title="Biskra">Biskra</a>
</td></tr>
<tr>
<td>DAUE</td>
<td>ELG</td>
<td><a href="/wiki/El_Golea_Airport" title="El Golea Airport">El Golea Airport</a></td>
<td><a href="/wiki/El_Golea" class="mw-redirect" title="El Golea">El Golea</a>
</td></tr>
<tr>
<td>DAUG</td>
<td>GHA</td>
<td><a href="/wiki/Noumerate_Airport" class="mw-redirect" title="Noumerate Airport">Noumerate Airport</a></td>
<td><a href="/wiki/Ghardaia" class="mw-redirect" title="Ghardaia">Ghardaia</a>
</td></tr>
<tr>
<td>DAUH</td>
<td>HME</td>
<td><a href="/wiki/Oued_Irara_Airport" class="mw-redirect" title="Oued Irara Airport">Oued Irara Airport</a></td>
<td><a href="/wiki/Hassi_Messaoud" title="Hassi Messaoud">Hassi Messaoud</a>
</td></tr>
<tr>
<td>DAUI</td>
<td>INZ</td>
<td><a href="/wiki/In_Salah_Airport" title="In Salah Airport">In Salah Airport</a></td>
<td><a href="/wiki/In_Salah" title="In Salah">In Salah</a>
</td></tr>
<tr>
<td>DAUK</td>
<td>TGR</td>
<td><a href="/wiki/Touggourt_Sidi_Madhi_Airport" class="mw-redirect" title="Touggourt Sidi Madhi Airport">Touggourt Sidi Madhi Airport</a></td>
<td><a href="/wiki/Touggourt" title="Touggourt">Touggourt</a>
</td></tr>
<tr>
<td>DAUL</td>
<td>LOO</td>
<td><a href="/wiki/L%27Mekrareg_Airport" title="L'Mekrareg Airport">L'Mekrareg Airport</a></td>
<td><a href="/wiki/Laghouat" title="Laghouat">Laghouat</a>
</td></tr>
<tr>
<td>DAUO</td>
<td>ELU</td>
<td><a href="/wiki/Guemar_Airport" title="Guemar Airport">Guemar Airport</a></td>
<td><a href="/wiki/El_Oued" title="El Oued">El Oued</a>
</td></tr>
<tr>
<td>DAUT</td>
<td>TMX</td>
<td><a href="/wiki/Timimoun_Airport" title="Timimoun Airport">Timimoun Airport</a></td>
<td><a href="/wiki/Timimoun" title="Timimoun">Timimoun</a>
</td></tr>
<tr>
<td>DAUU</td>
<td>OGX</td>
<td><a href="/wiki/Ain_el_Beida_Airport" class="mw-redirect" title="Ain el Beida Airport">Ain el Beida Airport</a></td>
<td><a href="/wiki/Ouargla" title="Ouargla">Ouargla</a>
</td></tr>
<tr>
<td>DAUZ</td>
<td>IAM</td>
<td><a href="/wiki/In_Amenas_Airport" title="In Amenas Airport">In Amenas Airport</a></td>
<td><a href="/wiki/In_Amenas" title="In Amenas">In Amenas</a>
</td></tr></tbody></table>
'''
soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open('DA - Algeria.csv', mode='w', newline='', encoding='utf-8') as csv_file:
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

