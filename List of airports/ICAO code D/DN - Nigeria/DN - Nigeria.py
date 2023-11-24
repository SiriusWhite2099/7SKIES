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
<td>DNAA</td>
<td>ABV</td>
<td><a href="/wiki/Nnamdi_Azikiwe_International_Airport" title="Nnamdi Azikiwe International Airport">Nnamdi Azikiwe International Airport</a></td>
<td><a href="/wiki/Abuja" title="Abuja">Abuja</a></td>
<td><a href="/wiki/Federal_Capital_Territory,_Nigeria" class="mw-redirect" title="Federal Capital Territory, Nigeria">Federal Capital Territory (FCT)</a>
</td></tr>
<tr>
<td>DNAK</td>
<td>AKR</td>
<td><a href="/wiki/Akure_Airport" title="Akure Airport">Akure Airport</a></td>
<td><a href="/wiki/Akure" title="Akure">Akure</a></td>
<td><a href="/wiki/Ondo_State" title="Ondo State">Ondo State</a>
</td></tr>
<tr>
<td>DNAI</td>
<td>QUO</td>
<td><a href="/wiki/Akwa_Ibom_International_Airport" class="mw-redirect" title="Akwa Ibom International Airport">Akwa Ibom International Airport</a></td>
<td><a href="/wiki/Uyo" title="Uyo">Uyo</a></td>
<td><a href="/wiki/Akwa_Ibom_State" title="Akwa Ibom State">Akwa Ibom State</a>
</td></tr>
<tr>
<td>DNAS</td>
<td>ABB</td>
<td><a href="/wiki/Asaba_International_Airport" title="Asaba International Airport">Asaba International Airport</a></td>
<td><a href="/wiki/Asaba" title="Asaba">Asaba</a> and <a href="/wiki/Delta_State" title="Delta State">Delta State</a></td>
<td>Delta State
</td></tr>
<tr>
<td>DNBE</td>
<td>BNI</td>
<td><a href="/wiki/Benin_Airport" title="Benin Airport">Benin Airport</a></td>
<td><a href="/wiki/Benin_City" title="Benin City">Benin City</a></td>
<td><a href="/wiki/Edo_State" title="Edo State">Edo State</a>
</td></tr>
<tr>
<td>DNBI</td>
<td></td>
<td><a href="/wiki/Bida_Airstrip" title="Bida Airstrip">Bida Airstrip</a></td>
<td><a href="/wiki/Bida,_Nigeria" class="mw-redirect" title="Bida, Nigeria">Bida</a></td>
<td><a href="/wiki/Niger_State" title="Niger State">Niger State</a>
</td></tr>
<tr>
<td>DNBK</td>
<td></td>
<td><a href="/wiki/Sir_Ahmadu_Bello_International_Airport" title="Sir Ahmadu Bello International Airport">Sir Ahmadu Bello International Airport</a></td>
<td><a href="/wiki/Birnin_Kebbi" title="Birnin Kebbi">Birnin Kebbi</a></td>
<td><a href="/wiki/Kebbi_State" title="Kebbi State">Kebbi State</a>
</td></tr>
<tr>
<td>DNCA</td>
<td>CBQ</td>
<td><a href="/wiki/Margaret_Ekpo_International_Airport" title="Margaret Ekpo International Airport">Margaret Ekpo International Airport</a></td>
<td><a href="/wiki/Calabar" title="Calabar">Calabar</a></td>
<td><a href="/wiki/Cross_River_State" title="Cross River State">Cross River State</a>
</td></tr>
<tr>
<td>DNDS</td>
<td>(pending)</td>
<td><a href="/wiki/Dutse_International_Airport" title="Dutse International Airport">Dutse International Airport</a></td>
<td><a href="/wiki/Dutse" title="Dutse">Dutse</a></td>
<td><a href="/wiki/Jigawa_State" title="Jigawa State">Jigawa State</a>
</td></tr>
<tr>
<td>DNEN</td>
<td>ENU</td>
<td><a href="/wiki/Akanu_Ibiam_International_Airport" title="Akanu Ibiam International Airport">Akanu Ibiam International Airport</a></td>
<td><a href="/wiki/Enugu" title="Enugu">Enugu</a></td>
<td><a href="/wiki/Enugu_State" title="Enugu State">Enugu State</a>
</td></tr>
<tr>
<td>DNGU</td>
<td>QUS</td>
<td><a href="/wiki/Gusau_Airstrip" title="Gusau Airstrip">Gusau Airstrip</a></td>
<td><a href="/wiki/Gusau" title="Gusau">Gusau</a></td>
<td><a href="/wiki/Zamfara_State" title="Zamfara State">Zamfara State</a>
</td></tr>
<tr>
<td>DNIB</td>
<td>IBA</td>
<td><a href="/wiki/Ibadan_Airport" title="Ibadan Airport">Ibadan Airport</a></td>
<td><a href="/wiki/Ibadan" title="Ibadan">Ibadan</a></td>
<td><a href="/wiki/Oyo_State" title="Oyo State">Oyo State</a>
</td></tr>
<tr>
<td>DNIL</td>
<td>ILR</td>
<td><a href="/wiki/Ilorin_International_Airport" title="Ilorin International Airport">Ilorin International Airport</a></td>
<td><a href="/wiki/Ilorin" title="Ilorin">Ilorin</a></td>
<td><a href="/wiki/Kwara_State" title="Kwara State">Kwara State</a>
</td></tr>
<tr>
<td>DNIM</td>
<td>QOW</td>
<td><a href="/wiki/Sam_Mbakwe_International_Cargo_Airport" class="mw-redirect" title="Sam Mbakwe International Cargo Airport">Sam Mbakwe International Cargo Airport</a></td>
<td><a href="/wiki/Owerri" title="Owerri">Owerri</a></td>
<td><a href="/wiki/Imo_State" title="Imo State">Imo State</a>
</td></tr>
<tr>
<td>DNJO</td>
<td>JOS</td>
<td><a href="/wiki/Jos_Airport" class="mw-redirect" title="Jos Airport">Jos Airport</a></td>
<td><a href="/wiki/Jos" title="Jos">Jos</a></td>
<td><a href="/wiki/Plateau_State" title="Plateau State">Plateau State</a>
</td></tr>
<tr>
<td>DNKA</td>
<td>KAD</td>
<td><a href="/wiki/Kaduna_Airport" class="mw-redirect" title="Kaduna Airport">Kaduna International Airport</a></td>
<td><a href="/wiki/Kaduna" title="Kaduna">Kaduna</a></td>
<td><a href="/wiki/Kaduna_State" title="Kaduna State">Kaduna State</a>
</td></tr>
<tr>
<td>DNKN</td>
<td>KAN</td>
<td><a href="/wiki/Mallam_Aminu_Kano_International_Airport" title="Mallam Aminu Kano International Airport">Mallam Aminu Kano International Airport</a></td>
<td><a href="/wiki/Kano_(city)" title="Kano (city)">Kano</a></td>
<td><a href="/wiki/Kano_State" title="Kano State">Kano State</a>
</td></tr>
<tr>
<td>DNMA</td>
<td>MIU</td>
<td><a href="/wiki/Maiduguri_International_Airport" title="Maiduguri International Airport">Maiduguri International Airport</a></td>
<td><a href="/wiki/Maiduguri" title="Maiduguri">Maiduguri</a></td>
<td><a href="/wiki/Borno_State" title="Borno State">Borno State</a>
</td></tr>
<tr>
<td>DNMK</td>
<td>MDI</td>
<td><a href="/wiki/Makurdi_Air_Force_Base" class="mw-redirect" title="Makurdi Air Force Base">Makurdi Air Force Base</a></td>
<td><a href="/wiki/Makurdi" title="Makurdi">Makurdi</a></td>
<td><a href="/wiki/Benue_State" title="Benue State">Benue State</a>
</td></tr>
<tr>
<td>DNMM</td>
<td>LOS</td>
<td><a href="/wiki/Murtala_Mohammed_International_Airport" class="mw-redirect" title="Murtala Mohammed International Airport">Murtala Mohammed International Airport</a></td>
<td><a href="/wiki/Ikeja" title="Ikeja">Ikeja</a></td>
<td><a href="/wiki/Lagos_State" title="Lagos State">Lagos State</a>
</td></tr>
<tr>
<td>DNMN</td>
<td>MXJ</td>
<td><a href="/wiki/Minna_Airport" title="Minna Airport">Minna Airport</a></td>
<td><a href="/wiki/Minna" title="Minna">Minna</a></td>
<td><a href="/wiki/Niger_State" title="Niger State">Niger State</a>
</td></tr>
<tr>
<td>DNOS</td>
<td></td>
<td><a href="/w/index.php?title=Osogbo_Airstrip&amp;action=edit&amp;redlink=1" class="new" title="Osogbo Airstrip (page does not exist)">Osogbo Airstrip</a></td>
<td><a href="/wiki/Osogbo" title="Osogbo">Osogbo</a></td>
<td><a href="/wiki/Osun_State" title="Osun State">Osun State</a>
</td></tr>
<tr>
<td>DNPO</td>
<td>PHC</td>
<td><a href="/wiki/Port_Harcourt_International_Airport" title="Port Harcourt International Airport">Port Harcourt International Airport</a></td>
<td><a href="/wiki/Port_Harcourt" title="Port Harcourt">Port Harcourt</a></td>
<td><a href="/wiki/Rivers_State" title="Rivers State">Rivers State</a>
</td></tr>
<tr>
<td>DNSO</td>
<td>SKO</td>
<td><a href="/wiki/Sadiq_Abubakar_III_International_Airport" title="Sadiq Abubakar III International Airport">Sadiq Abubakar III International Airport</a></td>
<td><a href="/wiki/Sokoto" title="Sokoto">Sokoto</a></td>
<td><a href="/wiki/Sokoto_State" title="Sokoto State">Sokoto State</a>
</td></tr>
<tr>
<td>DNYO</td>
<td>YOL</td>
<td><a href="/wiki/Yola_Airport" title="Yola Airport">Yola Airport</a></td>
<td><a href="/wiki/Yola,_Nigeria" title="Yola, Nigeria">Yola</a></td>
<td><a href="/wiki/Adamawa_State" title="Adamawa State">Adamawa State</a>
</td></tr>
<tr>
<td>DNZA</td>
<td>ZAR</td>
<td><a href="/wiki/Zaria_Airport" title="Zaria Airport">Zaria Airport</a></td>
<td><a href="/wiki/Zaria,_Nigeria" class="mw-redirect" title="Zaria, Nigeria">Zaria</a></td>
<td><a href="/wiki/Kaduna_State" title="Kaduna State">Kaduna State</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open('DN-Nigeria.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ICAO', 'IATA', 'Airport Name', 'Community', 'Province or Territory']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    rows = table.find_all('tr')

    for row in rows[1:]:  # Ignorer la première ligne car c'est l'en-tête
        columns = row.find_all(['th', 'td'])

        # Vérifier que la ligne a le nombre attendu de colonnes
        if len(columns) >= len(fieldnames):
            icao = columns[0].text.strip()
            iata = columns[1].text.strip()
            airport_name = columns[2].text.strip()
            community = columns[3].text.strip()
            province_territory = columns[4].text.strip()

            writer.writerow({
                'ICAO': icao,
                'IATA': iata,
                'Airport Name': airport_name,
                'Community': community,
                'Province or Territory': province_territory
            })
        else:
            print(f"Ignorer la ligne avec un nombre incorrect de colonnes: {row}")

print("Le fichier CSV a été créé avec succès.")