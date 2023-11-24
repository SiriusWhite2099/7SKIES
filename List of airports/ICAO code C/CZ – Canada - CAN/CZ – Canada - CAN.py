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
<td>CZAC</td>
<td>ZAC</td>
<td><a href="/wiki/York_Landing_Airport" title="York Landing Airport">York Landing Airport</a></td>
<td><a href="/wiki/York_Factory_First_Nation" title="York Factory First Nation">York Factory First Nation</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZAM</td>
<td>YSN</td>
<td><a href="/wiki/Salmon_Arm_Airport" title="Salmon Arm Airport">Salmon Arm Airport</a></td>
<td><a href="/wiki/Salmon_Arm" title="Salmon Arm">Salmon Arm</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CZBA</td>
<td></td>
<td><a href="/wiki/Burlington_Executive_Airport" title="Burlington Executive Airport">Burlington Executive Airport</a></td>
<td><a href="/wiki/Burlington,_Ontario" title="Burlington, Ontario">Burlington</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CZBB</td>
<td>YDT</td>
<td><a href="/wiki/Boundary_Bay_Airport" title="Boundary Bay Airport">Boundary Bay Airport</a> (Vancouver/Boundary Bay Airport</td>
<td><a href="/wiki/Delta,_British_Columbia" title="Delta, British Columbia">Delta</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CZBD</td>
<td>ILF</td>
<td><a href="/wiki/Ilford_Airport" title="Ilford Airport">Ilford Airport</a></td>
<td><a href="/wiki/Ilford,_Manitoba" title="Ilford, Manitoba">Ilford</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZBF</td>
<td>ZBF</td>
<td><a href="/wiki/Bathurst_Airport_(New_Brunswick)" title="Bathurst Airport (New Brunswick)">Bathurst Airport</a></td>
<td><a href="/wiki/Bathurst,_New_Brunswick" title="Bathurst, New Brunswick">Bathurst</a></td>
<td><a href="/wiki/New_Brunswick" title="New Brunswick">NB</a>
</td></tr>
<tr>
<td>CZBM</td>
<td>ZBM</td>
<td><a href="/wiki/Roland-D%C3%A9sourdy_Airport" title="Roland-Désourdy Airport">Roland-Désourdy Airport</a></td>
<td><a href="/wiki/Bromont,_Quebec" class="mw-redirect" title="Bromont, Quebec">Bromont</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CZEE</td>
<td>KES</td>
<td><a href="/wiki/Kelsey_Airport" title="Kelsey Airport">Kelsey Airport</a></td>
<td><a href="/wiki/Kelsey,_Manitoba" title="Kelsey, Manitoba">Kelsey</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZEM</td>
<td>ZEM</td>
<td><a href="/wiki/Eastmain_River_Airport" title="Eastmain River Airport">Eastmain River Airport</a></td>
<td><a href="/wiki/Eastmain" title="Eastmain">Eastmain</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CZF2</td>
<td></td>
<td><a href="/wiki/Zephyr/Dillon_Field_Aerodrome" title="Zephyr/Dillon Field Aerodrome">Zephyr/Dillon Field Aerodrome</a></td>
<td><a href="/wiki/Uxbridge,_Ontario" title="Uxbridge, Ontario">Zephyr</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CZFA</td>
<td>ZFA</td>
<td><a href="/wiki/Faro_Airport_(Yukon)" title="Faro Airport (Yukon)">Faro Airport</a></td>
<td><a href="/wiki/Faro,_Yukon" title="Faro, Yukon">Faro</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CZFD</td>
<td>ZFD</td>
<td><a href="/wiki/Fond-du-Lac_Airport" title="Fond-du-Lac Airport">Fond-du-Lac Airport</a></td>
<td><a href="/wiki/Fond_du_Lac_Denesuline_First_Nation" title="Fond du Lac Denesuline First Nation">Fond du Lac Denesuline First Nation</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CZFG</td>
<td>XPK</td>
<td><a href="/wiki/Pukatawagan_Airport" title="Pukatawagan Airport">Pukatawagan Airport</a></td>
<td><a href="/wiki/Pukatawagan" title="Pukatawagan">Pukatawagan</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZFM</td>
<td>ZFM</td>
<td><a href="/wiki/Fort_McPherson_Airport" title="Fort McPherson Airport">Fort McPherson Airport</a></td>
<td><a href="/wiki/Fort_McPherson,_Northwest_Territories" title="Fort McPherson, Northwest Territories">Fort McPherson</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CZFN</td>
<td>ZFN</td>
<td><a href="/wiki/Tulita_Airport" title="Tulita Airport">Tulita Airport</a></td>
<td><a href="/wiki/Tulita" title="Tulita">Tulita</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CZGF</td>
<td>ZGF</td>
<td><a href="/wiki/Grand_Forks_Airport" title="Grand Forks Airport">Grand Forks Airport</a></td>
<td><a href="/wiki/Grand_Forks,_British_Columbia" title="Grand Forks, British Columbia">Grand Forks</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CZGI</td>
<td>ZGI</td>
<td><a href="/wiki/Gods_River_Airport" title="Gods River Airport">Gods River Airport</a></td>
<td><a href="/wiki/Manto_Sipi_Cree_Nation" title="Manto Sipi Cree Nation">Manto Sipi Cree Nation</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZGR</td>
<td>ZGR</td>
<td><a href="/wiki/Little_Grand_Rapids_Airport" title="Little Grand Rapids Airport">Little Grand Rapids Airport</a></td>
<td><a href="/wiki/Little_Grand_Rapids" title="Little Grand Rapids">Little Grand Rapids</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZHP</td>
<td></td>
<td><a href="/wiki/High_Prairie_Airport" title="High Prairie Airport">High Prairie Airport</a></td>
<td><a href="/wiki/High_Prairie" title="High Prairie">High Prairie</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CZJG</td>
<td>ZJG</td>
<td><a href="/wiki/Jenpeg_Airport" title="Jenpeg Airport">Jenpeg Airport</a></td>
<td><a href="/wiki/Unorganized_Division_No._22,_Manitoba" title="Unorganized Division No. 22, Manitoba">Jenpeg</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZJN</td>
<td>ZJN</td>
<td><a href="/wiki/Swan_River_Airport" title="Swan River Airport">Swan River Airport</a></td>
<td><a href="/wiki/Swan_River,_Manitoba" title="Swan River, Manitoba">Swan River</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZKE</td>
<td>ZKE</td>
<td><a href="/wiki/Kashechewan_Airport" title="Kashechewan Airport">Kashechewan Airport</a></td>
<td><a href="/wiki/Kashechewan_First_Nation" title="Kashechewan First Nation">Kashechewan First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CZLQ</td>
<td>YTD</td>
<td><a href="/wiki/Thicket_Portage_Airport" title="Thicket Portage Airport">Thicket Portage Airport</a></td>
<td><a href="/wiki/Thicket_Portage" title="Thicket Portage">Thicket Portage</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZMD</td>
<td>MSA</td>
<td><a href="/wiki/Muskrat_Dam_Airport" title="Muskrat Dam Airport">Muskrat Dam Airport</a></td>
<td><a href="/wiki/Muskrat_Dam_Lake_First_Nation" title="Muskrat Dam Lake First Nation">Muskrat Dam Lake First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CZML</td>
<td>ZMH</td>
<td><a href="/wiki/South_Cariboo_Regional_Airport" title="South Cariboo Regional Airport">South Cariboo Regional Airport</a> (108 Mile Ranch Airport</td>
<td><a href="/wiki/108_Mile_Ranch" title="108 Mile Ranch">108 Mile Ranch</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CZMN</td>
<td>PIW</td>
<td><a href="/wiki/Pikwitonei_Airport" title="Pikwitonei Airport">Pikwitonei Airport</a></td>
<td><a href="/wiki/Pikwitonei" title="Pikwitonei">Pikwitonei</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZMT</td>
<td>ZMT</td>
<td><a href="/wiki/Masset_Airport" title="Masset Airport">Masset Airport</a></td>
<td><a href="/wiki/Masset" title="Masset">Masset</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CZNG</td>
<td>XPP</td>
<td><a href="/wiki/Poplar_River_Airport" title="Poplar River Airport">Poplar River Airport</a></td>
<td><a href="/wiki/Poplar_River_First_Nation" title="Poplar River First Nation">Poplar River First Nation</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZNL</td>
<td></td>
<td><a href="/wiki/Nelson_Airport_(British_Columbia)" title="Nelson Airport (British Columbia)">Nelson Airport</a></td>
<td><a href="/wiki/Nelson,_British_Columbia" title="Nelson, British Columbia">Nelson</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CZPB</td>
<td>ZPB</td>
<td><a href="/wiki/Sachigo_Lake_Airport" title="Sachigo Lake Airport">Sachigo Lake Airport</a></td>
<td><a href="/wiki/Sachigo_Lake_First_Nation" title="Sachigo Lake First Nation">Sachigo Lake First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CZPC</td>
<td></td>
<td><a href="/wiki/Pincher_Creek_Airport" title="Pincher Creek Airport">Pincher Creek Airport</a></td>
<td><a href="/wiki/Pincher_Creek" title="Pincher Creek">Pincher Creek</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CZPO</td>
<td></td>
<td><a href="/wiki/Pinehouse_Lake_Airport" title="Pinehouse Lake Airport">Pinehouse Lake Airport</a></td>
<td><a href="/wiki/Pinehouse" title="Pinehouse">Pinehouse</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CZRJ</td>
<td>ZRJ</td>
<td><a href="/wiki/Round_Lake_(Weagamow_Lake)_Airport" title="Round Lake (Weagamow Lake) Airport">Round Lake (Weagamow Lake) Airport</a></td>
<td><a href="/wiki/North_Caribou_Lake_First_Nation" title="North Caribou Lake First Nation">North Caribou Lake First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CZSJ</td>
<td>ZSJ</td>
<td><a href="/wiki/Sandy_Lake_Airport" title="Sandy Lake Airport">Sandy Lake Airport</a></td>
<td><a href="/wiki/Sandy_Lake_First_Nation" title="Sandy Lake First Nation">Sandy Lake First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CZSN</td>
<td>XSI</td>
<td><a href="/wiki/South_Indian_Lake_Airport" title="South Indian Lake Airport">South Indian Lake Airport</a></td>
<td><a href="/wiki/South_Indian_Lake" title="South Indian Lake">South Indian Lake</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZST</td>
<td>ZST</td>
<td><a href="/wiki/Stewart_Aerodrome" title="Stewart Aerodrome">Stewart Aerodrome</a></td>
<td><a href="/wiki/Stewart,_British_Columbia" title="Stewart, British Columbia">Stewart</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CZSW</td>
<td>ZSW</td>
<td><a href="/wiki/Prince_Rupert/Seal_Cove_Water_Aerodrome" title="Prince Rupert/Seal Cove Water Aerodrome">Prince Rupert/Seal Cove Water Aerodrome</a></td>
<td><a href="/wiki/Prince_Rupert,_British_Columbia" title="Prince Rupert, British Columbia">Prince Rupert</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CZTA</td>
<td>YDV</td>
<td><a href="/wiki/Bloodvein_River_Airport" title="Bloodvein River Airport">Bloodvein River Airport</a></td>
<td><a href="/wiki/Bloodvein_First_Nation" title="Bloodvein First Nation">Bloodvein First Nation</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZTM</td>
<td>ZTM</td>
<td><a href="/wiki/Shamattawa_Airport" title="Shamattawa Airport">Shamattawa Airport</a></td>
<td><a href="/wiki/Shamattawa_First_Nation" title="Shamattawa First Nation">Shamattawa First Nation</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZUC</td>
<td>ZUC</td>
<td><a href="/wiki/Ignace_Municipal_Airport" title="Ignace Municipal Airport">Ignace Municipal Airport</a></td>
<td><a href="/wiki/Ignace" title="Ignace">Ignace</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CZUM</td>
<td>ZUM</td>
<td><a href="/wiki/Churchill_Falls_Airport" title="Churchill Falls Airport">Churchill Falls Airport</a></td>
<td><a href="/wiki/Churchill_Falls" title="Churchill Falls">Churchill Falls</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CZVL</td>
<td>ZVL</td>
<td><a href="/wiki/Edmonton/Villeneuve_Airport" title="Edmonton/Villeneuve Airport">Edmonton/Villeneuve Airport</a> (Villeneuve Airport)</td>
<td><a href="/wiki/Villeneuve,_Alberta" title="Villeneuve, Alberta">Villeneuve</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CZWH</td>
<td>XLB</td>
<td><a href="/wiki/Lac_Brochet_Airport" title="Lac Brochet Airport">Lac Brochet Airport</a></td>
<td><a href="/wiki/Lac_Brochet,_Manitoba" title="Lac Brochet, Manitoba">Lac Brochet</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CZWL</td>
<td>ZWL</td>
<td><a href="/wiki/Wollaston_Lake_Airport" title="Wollaston Lake Airport">Wollaston Lake Airport</a></td>
<td><a href="/wiki/Hatchet_Lake_Dene_Nation" class="mw-redirect" title="Hatchet Lake Dene Nation">Hatchet Lake Dene Nation</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open('CZ – Canada - CAN.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['ICAO', 'IATA', 'Airport Name', 'Community', 'Province or territory']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    rows = table.find_all('tr')

    for row in rows[1:]:  # Ignorer la première ligne car c'est l'en-tête
        columns = row.find_all('td')
        icao = columns[0].text.strip()
        iata = columns[1].text.strip()
        airport_name = columns[2].text.strip()
        community = columns[3].text.strip()
        Province_or_territory = columns[4].text.strip()

        writer.writerow({'ICAO': icao, 'IATA': iata, 'Airport Name': airport_name, 'Community': community, 'Province or territory': Province_or_territory})

print("Le fichier CSV a été créé avec succès.")