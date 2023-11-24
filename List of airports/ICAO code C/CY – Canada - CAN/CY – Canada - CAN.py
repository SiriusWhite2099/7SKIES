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
<td>CYAB</td>
<td>YAB</td>
<td><a href="/wiki/Arctic_Bay_Airport" title="Arctic Bay Airport">Arctic Bay Airport</a></td>
<td><a href="/wiki/Arctic_Bay" title="Arctic Bay">Arctic Bay</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYAC</td>
<td>YAC</td>
<td><a href="/wiki/Cat_Lake_Airport" title="Cat Lake Airport">Cat Lake Airport</a></td>
<td><a href="/wiki/Cat_Lake_First_Nation" title="Cat Lake First Nation">Cat Lake First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYAD</td>
<td>YAR</td>
<td><a href="/wiki/La_Grande-3_Airport" title="La Grande-3 Airport">La Grande-3 Airport</a></td>
<td><a href="/wiki/La_Grande-3_generating_station" title="La Grande-3 generating station">La Grande-3 generating station</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYAG</td>
<td>YAG</td>
<td><a href="/wiki/Fort_Frances_Municipal_Airport" title="Fort Frances Municipal Airport">Fort Frances Municipal Airport</a></td>
<td><a href="/wiki/Fort_Frances" title="Fort Frances">Fort Frances</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYAH</td>
<td>YAH</td>
<td><a href="/wiki/La_Grande-4_Airport" title="La Grande-4 Airport">La Grande-4 Airport</a></td>
<td><a href="/wiki/La_Grande-4_generating_station" title="La Grande-4 generating station">La Grande-4 generating station</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYAL</td>
<td>YAL</td>
<td><a href="/wiki/Alert_Bay_Airport" title="Alert Bay Airport">Alert Bay Airport</a></td>
<td><a href="/wiki/Alert_Bay" title="Alert Bay">Alert Bay</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYAM</td>
<td>YAM</td>
<td><a href="/wiki/Sault_Ste._Marie_Airport" title="Sault Ste. Marie Airport">Sault Ste. Marie Airport</a></td>
<td><a href="/wiki/Sault_Ste._Marie,_Ontario" title="Sault Ste. Marie, Ontario">Sault Ste. Marie</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYAQ</td>
<td>XKS</td>
<td><a href="/wiki/Kasabonika_Airport" title="Kasabonika Airport">Kasabonika Airport</a></td>
<td><a href="/wiki/Kasabonika_Lake_First_Nation" title="Kasabonika Lake First Nation">Kasabonika Lake First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYAS</td>
<td>YKG</td>
<td><a href="/wiki/Kangirsuk_Airport" title="Kangirsuk Airport">Kangirsuk Airport</a></td>
<td><a href="/wiki/Kangirsuk" title="Kangirsuk">Kangirsuk</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYAT</td>
<td>YAT</td>
<td><a href="/wiki/Attawapiskat_Airport" title="Attawapiskat Airport">Attawapiskat Airport</a></td>
<td><a href="/wiki/Attawapiskat_First_Nation" title="Attawapiskat First Nation">Attawapiskat First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYAU</td>
<td></td>
<td><a href="/wiki/South_Shore_Regional_Airport" title="South Shore Regional Airport">South Shore Regional Airport</a> (Liverpool/South Shore Regional Airport)</td>
<td><a href="/wiki/Liverpool,_Nova_Scotia" title="Liverpool, Nova Scotia">Liverpool</a></td>
<td><a href="/wiki/Nova_Scotia" title="Nova Scotia">NS</a>
</td></tr>
<tr>
<td>CYAV</td>
<td></td>
<td><a href="/wiki/St._Andrews_Airport" class="mw-redirect" title="St. Andrews Airport">St. Andrews Airport</a> (Winnipeg/St. Andrews Airport)</td>
<td><a href="/wiki/Rural_Municipality_of_St._Andrews" title="Rural Municipality of St. Andrews">Rural Municipality of St. Andrews</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYAW</td>
<td>YAW</td>
<td><a href="/wiki/CFB_Shearwater" title="CFB Shearwater">CFB Shearwater</a> (Halifax/Shearwater Heliport)</td>
<td><a href="/wiki/Shearwater,_Nova_Scotia" title="Shearwater, Nova Scotia">Shearwater</a></td>
<td><a href="/wiki/Nova_Scotia" title="Nova Scotia">NS</a>
</td></tr>
<tr>
<td>CYAX</td>
<td></td>
<td><a href="/wiki/Lac_du_Bonnet_Airport" title="Lac du Bonnet Airport">Lac du Bonnet Airport</a></td>
<td><a href="/wiki/Lac_du_Bonnet,_Manitoba" title="Lac du Bonnet, Manitoba">Lac du Bonnet</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYAY</td>
<td>YAY</td>
<td><a href="/wiki/St._Anthony_Airport" title="St. Anthony Airport">St. Anthony Airport</a></td>
<td><a href="/wiki/St._Anthony,_Newfoundland_and_Labrador" title="St. Anthony, Newfoundland and Labrador">St. Anthony</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYAZ</td>
<td>YAZ</td>
<td><a href="/wiki/Tofino/Long_Beach_Airport" class="mw-redirect" title="Tofino/Long Beach Airport">Tofino/Long Beach Airport</a></td>
<td><a href="/wiki/Tofino" title="Tofino">Tofino</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYB3</td>
<td></td>
<td><a href="/wiki/List_of_heliports_in_Canada#77" title="List of heliports in Canada">Nelson/Baylock Estate Heliport</a></td>
<td><a href="/wiki/Nelson,_British_Columbia" title="Nelson, British Columbia">Nelson, British Columbia</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYBA</td>
<td></td>
<td><a href="/wiki/Banff_Airport" title="Banff Airport">Banff Airport</a></td>
<td><a href="/wiki/Banff,_Alberta" title="Banff, Alberta">Banff</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYBB</td>
<td>YBB</td>
<td><a href="/wiki/Kugaaruk_Airport" title="Kugaaruk Airport">Kugaaruk Airport</a></td>
<td><a href="/wiki/Kugaaruk" title="Kugaaruk">Kugaaruk</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYBC</td>
<td>YBC</td>
<td><a href="/wiki/Baie-Comeau_Airport" title="Baie-Comeau Airport">Baie-Comeau Airport</a></td>
<td><a href="/wiki/Baie-Comeau" title="Baie-Comeau">Baie-Comeau</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYBD</td>
<td>QBC</td>
<td><a href="/wiki/Bella_Coola_Airport" title="Bella Coola Airport">Bella Coola Airport</a></td>
<td><a href="/wiki/Bella_Coola,_British_Columbia" title="Bella Coola, British Columbia">Bella Coola</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYBE</td>
<td>YBE</td>
<td><a href="/wiki/Uranium_City_Airport" title="Uranium City Airport">Uranium City Airport</a></td>
<td><a href="/wiki/Uranium_City" title="Uranium City">Uranium City</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYBF</td>
<td></td>
<td><a href="/wiki/Bonnyville_Airport" title="Bonnyville Airport">Bonnyville Airport</a></td>
<td><a href="/wiki/Bonnyville" title="Bonnyville">Bonnyville</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYBG</td>
<td>YBG</td>
<td><a href="/wiki/CFB_Bagotville" title="CFB Bagotville">CFB Bagotville</a> (Bagotville Airport)</td>
<td><a href="/wiki/La_Baie" title="La Baie">La Baie</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYBK</td>
<td>YBK</td>
<td><a href="/wiki/Baker_Lake_Airport" title="Baker Lake Airport">Baker Lake Airport</a></td>
<td><a href="/wiki/Baker_Lake,_Nunavut" title="Baker Lake, Nunavut">Baker Lake</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYBL</td>
<td>YBL</td>
<td><a href="/wiki/Campbell_River_Airport" title="Campbell River Airport">Campbell River Airport</a></td>
<td><a href="/wiki/Campbell_River,_British_Columbia" title="Campbell River, British Columbia">Campbell River</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYBN</td>
<td></td>
<td><a href="/wiki/CFB_Borden" title="CFB Borden">CFB Borden</a> (Borden Heliport)</td>
<td></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYBP</td>
<td></td>
<td><a href="/wiki/Brooks_Regional_Aerodrome" title="Brooks Regional Aerodrome">Brooks Regional Aerodrome</a></td>
<td><a href="/wiki/Brooks,_Alberta" title="Brooks, Alberta">Brooks</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYBQ</td>
<td>XTL</td>
<td><a href="/wiki/Tadoule_Lake_Airport" title="Tadoule Lake Airport">Tadoule Lake Airport</a></td>
<td><a href="/wiki/Tadoule_Lake" title="Tadoule Lake">Tadoule Lake</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYBR</td>
<td>YBR</td>
<td><a href="/wiki/Brandon_Municipal_Airport" title="Brandon Municipal Airport">Brandon Municipal Airport</a> (McGill Field)</td>
<td><a href="/wiki/Brandon,_Manitoba" title="Brandon, Manitoba">Brandon</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYBT</td>
<td>YBT</td>
<td><a href="/wiki/Brochet_Airport" title="Brochet Airport">Brochet Airport</a></td>
<td><a href="/wiki/Brochet,_Manitoba" title="Brochet, Manitoba">Brochet</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYBU</td>
<td>YBU</td>
<td><a href="/wiki/Nipawin_Airport" title="Nipawin Airport">Nipawin Airport</a></td>
<td><a href="/wiki/Nipawin" title="Nipawin">Nipawin</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYBV</td>
<td>YBV</td>
<td><a href="/wiki/Berens_River_Airport" title="Berens River Airport">Berens River Airport</a></td>
<td><a href="/wiki/Berens_River,_Manitoba" title="Berens River, Manitoba">Berens River</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYBW</td>
<td>YBW</td>
<td><a href="/wiki/Calgary/Springbank_Airport" title="Calgary/Springbank Airport">Calgary/Springbank Airport</a> (Springbank Airport)</td>
<td><a href="/wiki/Springbank,_Alberta" title="Springbank, Alberta">Springbank</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYBX</td>
<td>YBX</td>
<td><a href="/wiki/Lourdes-de-Blanc-Sablon_Airport" title="Lourdes-de-Blanc-Sablon Airport">Lourdes-de-Blanc-Sablon Airport</a></td>
<td><a href="/wiki/Blanc-Sablon,_Quebec" class="mw-redirect" title="Blanc-Sablon, Quebec">Blanc-Sablon</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYCB</td>
<td>YCB</td>
<td><a href="/wiki/Cambridge_Bay_Airport" title="Cambridge Bay Airport">Cambridge Bay Airport</a></td>
<td><a href="/wiki/Cambridge_Bay" title="Cambridge Bay">Cambridge Bay</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYCC</td>
<td>YCC</td>
<td><a href="/wiki/Cornwall_Regional_Airport" title="Cornwall Regional Airport">Cornwall Regional Airport</a></td>
<td><a href="/wiki/Cornwall,_Ontario" title="Cornwall, Ontario">Cornwall</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYCD</td>
<td>YCD</td>
<td><a href="/wiki/Nanaimo_Airport" title="Nanaimo Airport">Nanaimo Airport</a></td>
<td><a href="/wiki/Nanaimo" title="Nanaimo">Nanaimo</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYCE</td>
<td>YCE</td>
<td><a href="/wiki/Centralia/James_T._Field_Memorial_Aerodrome" title="Centralia/James T. Field Memorial Aerodrome">Centralia/James T. Field Memorial Aerodrome</a></td>
<td><a href="/wiki/South_Huron" title="South Huron">Centralia</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYCG</td>
<td>YCG</td>
<td><a href="/wiki/West_Kootenay_Regional_Airport" title="West Kootenay Regional Airport">West Kootenay Regional Airport</a> (Castlegar/West Kootenay Regional Airport)</td>
<td><a href="/wiki/Castlegar,_British_Columbia" title="Castlegar, British Columbia">Castlegar</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYCH</td>
<td>YCH</td>
<td><a href="/wiki/Miramichi_Airport" title="Miramichi Airport">Miramichi Airport</a></td>
<td><a href="/wiki/Miramichi,_New_Brunswick" title="Miramichi, New Brunswick">Miramichi</a></td>
<td><a href="/wiki/New_Brunswick" title="New Brunswick">NB</a>
</td></tr>
<tr>
<td>CYCK</td>
<td>XCM</td>
<td><a href="/wiki/Chatham-Kent_Airport" title="Chatham-Kent Airport">Chatham-Kent Airport</a></td>
<td><a href="/wiki/Chatham-Kent" title="Chatham-Kent">Chatham-Kent</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYCL</td>
<td>YCL</td>
<td><a href="/wiki/Charlo_Airport" title="Charlo Airport">Charlo Airport</a></td>
<td><a href="/wiki/Charlo,_New_Brunswick" title="Charlo, New Brunswick">Charlo</a></td>
<td><a href="/wiki/New_Brunswick" title="New Brunswick">NB</a>
</td></tr>
<tr>
<td>CYCN</td>
<td>YCN</td>
<td><a href="/wiki/Cochrane_Aerodrome" title="Cochrane Aerodrome">Cochrane Aerodrome</a></td>
<td><a href="/wiki/Cochrane,_Ontario" title="Cochrane, Ontario">Cochrane</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYCO</td>
<td>YCO</td>
<td><a href="/wiki/Kugluktuk_Airport" title="Kugluktuk Airport">Kugluktuk Airport</a></td>
<td><a href="/wiki/Kugluktuk" title="Kugluktuk">Kugluktuk</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYCP</td>
<td>YCP</td>
<td><a href="/wiki/Blue_River_Airport" title="Blue River Airport">Blue River Airport</a></td>
<td><a href="/wiki/Blue_River,_British_Columbia" title="Blue River, British Columbia">Blue River</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYCQ</td>
<td>YCQ</td>
<td><a href="/wiki/Chetwynd_Airport" title="Chetwynd Airport">Chetwynd Airport</a></td>
<td><a href="/wiki/Chetwynd,_British_Columbia" title="Chetwynd, British Columbia">Chetwynd</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYCR</td>
<td>YCR</td>
<td><a href="/wiki/Cross_Lake_(Charlie_Sinclair_Memorial)_Airport" title="Cross Lake (Charlie Sinclair Memorial) Airport">Cross Lake (Charlie Sinclair Memorial) Airport</a></td>
<td><a href="/wiki/Cross_Lake,_Manitoba" title="Cross Lake, Manitoba">Cross Lake</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYCS</td>
<td>YCS</td>
<td><a href="/wiki/Chesterfield_Inlet_Airport" title="Chesterfield Inlet Airport">Chesterfield Inlet Airport</a></td>
<td><a href="/wiki/Chesterfield_Inlet,_Nunavut" title="Chesterfield Inlet, Nunavut">Chesterfield Inlet</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYCT</td>
<td></td>
<td><a href="/wiki/Coronation_Airport" title="Coronation Airport">Coronation Airport</a></td>
<td><a href="/wiki/Coronation,_Alberta" title="Coronation, Alberta">Coronation</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYCW</td>
<td>YCW</td>
<td><a href="/wiki/Chilliwack_Airport" title="Chilliwack Airport">Chilliwack Airport</a></td>
<td><a href="/wiki/Chilliwack" title="Chilliwack">Chilliwack</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYCX</td>
<td>YCX</td>
<td><a href="/wiki/CFB_Gagetown" title="CFB Gagetown">CFB Gagetown</a> (Gagetown Heliport)</td>
<td><a href="/wiki/Oromocto" title="Oromocto">Oromocto</a></td>
<td><a href="/wiki/New_Brunswick" title="New Brunswick">NB</a>
</td></tr>
<tr>
<td>CYCY</td>
<td>YCY</td>
<td><a href="/wiki/Clyde_River_Airport" title="Clyde River Airport">Clyde River Airport</a></td>
<td><a href="/wiki/Clyde_River,_Nunavut" title="Clyde River, Nunavut">Clyde River</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYCZ</td>
<td>YCZ</td>
<td><a href="/wiki/Fairmont_Hot_Springs_Airport" title="Fairmont Hot Springs Airport">Fairmont Hot Springs Airport</a></td>
<td><a href="/wiki/Fairmont_Hot_Springs,_British_Columbia" title="Fairmont Hot Springs, British Columbia">Fairmont Hot Springs</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYD2</td>
<td></td>
<td><a href="/wiki/Graham_Lake_(Yellow_Dog_Lodge)_Water_Aerodrome" title="Graham Lake (Yellow Dog Lodge) Water Aerodrome">Graham Lake (Yellow Dog Lodge) Water Aerodrome</a></td>
<td><a href="/w/index.php?title=Graham_Lake_(Northwest_Territories)&amp;action=edit&amp;redlink=1" class="new" title="Graham Lake (Northwest Territories) (page does not exist)">Graham Lake</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYDA</td>
<td>YDA</td>
<td><a href="/wiki/Dawson_City_Airport" title="Dawson City Airport">Dawson City Airport</a></td>
<td><a href="/wiki/Dawson_City" title="Dawson City">Dawson City</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CYDB</td>
<td>YDB</td>
<td><a href="/wiki/Burwash_Airport" title="Burwash Airport">Burwash Airport</a></td>
<td><a href="/wiki/Burwash_Landing" title="Burwash Landing">Burwash Landing</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CYDC</td>
<td></td>
<td><a href="/wiki/Princeton_Aerodrome" title="Princeton Aerodrome">Princeton Aerodrome</a></td>
<td><a href="/wiki/Princeton,_British_Columbia" title="Princeton, British Columbia">Princeton</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYDF</td>
<td>YDF</td>
<td><a href="/wiki/Deer_Lake_Regional_Airport" title="Deer Lake Regional Airport">Deer Lake Regional Airport</a></td>
<td><a href="/wiki/Deer_Lake,_Newfoundland_and_Labrador" title="Deer Lake, Newfoundland and Labrador">Deer Lake</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYDH</td>
<td></td>
<td><a href="/wiki/List_of_heliports_in_Canada#183" title="List of heliports in Canada">Ottawa/Dwyer Hill Heliport</a></td>
<td><a href="/wiki/Ottawa" title="Ottawa">Ottawa</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYDL</td>
<td>YDL</td>
<td><a href="/wiki/Dease_Lake_Airport" title="Dease Lake Airport">Dease Lake Airport</a></td>
<td><a href="/wiki/Dease_Lake" title="Dease Lake">Dease Lake</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYDM</td>
<td>XRR</td>
<td><a href="/wiki/Ross_River_Airport" title="Ross River Airport">Ross River Airport</a></td>
<td><a href="/wiki/Ross_River,_Yukon" title="Ross River, Yukon">Ross River</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CYDN</td>
<td>YDN</td>
<td><a href="/wiki/Lt._Col_W.G._(Billy)_Barker_VC_Airport" title="Lt. Col W.G. (Billy) Barker VC Airport">Lt. Col W.G. (Billy) Barker VC Airport</a> (Dauphin (Lt. Col W.G. (Billy) Barker VC) Airport)</td>
<td><a href="/wiki/Dauphin,_Manitoba" title="Dauphin, Manitoba">Dauphin</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYDO</td>
<td>YDO</td>
<td><a href="/wiki/Dolbeau-Saint-F%C3%A9licien_Airport" title="Dolbeau-Saint-Félicien Airport">Dolbeau-Saint-Félicien Airport</a></td>
<td><a href="/wiki/Dolbeau-Mistassini" title="Dolbeau-Mistassini">Dolbeau-Mistassini</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYDP</td>
<td>YDP</td>
<td><a href="/wiki/Nain_Airport" title="Nain Airport">Nain Airport</a></td>
<td><a href="/wiki/Nain,_Newfoundland_and_Labrador" title="Nain, Newfoundland and Labrador">Nain</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYDQ</td>
<td>YDQ</td>
<td><a href="/wiki/Dawson_Creek_Airport" title="Dawson Creek Airport">Dawson Creek Airport</a></td>
<td><a href="/wiki/Dawson_Creek" title="Dawson Creek">Dawson Creek</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYEA</td>
<td></td>
<td><a href="/wiki/Empress_Airport" title="Empress Airport">Empress Airport</a></td>
<td><a href="/wiki/Empress,_Alberta" title="Empress, Alberta">Empress</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYED</td>
<td>YED</td>
<td><a href="/wiki/CFB_Edmonton" title="CFB Edmonton">CFB Edmonton</a> (Edmonton/Namao Heliport)</td>
<td><a href="/wiki/Edmonton" title="Edmonton">Edmonton</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYEE</td>
<td>YEE</td>
<td><a href="/wiki/Midland/Huronia_Airport" title="Midland/Huronia Airport">Midland/Huronia Airport</a></td>
<td><a href="/wiki/Midland,_Ontario" title="Midland, Ontario">Midland</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYEG</td>
<td>YEG</td>
<td><em><a href="/wiki/Edmonton_International_Airport" title="Edmonton International Airport">Edmonton International Airport</a></em></td>
<td><a href="/wiki/Nisku" title="Nisku">Nisku</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYEK</td>
<td>YEK</td>
<td><a href="/wiki/Arviat_Airport" title="Arviat Airport">Arviat Airport</a></td>
<td><a href="/wiki/Arviat" title="Arviat">Arviat</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYEL</td>
<td>YEL</td>
<td><a href="/wiki/Elliot_Lake_Municipal_Airport" title="Elliot Lake Municipal Airport">Elliot Lake Municipal Airport</a></td>
<td><a href="/wiki/Elliot_Lake" title="Elliot Lake">Elliot Lake</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYEM</td>
<td>YEM</td>
<td><a href="/wiki/Manitowaning/Manitoulin_East_Municipal_Airport" title="Manitowaning/Manitoulin East Municipal Airport">Manitowaning/Manitoulin East Municipal Airport</a></td>
<td><a href="/wiki/Assiginack" title="Assiginack">Manitowaning</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYEN</td>
<td>YEN</td>
<td><a href="/wiki/Estevan_Regional_Aerodrome" title="Estevan Regional Aerodrome">Estevan Regional Aerodrome</a></td>
<td><a href="/wiki/Estevan" title="Estevan">Estevan</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYER</td>
<td>YER</td>
<td><a href="/wiki/Fort_Severn_Airport" title="Fort Severn Airport">Fort Severn Airport</a></td>
<td><a href="/wiki/Fort_Severn_First_Nation" title="Fort Severn First Nation">Fort Severn First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYES</td>
<td></td>
<td><a href="/wiki/Edmundston_Airport" title="Edmundston Airport">Edmundston Airport</a></td>
<td><a href="/wiki/Edmundston" title="Edmundston">Edmundston</a></td>
<td><a href="/wiki/New_Brunswick" title="New Brunswick">NB</a>
</td></tr>
<tr>
<td>CYET</td>
<td>YET</td>
<td><a href="/wiki/Edson_Airport" title="Edson Airport">Edson Airport</a></td>
<td><a href="/wiki/Edson,_Alberta" title="Edson, Alberta">Edson</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYEU</td>
<td>YEU</td>
<td><a href="/wiki/Eureka_Aerodrome" title="Eureka Aerodrome">Eureka Aerodrome</a></td>
<td><a href="/wiki/Eureka,_Nunavut" title="Eureka, Nunavut">Eureka</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYEV</td>
<td>YEV</td>
<td><a href="/wiki/Inuvik_(Mike_Zubko)_Airport" title="Inuvik (Mike Zubko) Airport">Inuvik (Mike Zubko) Airport</a></td>
<td><a href="/wiki/Inuvik" title="Inuvik">Inuvik</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYEY</td>
<td>YEY</td>
<td><a href="/wiki/Amos/Magny_Airport" title="Amos/Magny Airport">Amos/Magny Airport</a></td>
<td><a href="/wiki/Amos,_Quebec" title="Amos, Quebec">Amos</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYFA</td>
<td>YFA</td>
<td><a href="/wiki/Fort_Albany_Airport" title="Fort Albany Airport">Fort Albany Airport</a></td>
<td><a href="/wiki/Fort_Albany_First_Nation" title="Fort Albany First Nation">Fort Albany First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYFB</td>
<td>YFB</td>
<td><em><a href="/wiki/Iqaluit_Airport" title="Iqaluit Airport">Iqaluit Airport</a></em></td>
<td><a href="/wiki/Iqaluit" title="Iqaluit">Iqaluit</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYFC</td>
<td>YFC</td>
<td><em><a href="/wiki/Fredericton_International_Airport" title="Fredericton International Airport">Fredericton International Airport</a></em> (Greater Fredericton International Airport)</td>
<td><a href="/wiki/Fredericton" title="Fredericton">Fredericton</a></td>
<td><a href="/wiki/New_Brunswick" title="New Brunswick">NB</a>
</td></tr>
<tr>
<td>CYFD</td>
<td>YFD</td>
<td><a href="/wiki/Brantford_Airport" title="Brantford Airport">Brantford Airport</a></td>
<td><a href="/wiki/Brantford" title="Brantford">Brantford</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYFE</td>
<td>YFE</td>
<td><a href="/wiki/Forestville_Airport" title="Forestville Airport">Forestville Airport</a></td>
<td><a href="/wiki/Forestville,_Quebec" title="Forestville, Quebec">Forestville</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYFH</td>
<td>YFH</td>
<td><a href="/wiki/Fort_Hope_Airport" title="Fort Hope Airport">Fort Hope Airport</a></td>
<td><a href="/wiki/Eabametoong_First_Nation" title="Eabametoong First Nation">Eabametoong First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYFI</td>
<td>YFI</td>
<td><a href="/wiki/Fort_MacKay/Firebag_Aerodrome" title="Fort MacKay/Firebag Aerodrome">Fort MacKay/Firebag Aerodrome</a></td>
<td><a href="/wiki/Fort_McKay" title="Fort McKay">Fort McKay</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYFJ</td>
<td></td>
<td><a href="/wiki/Mont_Tremblant_International_Airport" class="mw-redirect" title="Mont Tremblant International Airport">Mont Tremblant International Airport</a> (La Mazaca/Mont Tremblant International Airport)</td>
<td><a href="/wiki/Mont-Tremblant" title="Mont-Tremblant">Mont-Tremblant</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYFO</td>
<td>YFO</td>
<td><a href="/wiki/Flin_Flon_Airport" title="Flin Flon Airport">Flin Flon Airport</a></td>
<td><a href="/wiki/Flin_Flon" title="Flin Flon">Flin Flon</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYFR</td>
<td>YFR</td>
<td><a href="/wiki/Fort_Resolution_Airport" title="Fort Resolution Airport">Fort Resolution Airport</a></td>
<td><a href="/wiki/Fort_Resolution" title="Fort Resolution">Fort Resolution</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYFS</td>
<td>YFS</td>
<td><a href="/wiki/Fort_Simpson_Airport" title="Fort Simpson Airport">Fort Simpson Airport</a></td>
<td><a href="/wiki/Fort_Simpson" title="Fort Simpson">Fort Simpson</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYFT</td>
<td>YMN</td>
<td><a href="/wiki/Makkovik_Airport" title="Makkovik Airport">Makkovik Airport</a></td>
<td><a href="/wiki/Makkovik" title="Makkovik">Makkovik</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYG2</td>
<td></td>
<td><a href="/wiki/Parkhill_(Yellow_Gold)_Aerodrome" title="Parkhill (Yellow Gold) Aerodrome">Parkhill (Yellow Gold) Aerodrome</a></td>
<td><a href="/wiki/North_Middlesex,_Ontario" title="North Middlesex, Ontario">Parkhill</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYGB</td>
<td>YGB</td>
<td><a href="/wiki/Texada/Gillies_Bay_Airport" title="Texada/Gillies Bay Airport">Texada/Gillies Bay Airport</a></td>
<td><a href="/wiki/Texada_Island" title="Texada Island">Texada Island</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYGD</td>
<td>YGD</td>
<td><a href="/wiki/Goderich_Airport" title="Goderich Airport">Goderich Airport</a></td>
<td><a href="/wiki/Goderich,_Ontario" title="Goderich, Ontario">Goderich</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYGE</td>
<td>YGE</td>
<td><a href="/wiki/Golden_Airport" title="Golden Airport">Golden Airport</a></td>
<td><a href="/wiki/Golden,_British_Columbia" title="Golden, British Columbia">Golden</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYGH</td>
<td>YGH</td>
<td><a href="/wiki/Fort_Good_Hope_Airport" title="Fort Good Hope Airport">Fort Good Hope Airport</a></td>
<td><a href="/wiki/Fort_Good_Hope" title="Fort Good Hope">Fort Good Hope</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYGK</td>
<td>YGK</td>
<td><a href="/wiki/Kingston_Norman_Rogers_Airport" title="Kingston Norman Rogers Airport">Kingston Norman Rogers Airport</a> (Kingston Airport)</td>
<td><a href="/wiki/Kingston,_Ontario" title="Kingston, Ontario">Kingston</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYGL</td>
<td>YGL</td>
<td><a href="/wiki/La_Grande_Rivi%C3%A8re_Airport" title="La Grande Rivière Airport">La Grande Rivière Airport</a></td>
<td><a href="/wiki/Radisson,_Quebec" title="Radisson, Quebec">Radisson</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYGM</td>
<td>YGM</td>
<td><a href="/wiki/Gimli_Industrial_Park_Airport" title="Gimli Industrial Park Airport">Gimli Industrial Park Airport</a></td>
<td><a href="/wiki/Gimli,_Manitoba" title="Gimli, Manitoba">Gimli</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYGO</td>
<td>YGO</td>
<td><a href="/wiki/Gods_Lake_Narrows_Airport" title="Gods Lake Narrows Airport">Gods Lake Narrows Airport</a></td>
<td><a href="/wiki/Gods_Lake_Narrows" title="Gods Lake Narrows">Gods Lake Narrows</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYGP</td>
<td>YGP</td>
<td><a href="/wiki/Michel-Pouliot_Gasp%C3%A9_Airport" title="Michel-Pouliot Gaspé Airport">Michel-Pouliot Gaspé Airport</a> (Gaspé (Michel-Pouliot) Airport)</td>
<td><a href="/wiki/Gasp%C3%A9,_Quebec" title="Gaspé, Quebec">Gaspé</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYGQ</td>
<td>YGQ</td>
<td><a href="/wiki/Geraldton_(Greenstone_Regional)_Airport" title="Geraldton (Greenstone Regional) Airport">Geraldton (Greenstone Regional) Airport</a></td>
<td><a href="/wiki/Greenstone,_Ontario" title="Greenstone, Ontario">Greenstone</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYGR</td>
<td>YGR</td>
<td><a href="/wiki/%C3%8Eles-de-la-Madeleine_Airport" title="Îles-de-la-Madeleine Airport">Îles-de-la-Madeleine Airport</a></td>
<td><a href="/wiki/Magdalen_Islands" title="Magdalen Islands">Magdalen Islands</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYGT</td>
<td>YGT</td>
<td><a href="/wiki/Igloolik_Airport" title="Igloolik Airport">Igloolik Airport</a></td>
<td><a href="/wiki/Igloolik" title="Igloolik">Igloolik</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYGV</td>
<td>YGV</td>
<td><a href="/wiki/Havre_Saint-Pierre_Airport" title="Havre Saint-Pierre Airport">Havre Saint-Pierre Airport</a></td>
<td><a href="/wiki/Havre-Saint-Pierre" title="Havre-Saint-Pierre">Havre-Saint-Pierre</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYGW</td>
<td>YGW</td>
<td><a href="/wiki/Kuujjuarapik_Airport" title="Kuujjuarapik Airport">Kuujjuarapik Airport</a></td>
<td><a href="/wiki/Kuujjuarapik" title="Kuujjuarapik">Kuujjuarapik</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYGX</td>
<td>YGX</td>
<td><a href="/wiki/Gillam_Airport" title="Gillam Airport">Gillam Airport</a></td>
<td><a href="/wiki/Gillam,_Manitoba" title="Gillam, Manitoba">Gillam</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYGZ</td>
<td>YGZ</td>
<td><a href="/wiki/Grise_Fiord_Airport" title="Grise Fiord Airport">Grise Fiord Airport</a></td>
<td><a href="/wiki/Grise_Fiord" title="Grise Fiord">Grise Fiord</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYHA</td>
<td>YQC</td>
<td><a href="/wiki/Quaqtaq_Airport" title="Quaqtaq Airport">Quaqtaq Airport</a></td>
<td><a href="/wiki/Quaqtaq" title="Quaqtaq">Quaqtaq</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYHB</td>
<td>YHB</td>
<td><a href="/wiki/Hudson_Bay_Airport" title="Hudson Bay Airport">Hudson Bay Airport</a></td>
<td><a href="/wiki/Hudson_Bay,_Saskatchewan" title="Hudson Bay, Saskatchewan">Hudson Bay</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYHC</td>
<td>CXH</td>
<td><a href="/wiki/Vancouver_Harbour_Flight_Centre" title="Vancouver Harbour Flight Centre">Vancouver Harbour Flight Centre</a> (Vancouver Harbour Water Airport, Vancouver Coal Harbour Seaplane Base)</td>
<td><a href="/wiki/Vancouver" title="Vancouver">Vancouver</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYHD</td>
<td>YHD</td>
<td><a href="/wiki/Dryden_Regional_Airport" title="Dryden Regional Airport">Dryden Regional Airport</a></td>
<td><a href="/wiki/Dryden,_Ontario" title="Dryden, Ontario">Dryden</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYHE</td>
<td>YHE</td>
<td><a href="/wiki/Hope_Aerodrome" title="Hope Aerodrome">Hope Aerodrome</a></td>
<td><a href="/wiki/Hope,_British_Columbia" title="Hope, British Columbia">Hope</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYHF</td>
<td>YHF</td>
<td><a href="/wiki/Hearst_(Ren%C3%A9_Fontaine)_Municipal_Airport" title="Hearst (René Fontaine) Municipal Airport">Hearst (René Fontaine) Municipal Airport</a></td>
<td><a href="/wiki/Hearst,_Ontario" title="Hearst, Ontario">Hearst</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYHH</td>
<td>YNS</td>
<td><a href="/wiki/Nemiscau_Airport" title="Nemiscau Airport">Nemiscau Airport</a></td>
<td><a href="/wiki/Nemaska" title="Nemaska">Nemaska</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYHI</td>
<td>YHI</td>
<td><a href="/wiki/Ulukhaktok/Holman_Airport" title="Ulukhaktok/Holman Airport">Ulukhaktok/Holman Airport</a></td>
<td><a href="/wiki/Ulukhaktok" title="Ulukhaktok">Ulukhaktok</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYHK</td>
<td>YHK</td>
<td><a href="/wiki/Gjoa_Haven_Airport" title="Gjoa Haven Airport">Gjoa Haven Airport</a></td>
<td><a href="/wiki/Gjoa_Haven" title="Gjoa Haven">Gjoa Haven</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYHM</td>
<td>YHM</td>
<td><a href="/wiki/John_C._Munro_Hamilton_International_Airport" title="John C. Munro Hamilton International Airport">John C. Munro Hamilton International Airport</a> (Hamilton Airport)</td>
<td><a href="/wiki/Hamilton,_Ontario" title="Hamilton, Ontario">Hamilton</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYHN</td>
<td>YHN</td>
<td><a href="/wiki/Hornepayne_Municipal_Airport" title="Hornepayne Municipal Airport">Hornepayne Municipal Airport</a></td>
<td><a href="/wiki/Hornepayne" title="Hornepayne">Hornepayne</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYHO</td>
<td>YHO</td>
<td><a href="/wiki/Hopedale_Airport" title="Hopedale Airport">Hopedale Airport</a></td>
<td><a href="/wiki/Hopedale,_Newfoundland_and_Labrador" title="Hopedale, Newfoundland and Labrador">Hopedale</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYHP</td>
<td>YHP</td>
<td><a href="/wiki/Poplar_Hill_Airport" title="Poplar Hill Airport">Poplar Hill Airport</a></td>
<td><a href="/wiki/Poplar_Hill,_Ontario" class="mw-redirect" title="Poplar Hill, Ontario">Poplar Hill</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYHR</td>
<td>YHR</td>
<td><a href="/wiki/Chevery_Airport" title="Chevery Airport">Chevery Airport</a></td>
<td><a href="/wiki/Chevery" title="Chevery">Chevery</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYHS</td>
<td></td>
<td><a href="/wiki/Hanover_Saugeen_Airport" title="Hanover Saugeen Airport">Hanover Saugeen Airport</a></td>
<td><a href="/wiki/Hanover,_Ontario" title="Hanover, Ontario">Hanover</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYHT</td>
<td>YHT</td>
<td><a href="/wiki/Haines_Junction_Airport" title="Haines Junction Airport">Haines Junction Airport</a></td>
<td><a href="/wiki/Haines_Junction" class="mw-redirect" title="Haines Junction">Haines Junction</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CYHU</td>
<td>YHU</td>
<td><a href="/wiki/Montreal_Saint-Hubert_Longueuil_Airport" title="Montreal Saint-Hubert Longueuil Airport">Montreal Saint-Hubert Longueuil Airport</a></td>
<td><a href="/wiki/Longueuil" title="Longueuil">Longueuil</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYHY</td>
<td>YHY</td>
<td><a href="/wiki/Hay_River/Merlyn_Carter_Airport" title="Hay River/Merlyn Carter Airport">Hay River/Merlyn Carter Airport</a></td>
<td><a href="/wiki/Hay_River,_Northwest_Territories" title="Hay River, Northwest Territories">Hay River</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYHZ</td>
<td>YHZ</td>
<td><em><a href="/wiki/Halifax_Stanfield_International_Airport" title="Halifax Stanfield International Airport">Halifax Stanfield International Airport</a></em></td>
<td><a href="/wiki/Halifax,_Nova_Scotia" title="Halifax, Nova Scotia">Halifax</a></td>
<td><a href="/wiki/Nova_Scotia" title="Nova Scotia">NS</a>
</td></tr>
<tr>
<td>CYIB</td>
<td>YIB</td>
<td><a href="/wiki/Atikokan_Municipal_Airport" title="Atikokan Municipal Airport">Atikokan Municipal Airport</a></td>
<td><a href="/wiki/Atikokan" title="Atikokan">Atikokan</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYID</td>
<td>YDG</td>
<td><a href="/wiki/Digby/Annapolis_Regional_Airport" title="Digby/Annapolis Regional Airport">Digby/Annapolis Regional Airport</a></td>
<td><a href="/wiki/Digby,_Nova_Scotia" title="Digby, Nova Scotia">Digby</a></td>
<td><a href="/wiki/Nova_Scotia" title="Nova Scotia">NS</a>
</td></tr>
<tr>
<td>CYIF</td>
<td>YIF</td>
<td><a href="/wiki/Saint-Augustin_Airport" title="Saint-Augustin Airport">Saint-Augustin Airport</a></td>
<td><a href="/wiki/Saint-Augustin,_C%C3%B4te-Nord,_Quebec" title="Saint-Augustin, Côte-Nord, Quebec">Saint-Augustin</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYIK</td>
<td>YIK</td>
<td><a href="/wiki/Ivujivik_Airport" title="Ivujivik Airport">Ivujivik Airport</a></td>
<td><a href="/wiki/Ivujivik" title="Ivujivik">Ivujivik</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYIO</td>
<td>YIO</td>
<td><a href="/wiki/Pond_Inlet_Airport" title="Pond Inlet Airport">Pond Inlet Airport</a></td>
<td><a href="/wiki/Pond_Inlet" title="Pond Inlet">Pond Inlet</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYIV</td>
<td>YIV</td>
<td><a href="/wiki/Island_Lake_Airport" title="Island Lake Airport">Island Lake Airport</a></td>
<td><a href="/wiki/Island_Lake,_Manitoba" title="Island Lake, Manitoba">Island Lake</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYJA</td>
<td></td>
<td><a href="/wiki/Jasper_Airport" title="Jasper Airport">Jasper Airport</a></td>
<td><a href="/wiki/Jasper,_Alberta" title="Jasper, Alberta">Jasper</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYJF</td>
<td>YJF</td>
<td><a href="/wiki/Fort_Liard_Airport" title="Fort Liard Airport">Fort Liard Airport</a></td>
<td><a href="/wiki/Fort_Liard" title="Fort Liard">Fort Liard</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYJM</td>
<td>YJM</td>
<td><a href="/wiki/Fort_St._James_(Perison)_Airport" title="Fort St. James (Perison) Airport">Fort St. James (Perison) Airport</a></td>
<td><a href="/wiki/Fort_St._James" title="Fort St. James">Fort St. James</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYJN</td>
<td>YJN</td>
<td><a href="/wiki/Saint-Jean_Airport" title="Saint-Jean Airport">Saint-Jean Airport</a> (Saint-Jean-sur-Richelieu Airport)</td>
<td><a href="/wiki/Saint-Jean-sur-Richelieu" title="Saint-Jean-sur-Richelieu">Saint-Jean-sur-Richelieu</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYJP</td>
<td></td>
<td><a href="/wiki/Fort_Providence_Airport" title="Fort Providence Airport">Fort Providence Airport</a></td>
<td><a href="/wiki/Fort_Providence" title="Fort Providence">Fort Providence</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYJQ</td>
<td>ZEL</td>
<td><a href="/wiki/Denny_Island_Aerodrome" title="Denny Island Aerodrome">Denny Island Aerodrome</a></td>
<td><a href="/wiki/Bella_Bella,_British_Columbia" title="Bella Bella, British Columbia">Bella Bella</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYJT</td>
<td>YJT</td>
<td><a href="/wiki/Stephenville_International_Airport" title="Stephenville International Airport">Stephenville International Airport</a></td>
<td><a href="/wiki/Stephenville,_Newfoundland_and_Labrador" title="Stephenville, Newfoundland and Labrador">Stephenville</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYKA</td>
<td>YKA</td>
<td><a href="/wiki/Kamloops_Airport" title="Kamloops Airport">Kamloops Airport</a></td>
<td><a href="/wiki/Kamloops" title="Kamloops">Kamloops</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYKC</td>
<td></td>
<td><a href="/wiki/Collins_Bay_Airport" title="Collins Bay Airport">Collins Bay Airport</a></td>
<td><a href="/wiki/Wollaston_Lake" title="Wollaston Lake">Collins Bay</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYKD</td>
<td>LAK</td>
<td><a href="/wiki/Aklavik/Freddie_Carmichael_Airport" title="Aklavik/Freddie Carmichael Airport">Aklavik/Freddie Carmichael Airport</a></td>
<td><a href="/wiki/Aklavik" title="Aklavik">Aklavik</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYKF</td>
<td>YKF</td>
<td><a href="/wiki/Region_of_Waterloo_International_Airport" title="Region of Waterloo International Airport">Region of Waterloo International Airport</a> (Kitchener/Waterloo Regional Airport)</td>
<td><a href="/wiki/Regional_Municipality_of_Waterloo" title="Regional Municipality of Waterloo">Regional Municipality of Waterloo</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYKG</td>
<td></td>
<td><a href="/wiki/Kangiqsujuaq_(Wakeham_Bay)_Airport" title="Kangiqsujuaq (Wakeham Bay) Airport">Kangiqsujuaq (Wakeham Bay) Airport</a></td>
<td><a href="/wiki/Kangiqsujuaq" title="Kangiqsujuaq">Kangiqsujuaq</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYKJ</td>
<td>YKJ</td>
<td><a href="/wiki/Key_Lake_Airport" title="Key Lake Airport">Key Lake Airport</a></td>
<td><a href="/wiki/Key_Lake_mine" title="Key Lake mine">Key Lake mine</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYKL</td>
<td>YKL</td>
<td><a href="/wiki/Schefferville_Airport" title="Schefferville Airport">Schefferville Airport</a></td>
<td><a href="/wiki/Schefferville" title="Schefferville">Schefferville</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYKM</td>
<td>YKD</td>
<td><a href="/wiki/Kincardine_Municipal_Airport" title="Kincardine Municipal Airport">Kincardine Municipal Airport</a></td>
<td><a href="/wiki/Kincardine,_Ontario" title="Kincardine, Ontario">Kincardine</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYKO</td>
<td>AKV</td>
<td><a href="/wiki/Akulivik_Airport" title="Akulivik Airport">Akulivik Airport</a></td>
<td><a href="/wiki/Akulivik" title="Akulivik">Akulivik</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYKP</td>
<td>YOG</td>
<td><a href="/wiki/Ogoki_Post_Airport" title="Ogoki Post Airport">Ogoki Post Airport</a></td>
<td><a href="/wiki/Marten_Falls_First_Nation" title="Marten Falls First Nation">Marten Falls First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYKQ</td>
<td>YKQ</td>
<td><a href="/wiki/Waskaganish_Airport" title="Waskaganish Airport">Waskaganish Airport</a></td>
<td><a href="/wiki/Waskaganish" title="Waskaganish">Waskaganish</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYKX</td>
<td>YKX</td>
<td><a href="/wiki/Kirkland_Lake_Airport" title="Kirkland Lake Airport">Kirkland Lake Airport</a></td>
<td><a href="/wiki/Kirkland_Lake" title="Kirkland Lake">Kirkland Lake</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYKY</td>
<td>YKY</td>
<td><a href="/wiki/Kindersley_Regional_Airport" title="Kindersley Regional Airport">Kindersley Regional Airport</a></td>
<td><a href="/wiki/Kindersley" title="Kindersley">Kindersley</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYKZ</td>
<td>YKZ</td>
<td><a href="/wiki/Buttonville_Municipal_Airport" title="Buttonville Municipal Airport">Buttonville Municipal Airport</a> (Toronto/Buttonville Municipal Airport)</td>
<td><a href="/wiki/Buttonville,_Ontario" title="Buttonville, Ontario">Buttonville</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYLA</td>
<td>YPJ</td>
<td><a href="/wiki/Aupaluk_Airport" title="Aupaluk Airport">Aupaluk Airport</a></td>
<td><a href="/wiki/Aupaluk" title="Aupaluk">Aupaluk</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYLB</td>
<td></td>
<td><a href="/wiki/Lac_La_Biche_Airport" title="Lac La Biche Airport">Lac La Biche Airport</a></td>
<td><a href="/wiki/Lac_La_Biche,_Alberta" title="Lac La Biche, Alberta">Lac La Biche</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYLC</td>
<td>YLC</td>
<td><a href="/wiki/Kimmirut_Airport" title="Kimmirut Airport">Kimmirut Airport</a></td>
<td><a href="/wiki/Kimmirut" title="Kimmirut">Kimmirut</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYLD</td>
<td>YLD</td>
<td><a href="/wiki/Chapleau_Airport" title="Chapleau Airport">Chapleau Airport</a></td>
<td><a href="/wiki/Chapleau,_Ontario" title="Chapleau, Ontario">Chapleau</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYLH</td>
<td>YLH</td>
<td><a href="/wiki/Lansdowne_House_Airport" title="Lansdowne House Airport">Lansdowne House Airport</a></td>
<td><a href="/wiki/Neskantaga_First_Nation" title="Neskantaga First Nation">Neskantaga First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYLI</td>
<td></td>
<td><a href="/wiki/Lillooet_Airport" title="Lillooet Airport">Lillooet Airport</a></td>
<td><a href="/wiki/Lillooet" title="Lillooet">Lillooet</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYLJ</td>
<td>YLJ</td>
<td><a href="/wiki/Meadow_Lake_Airport_(Saskatchewan)" title="Meadow Lake Airport (Saskatchewan)">Meadow Lake Airport</a></td>
<td><a href="/wiki/Meadow_Lake,_Saskatchewan" title="Meadow Lake, Saskatchewan">Meadow Lake</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYLK</td>
<td></td>
<td><a href="/wiki/Lutselk%27e_Airport" title="Lutselk'e Airport">Lutselk'e Airport</a></td>
<td><a href="/wiki/%C5%81utselk%27e" title="Łutselk'e">Łutselk'e</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYLL</td>
<td>YLL</td>
<td><a href="/wiki/Lloydminster_Airport" title="Lloydminster Airport">Lloydminster Airport</a></td>
<td><a href="/wiki/Lloydminster" title="Lloydminster">Lloydminster</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYLQ</td>
<td>YLQ</td>
<td><a href="/wiki/La_Tuque_Airport" title="La Tuque Airport">La Tuque Airport</a></td>
<td><a href="/wiki/La_Tuque,_Quebec" title="La Tuque, Quebec">La Tuque</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYLR</td>
<td>YLR</td>
<td><a href="/wiki/Leaf_Rapids_Airport" title="Leaf Rapids Airport">Leaf Rapids Airport</a></td>
<td><a href="/wiki/Leaf_Rapids" title="Leaf Rapids">Leaf Rapids</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYLS</td>
<td></td>
<td><a href="/wiki/Lake_Simcoe_Regional_Airport" title="Lake Simcoe Regional Airport">Lake Simcoe Regional Airport</a> (Barrie-Orillia (Lake Simcoe Regional) Airport)</td>
<td><a href="/wiki/Barrie" title="Barrie">Barrie</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYLT</td>
<td>YLT</td>
<td><a href="/wiki/Alert_Airport" title="Alert Airport">Alert Airport</a></td>
<td><a href="/wiki/Alert,_Nunavut" title="Alert, Nunavut">Alert</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYLU</td>
<td>XGR</td>
<td><a href="/wiki/Kangiqsualujjuaq_(Georges_River)_Airport" title="Kangiqsualujjuaq (Georges River) Airport">Kangiqsualujjuaq (Georges River) Airport</a></td>
<td><a href="/wiki/Kangiqsualujjuaq" title="Kangiqsualujjuaq">Kangiqsualujjuaq</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYLW</td>
<td>YLW</td>
<td><em><a href="/wiki/Kelowna_International_Airport" title="Kelowna International Airport">Kelowna International Airport</a></em></td>
<td><a href="/wiki/Kelowna" title="Kelowna">Kelowna</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYMA</td>
<td>YMA</td>
<td><a href="/wiki/Mayo_Airport" title="Mayo Airport">Mayo Airport</a></td>
<td><a href="/wiki/Mayo,_Yukon" title="Mayo, Yukon">Mayo</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CYME</td>
<td>YME</td>
<td><a href="/wiki/Matane/Russell-Burnett_Airport" title="Matane/Russell-Burnett Airport">Matane/Russell-Burnett Airport</a></td>
<td><a href="/wiki/Matane" title="Matane">Matane</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYMG</td>
<td>YMG</td>
<td><a href="/wiki/Manitouwadge_Airport" title="Manitouwadge Airport">Manitouwadge Airport</a></td>
<td><a href="/wiki/Manitouwadge" title="Manitouwadge">Manitouwadge</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYMH</td>
<td>YMH</td>
<td><a href="/wiki/Mary%27s_Harbour_Airport" title="Mary's Harbour Airport">Mary's Harbour Airport</a></td>
<td><a href="/wiki/Mary%27s_Harbour" title="Mary's Harbour">Mary's Harbour</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYMJ</td>
<td>YMJ</td>
<td><a href="/wiki/CFB_Moose_Jaw" title="CFB Moose Jaw">CFB Moose Jaw</a> (Moose Jaw/Air Vice Marshal C.M. McEwen Airport)</td>
<td><a href="/wiki/Moose_Jaw" title="Moose Jaw">Moose Jaw</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYML</td>
<td>YML</td>
<td><a href="/wiki/Charlevoix_Airport" title="Charlevoix Airport">Charlevoix Airport</a></td>
<td><a href="/wiki/Charlevoix" title="Charlevoix">Charlevoix</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYMM</td>
<td>YMM</td>
<td><a href="/wiki/Fort_McMurray_International_Airport" title="Fort McMurray International Airport">Fort McMurray International Airport</a></td>
<td><a href="/wiki/Fort_McMurray" title="Fort McMurray">Fort McMurray</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYMO</td>
<td>YMO</td>
<td><a href="/wiki/Moosonee_Airport" title="Moosonee Airport">Moosonee Airport</a></td>
<td><a href="/wiki/Moosonee" title="Moosonee">Moosonee</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYMT</td>
<td>YMT</td>
<td><a href="/wiki/Chibougamau/Chapais_Airport" title="Chibougamau/Chapais Airport">Chibougamau/Chapais Airport</a></td>
<td><a href="/wiki/Chibougamau" title="Chibougamau">Chibougamau</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYMU</td>
<td>YUD</td>
<td><a href="/wiki/Umiujaq_Airport" title="Umiujaq Airport">Umiujaq Airport</a></td>
<td><a href="/wiki/Umiujaq" title="Umiujaq">Umiujaq</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYMW</td>
<td>YMW</td>
<td><a href="/wiki/Maniwaki_Airport" title="Maniwaki Airport">Maniwaki Airport</a></td>
<td><a href="/wiki/Maniwaki" title="Maniwaki">Maniwaki</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYMX</td>
<td>YMX</td>
<td><em><a href="/wiki/Montr%C3%A9al%E2%80%93Mirabel_International_Airport" title="Montréal–Mirabel International Airport">Montréal–Mirabel International Airport</a></em></td>
<td><a href="/wiki/Montreal" title="Montreal">Montreal</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYN6</td>
<td></td>
<td><a href="/wiki/Gravenhurst/Muskoka_Bay_Water_Aerodrome" title="Gravenhurst/Muskoka Bay Water Aerodrome">Gravenhurst/Muskoka Bay Water Aerodrome</a></td>
<td><a href="/wiki/Gravenhurst,_Ontario" title="Gravenhurst, Ontario">Gravenhurst</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYNA</td>
<td>YNA</td>
<td><a href="/wiki/Natashquan_Airport" title="Natashquan Airport">Natashquan Airport</a></td>
<td><a href="/wiki/Natashquan_(municipality)" class="mw-redirect" title="Natashquan (municipality)">Natashquan</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYNC</td>
<td>YNC</td>
<td><a href="/wiki/Wemindji_Airport" title="Wemindji Airport">Wemindji Airport</a></td>
<td><a href="/wiki/Wemindji" title="Wemindji">Wemindji</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYND</td>
<td>YND</td>
<td><a href="/wiki/Gatineau-Ottawa_Executive_Airport" title="Gatineau-Ottawa Executive Airport">Gatineau-Ottawa Executive Airport</a> (Ottawa/Gatineau Airport)</td>
<td><a href="/wiki/Gatineau" title="Gatineau">Gatineau</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYNE</td>
<td>YNE</td>
<td><a href="/wiki/Norway_House_Airport" title="Norway House Airport">Norway House Airport</a></td>
<td><a href="/wiki/Norway_House" title="Norway House">Norway House</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYNH</td>
<td>YNH</td>
<td><a href="/wiki/Hudson%27s_Hope_Airport" title="Hudson's Hope Airport">Hudson's Hope Airport</a></td>
<td><a href="/wiki/Hudson%27s_Hope" title="Hudson's Hope">Hudson's Hope</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYNJ</td>
<td>YNJ</td>
<td><a href="/wiki/Langley_Regional_Airport" title="Langley Regional Airport">Langley Regional Airport</a></td>
<td><a href="/wiki/Langley,_British_Columbia_(district_municipality)" title="Langley, British Columbia (district municipality)">Langley</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYNL</td>
<td>YNL</td>
<td><a href="/wiki/Points_North_Landing_Airport" title="Points North Landing Airport">Points North Landing Airport</a></td>
<td><a href="/wiki/Points_North_Landing" title="Points North Landing">Points North Landing</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYNM</td>
<td>YNM</td>
<td><a href="/wiki/Matagami_Airport" title="Matagami Airport">Matagami Airport</a></td>
<td><a href="/wiki/Matagami" title="Matagami">Matagami</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYNN</td>
<td></td>
<td><a href="/wiki/Nejanilini_Lake_Airport" title="Nejanilini Lake Airport">Nejanilini Lake Airport</a></td>
<td><a href="/w/index.php?title=Nejanilini_Lake&amp;action=edit&amp;redlink=1" class="new" title="Nejanilini Lake (page does not exist)">Nejanilini Lake</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYNR</td>
<td></td>
<td><a href="/wiki/Fort_MacKay/Horizon_Airport" title="Fort MacKay/Horizon Airport">Fort MacKay/Horizon Airport</a></td>
<td><a href="/wiki/Fort_McKay" title="Fort McKay">Fort McKay</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYOA</td>
<td>YOA</td>
<td><a href="/wiki/Ekati_Airport" title="Ekati Airport">Ekati Airport</a></td>
<td><a href="/wiki/Ekati_Diamond_Mine" title="Ekati Diamond Mine">Ekati Diamond Mine</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYOC</td>
<td>YOC</td>
<td><a href="/wiki/Old_Crow_Airport" title="Old Crow Airport">Old Crow Airport</a></td>
<td><a href="/wiki/Old_Crow,_Yukon" title="Old Crow, Yukon">Old Crow</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CYOD</td>
<td>YOD</td>
<td><a href="/wiki/CFB_Cold_Lake" title="CFB Cold Lake">CFB Cold Lake</a> (Cold Lake/Group Captain R.W. McNair Airport)</td>
<td><a href="/wiki/Cold_Lake,_Alberta" title="Cold Lake, Alberta">Cold Lake</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYOH</td>
<td>YOH</td>
<td><a href="/wiki/Oxford_House_Airport" title="Oxford House Airport">Oxford House Airport</a></td>
<td><a href="/wiki/Oxford_House,_Manitoba" title="Oxford House, Manitoba">Oxford House</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYOJ</td>
<td>YOJ</td>
<td><a href="/wiki/High_Level_Airport" title="High Level Airport">High Level Airport</a></td>
<td><a href="/wiki/High_Level" title="High Level">High Level</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYOO</td>
<td>YOO</td>
<td><a href="/wiki/Oshawa_Executive_Airport" title="Oshawa Executive Airport">Oshawa Executive Airport</a> (Toronto/Oshawa Executive Airport)</td>
<td><a href="/wiki/Oshawa" title="Oshawa">Oshawa</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYOP</td>
<td></td>
<td><a href="/wiki/Rainbow_Lake_Airport" title="Rainbow Lake Airport">Rainbow Lake Airport</a></td>
<td><a href="/wiki/Rainbow_Lake,_Alberta" title="Rainbow Lake, Alberta">Rainbow Lake</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYOS</td>
<td>YOS</td>
<td><a href="/wiki/Owen_Sound_Billy_Bishop_Regional_Airport" title="Owen Sound Billy Bishop Regional Airport">Owen Sound Billy Bishop Regional Airport</a> (Billy Bishop Regional Airport)</td>
<td><a href="/wiki/Owen_Sound" title="Owen Sound">Owen Sound</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYOW</td>
<td>YOW</td>
<td><em><a href="/wiki/Ottawa_Macdonald%E2%80%93Cartier_International_Airport" title="Ottawa Macdonald–Cartier International Airport">Ottawa Macdonald–Cartier International Airport</a></em> (Macdonald-Cartier International Airport)</td>
<td><a href="/wiki/Ottawa" title="Ottawa">Ottawa</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYOY</td>
<td>YOY</td>
<td><a href="/wiki/CFB_Valcartier" title="CFB Valcartier">CFB Valcartier</a> (Valcartier (W/C J.H.L. (Joe) Lecomte) Heliport)</td>
<td><a href="/wiki/Saint-Gabriel-de-Valcartier" title="Saint-Gabriel-de-Valcartier">Saint-Gabriel-de-Valcartier</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYPA</td>
<td>YPA</td>
<td><a href="/wiki/Prince_Albert_(Glass_Field)_Airport" title="Prince Albert (Glass Field) Airport">Prince Albert (Glass Field) Airport</a></td>
<td><a href="/wiki/Prince_Albert,_Saskatchewan" title="Prince Albert, Saskatchewan">Prince Albert</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYPC</td>
<td>YPC</td>
<td><a href="/wiki/Paulatuk_(Nora_Aliqatchialuk_Ruben)_Airport" title="Paulatuk (Nora Aliqatchialuk Ruben) Airport">Paulatuk (Nora Aliqatchialuk Ruben) Airport</a></td>
<td><a href="/wiki/Paulatuk" title="Paulatuk">Paulatuk</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYPD</td>
<td>YPS</td>
<td><a href="/wiki/Allan_J._MacEachen_Port_Hawkesbury_Airport" title="Allan J. MacEachen Port Hawkesbury Airport">Allan J. MacEachen Port Hawkesbury Airport</a> (Port Hawkesbury Airport)</td>
<td><a href="/wiki/Port_Hawkesbury" title="Port Hawkesbury">Port Hawkesbury</a></td>
<td><a href="/wiki/Nova_Scotia" title="Nova Scotia">NS</a>
</td></tr>
<tr>
<td>CYPE</td>
<td>YPE</td>
<td><a href="/wiki/Peace_River_Airport" title="Peace River Airport">Peace River Airport</a></td>
<td><a href="/wiki/Peace_River,_Alberta" title="Peace River, Alberta">Peace River</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYPG</td>
<td>YPG</td>
<td><a href="/wiki/Portage_la_Prairie/Southport_Airport" title="Portage la Prairie/Southport Airport">Portage la Prairie/Southport Airport</a></td>
<td><a href="/wiki/Portage_la_Prairie" title="Portage la Prairie">Portage la Prairie</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYPH</td>
<td>YPH</td>
<td><a href="/wiki/Inukjuak_Airport" title="Inukjuak Airport">Inukjuak Airport</a></td>
<td><a href="/wiki/Inukjuak" title="Inukjuak">Inukjuak</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYPK</td>
<td>YPK</td>
<td><a href="/wiki/Pitt_Meadows_Regional_Airport" title="Pitt Meadows Regional Airport">Pitt Meadows Regional Airport</a></td>
<td><a href="/wiki/Pitt_Meadows" title="Pitt Meadows">Pitt Meadows</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYPL</td>
<td>YPL</td>
<td><a href="/wiki/Pickle_Lake_Airport" title="Pickle Lake Airport">Pickle Lake Airport</a></td>
<td><a href="/wiki/Pickle_Lake" title="Pickle Lake">Pickle Lake</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYPM</td>
<td>YPM</td>
<td><a href="/wiki/Pikangikum_Airport" title="Pikangikum Airport">Pikangikum Airport</a></td>
<td><a href="/wiki/Pikangikum_First_Nation" title="Pikangikum First Nation">Pikangikum First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYPN</td>
<td>YPN</td>
<td><a href="/wiki/Port-Menier_Airport" title="Port-Menier Airport">Port-Menier Airport</a></td>
<td><a href="/wiki/Port-Menier,_Quebec" title="Port-Menier, Quebec">Port-Menier</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYPO</td>
<td>YPO</td>
<td><a href="/wiki/Peawanuck_Airport" title="Peawanuck Airport">Peawanuck Airport</a></td>
<td><a href="/wiki/Peawanuck" title="Peawanuck">Peawanuck</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYPP</td>
<td></td>
<td><a href="/wiki/Parent_Airport" title="Parent Airport">Parent Airport</a></td>
<td><a href="/wiki/Parent,_Quebec" title="Parent, Quebec">Parent</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYPQ</td>
<td>YPQ</td>
<td><a href="/wiki/Peterborough_Airport" title="Peterborough Airport">Peterborough Airport</a></td>
<td><a href="/wiki/Peterborough,_Ontario" title="Peterborough, Ontario">Peterborough</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYPR</td>
<td>YPR</td>
<td><a href="/wiki/Prince_Rupert_Airport" title="Prince Rupert Airport">Prince Rupert Airport</a></td>
<td><a href="/wiki/Prince_Rupert,_British_Columbia" title="Prince Rupert, British Columbia">Prince Rupert</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYPS</td>
<td></td>
<td><a href="/wiki/Pemberton_Regional_Airport" title="Pemberton Regional Airport">Pemberton Regional Airport</a></td>
<td><a href="/wiki/Pemberton,_British_Columbia" title="Pemberton, British Columbia">Pemberton</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYPT</td>
<td></td>
<td><a href="/wiki/Pelee_Island_Airport" title="Pelee Island Airport">Pelee Island Airport</a></td>
<td><a href="/wiki/Pelee,_Ontario" title="Pelee, Ontario">Pelee</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYPU</td>
<td>YPU</td>
<td><a href="/wiki/Puntzi_Mountain_Airport" title="Puntzi Mountain Airport">Puntzi Mountain Airport</a></td>
<td><a href="/w/index.php?title=Puntzi_Mountain,_British_Columbia&amp;action=edit&amp;redlink=1" class="new" title="Puntzi Mountain, British Columbia (page does not exist)">Puntzi Mountain</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYPW</td>
<td>YPW</td>
<td><a href="/wiki/Powell_River_Airport" title="Powell River Airport">Powell River Airport</a></td>
<td><a href="/wiki/Powell_River,_British_Columbia" title="Powell River, British Columbia">Powell River</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYPX</td>
<td></td>
<td><a href="/wiki/Puvirnituq_Airport" title="Puvirnituq Airport">Puvirnituq Airport</a></td>
<td><a href="/wiki/Puvirnituq" title="Puvirnituq">Puvirnituq</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYPY</td>
<td>YPY</td>
<td><a href="/wiki/Fort_Chipewyan_Airport" title="Fort Chipewyan Airport">Fort Chipewyan Airport</a></td>
<td><a href="/wiki/Fort_Chipewyan" title="Fort Chipewyan">Fort Chipewyan</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYPZ</td>
<td>YPZ</td>
<td><a href="/wiki/Burns_Lake_Airport" title="Burns Lake Airport">Burns Lake Airport</a></td>
<td><a href="/wiki/Burns_Lake" title="Burns Lake">Burns Lake</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYQA</td>
<td>YQA</td>
<td><a href="/wiki/Muskoka_Airport" title="Muskoka Airport">Muskoka Airport</a></td>
<td><a href="/wiki/District_Municipality_of_Muskoka" title="District Municipality of Muskoka">District Municipality of Muskoka</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYQB</td>
<td>YQB</td>
<td><em><a href="/wiki/Qu%C3%A9bec_City_Jean_Lesage_International_Airport" title="Québec City Jean Lesage International Airport">Québec City Jean Lesage International Airport</a></em></td>
<td><a href="/wiki/Quebec_City" title="Quebec City">Quebec City</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYQD</td>
<td>YQD</td>
<td><a href="/wiki/The_Pas_Airport" title="The Pas Airport">The Pas Airport</a></td>
<td><a href="/wiki/The_Pas" title="The Pas">The Pas</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYQF</td>
<td>YQF</td>
<td><a href="/wiki/Red_Deer_Regional_Airport" title="Red Deer Regional Airport">Red Deer Regional Airport</a></td>
<td><a href="/wiki/Red_Deer,_Alberta" title="Red Deer, Alberta">Red Deer</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYQG</td>
<td>YQG</td>
<td><a href="/wiki/Windsor_International_Airport" title="Windsor International Airport">Windsor International Airport</a></td>
<td><a href="/wiki/Windsor,_Ontario" title="Windsor, Ontario">Windsor</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYQH</td>
<td>YQH</td>
<td><a href="/wiki/Watson_Lake_Airport" title="Watson Lake Airport">Watson Lake Airport</a></td>
<td><a href="/wiki/Watson_Lake,_Yukon" title="Watson Lake, Yukon">Watson Lake</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CYQI</td>
<td>YQI</td>
<td><a href="/wiki/Yarmouth_Airport" title="Yarmouth Airport">Yarmouth Airport</a></td>
<td><a href="/wiki/Yarmouth,_Nova_Scotia" title="Yarmouth, Nova Scotia">Yarmouth</a></td>
<td><a href="/wiki/Nova_Scotia" title="Nova Scotia">NS</a>
</td></tr>
<tr>
<td>CYQK</td>
<td>YQK</td>
<td><a href="/wiki/Kenora_Airport" title="Kenora Airport">Kenora Airport</a></td>
<td><a href="/wiki/Kenora" title="Kenora">Kenora</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYQL</td>
<td>YQL</td>
<td><a href="/wiki/Lethbridge_Airport" title="Lethbridge Airport">Lethbridge Airport</a></td>
<td><a href="/wiki/Lethbridge" title="Lethbridge">Lethbridge</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYQM</td>
<td>YQM</td>
<td><em><a href="/wiki/Greater_Moncton_Rom%C3%A9o_LeBlanc_International_Airport" title="Greater Moncton Roméo LeBlanc International Airport">Greater Moncton Roméo LeBlanc International Airport</a></em> (Moncton/Greater Moncton Roméo LeBlanc International Airport)</td>
<td><a href="/wiki/Moncton" title="Moncton">Moncton</a></td>
<td><a href="/wiki/New_Brunswick" title="New Brunswick">NB</a>
</td></tr>
<tr>
<td>CYQN</td>
<td>YQN</td>
<td><a href="/wiki/Nakina_Airport" title="Nakina Airport">Nakina Airport</a></td>
<td><a href="/wiki/Greenstone,_Ontario" title="Greenstone, Ontario">Nakina</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYQQ</td>
<td>YQQ</td>
<td><a href="/wiki/CFB_Comox" title="CFB Comox">CFB Comox</a> (Comox Airport)</td>
<td><a href="/wiki/Comox,_British_Columbia" title="Comox, British Columbia">Comox</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYQR</td>
<td>YQR</td>
<td><em><a href="/wiki/Regina_International_Airport" title="Regina International Airport">Regina International Airport</a></em></td>
<td><a href="/wiki/Regina,_Saskatchewan" title="Regina, Saskatchewan">Regina</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYQS</td>
<td>YQS</td>
<td><a href="/wiki/St._Thomas_Municipal_Airport_(Ontario)" title="St. Thomas Municipal Airport (Ontario)">St. Thomas Municipal Airport</a></td>
<td><a href="/wiki/St._Thomas,_Ontario" title="St. Thomas, Ontario">St. Thomas</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYQT</td>
<td>YQT</td>
<td><a href="/wiki/Thunder_Bay_International_Airport" title="Thunder Bay International Airport">Thunder Bay International Airport</a></td>
<td><a href="/wiki/Thunder_Bay" title="Thunder Bay">Thunder Bay</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYQU</td>
<td>YQU</td>
<td><a href="/wiki/Grande_Prairie_Airport" title="Grande Prairie Airport">Grande Prairie Airport</a></td>
<td><a href="/wiki/Grande_Prairie" title="Grande Prairie">Grande Prairie</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYQV</td>
<td>YQV</td>
<td><a href="/wiki/Yorkton_Municipal_Airport" title="Yorkton Municipal Airport">Yorkton Municipal Airport</a></td>
<td><a href="/wiki/Yorkton" title="Yorkton">Yorkton</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYQW</td>
<td>YQW</td>
<td><a href="/wiki/North_Battleford_Airport" title="North Battleford Airport">North Battleford Airport</a></td>
<td><a href="/wiki/North_Battleford" title="North Battleford">North Battleford</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYQX</td>
<td>YQX</td>
<td><em><a href="/wiki/Gander_International_Airport" title="Gander International Airport">Gander International Airport</a></em></td>
<td><a href="/wiki/Gander,_Newfoundland_and_Labrador" title="Gander, Newfoundland and Labrador">Gander</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYQY</td>
<td>YQY</td>
<td><a href="/wiki/JA_Douglas_McCurdy_Sydney_Airport" title="JA Douglas McCurdy Sydney Airport">JA Douglas McCurdy Sydney Airport</a> (Sydney/J.A. Douglas McCurdy Airport)</td>
<td><a href="/wiki/Sydney,_Nova_Scotia" title="Sydney, Nova Scotia">Sydney</a></td>
<td><a href="/wiki/Nova_Scotia" title="Nova Scotia">NS</a>
</td></tr>
<tr>
<td>CYQZ</td>
<td>YQZ</td>
<td><a href="/wiki/Quesnel_Airport" title="Quesnel Airport">Quesnel Airport</a></td>
<td><a href="/wiki/Quesnel,_British_Columbia" title="Quesnel, British Columbia">Quesnel</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYRA</td>
<td>YRA</td>
<td><a href="/wiki/Gam%C3%A8t%C3%AC/Rae_Lakes_Airport" title="Gamètì/Rae Lakes Airport">Gamètì/Rae Lakes Airport</a></td>
<td><a href="/wiki/Gam%C3%A8ti" title="Gamèti">Gamèti</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYRB</td>
<td>YRB</td>
<td><a href="/wiki/Resolute_Bay_Airport" title="Resolute Bay Airport">Resolute Bay Airport</a></td>
<td><a href="/wiki/Resolute,_Nunavut" title="Resolute, Nunavut">Resolute</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYRC</td>
<td></td>
<td><a href="/wiki/Chicoutimi/Saint-Honor%C3%A9_Aerodrome" title="Chicoutimi/Saint-Honoré Aerodrome">Chicoutimi/Saint-Honoré Aerodrome</a></td>
<td><a href="/wiki/Chicoutimi" title="Chicoutimi">Chicoutimi</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYRI</td>
<td>YRI</td>
<td><a href="/wiki/Rivi%C3%A8re-du-Loup_Airport" title="Rivière-du-Loup Airport">Rivière-du-Loup Airport</a></td>
<td><a href="/wiki/Rivi%C3%A8re-du-Loup" title="Rivière-du-Loup">Rivière-du-Loup</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYRJ</td>
<td>YRJ</td>
<td><a href="/wiki/Roberval_Airport" title="Roberval Airport">Roberval Airport</a></td>
<td><a href="/wiki/Roberval,_Quebec" title="Roberval, Quebec">Roberval</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYRL</td>
<td>YRL</td>
<td><a href="/wiki/Red_Lake_Airport" title="Red Lake Airport">Red Lake Airport</a></td>
<td><a href="/wiki/Red_Lake,_Ontario" title="Red Lake, Ontario">Red Lake</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYRM</td>
<td>YRM</td>
<td><a href="/wiki/Rocky_Mountain_House_Airport" title="Rocky Mountain House Airport">Rocky Mountain House Airport</a></td>
<td><a href="/wiki/Rocky_Mountain_House" title="Rocky Mountain House">Rocky Mountain House</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYRO</td>
<td>YRO</td>
<td><a href="/wiki/Ottawa/Rockcliffe_Airport" title="Ottawa/Rockcliffe Airport">Ottawa/Rockcliffe Airport</a> (Rockcliffe Airport)</td>
<td><a href="/wiki/Ottawa" title="Ottawa">Ottawa</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYRP</td>
<td>YRP</td>
<td><a href="/wiki/Carp_Airport" title="Carp Airport">Carp Airport</a> (Ottawa/Carp Airport)</td>
<td><a href="/wiki/Carp,_Ontario" title="Carp, Ontario">Carp</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYRQ</td>
<td>YRQ</td>
<td><a href="/wiki/Trois-Rivi%C3%A8res_Airport" title="Trois-Rivières Airport">Trois-Rivières Airport</a></td>
<td><a href="/wiki/Trois-Rivi%C3%A8res" title="Trois-Rivières">Trois-Rivières</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYRS</td>
<td>YRS</td>
<td><a href="/wiki/Red_Sucker_Lake_Airport" title="Red Sucker Lake Airport">Red Sucker Lake Airport</a></td>
<td><a href="/wiki/Red_Sucker_Lake,_Manitoba" title="Red Sucker Lake, Manitoba">Red Sucker Lake</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYRT</td>
<td>YRT</td>
<td><a href="/wiki/Rankin_Inlet_Airport" title="Rankin Inlet Airport">Rankin Inlet Airport</a></td>
<td><a href="/wiki/Rankin_Inlet" title="Rankin Inlet">Rankin Inlet</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYRV</td>
<td>YRV</td>
<td><a href="/wiki/Revelstoke_Airport" title="Revelstoke Airport">Revelstoke Airport</a></td>
<td><a href="/wiki/Revelstoke,_British_Columbia" title="Revelstoke, British Columbia">Revelstoke</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYSA</td>
<td></td>
<td><a href="/wiki/Stratford_Municipal_Airport" title="Stratford Municipal Airport">Stratford Municipal Airport</a></td>
<td><a href="/wiki/Stratford,_Ontario" title="Stratford, Ontario">Stratford</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYSB</td>
<td>YSB</td>
<td><a href="/wiki/Sudbury_Airport" title="Sudbury Airport">Sudbury Airport</a> (Greater Sudbury Airport)</td>
<td><a href="/wiki/Greater_Sudbury" title="Greater Sudbury">Greater Sudbury</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYSC</td>
<td>YSC</td>
<td><a href="/wiki/Sherbrooke_Airport" title="Sherbrooke Airport">Sherbrooke Airport</a></td>
<td><a href="/wiki/Sherbrooke" title="Sherbrooke">Sherbrooke</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYSD</td>
<td>YSD</td>
<td><a href="/wiki/CFB_Suffield" title="CFB Suffield">CFB Suffield</a> (Suffield Heliport)</td>
<td><a href="/wiki/Suffield,_Alberta" title="Suffield, Alberta">Suffield</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYSE</td>
<td>YSE</td>
<td><a href="/wiki/Squamish_Airport" title="Squamish Airport">Squamish Airport</a></td>
<td><a href="/wiki/Squamish,_British_Columbia" title="Squamish, British Columbia">Squamish</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYSF</td>
<td>YSF</td>
<td><a href="/wiki/Stony_Rapids_Airport" title="Stony Rapids Airport">Stony Rapids Airport</a></td>
<td><a href="/wiki/Stony_Rapids" title="Stony Rapids">Stony Rapids</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYSG</td>
<td></td>
<td><a href="/wiki/Saint-Georges_Aerodrome" title="Saint-Georges Aerodrome">Saint-Georges Aerodrome</a></td>
<td><a href="/wiki/Saint-Georges,_Quebec" title="Saint-Georges, Quebec">Saint-Georges</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYSH</td>
<td>YSH</td>
<td><a href="/wiki/Smiths_Falls-Montague_Airport" title="Smiths Falls-Montague Airport">Smiths Falls-Montague Airport</a> (Smiths Falls-Montague (Russ Beach) Airport)</td>
<td><a href="/wiki/Smiths_Falls" title="Smiths Falls">Smiths Falls</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYSJ</td>
<td>YSJ</td>
<td><em><a href="/wiki/Saint_John_Airport" title="Saint John Airport">Saint John Airport</a></em></td>
<td><a href="/wiki/Saint_John,_New_Brunswick" title="Saint John, New Brunswick">Saint John</a></td>
<td><a href="/wiki/New_Brunswick" title="New Brunswick">NB</a>
</td></tr>
<tr>
<td>CYSK</td>
<td>YSK</td>
<td><a href="/wiki/Sanikiluaq_Airport" title="Sanikiluaq Airport">Sanikiluaq Airport</a></td>
<td><a href="/wiki/Sanikiluaq" title="Sanikiluaq">Sanikiluaq</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYSL</td>
<td>YSL</td>
<td><a href="/wiki/Saint-L%C3%A9onard_Aerodrome" title="Saint-Léonard Aerodrome">Saint-Léonard Aerodrome</a></td>
<td><a href="/wiki/Saint-L%C3%A9onard,_New_Brunswick" title="Saint-Léonard, New Brunswick">Saint-Léonard</a></td>
<td><a href="/wiki/New_Brunswick" title="New Brunswick">NB</a>
</td></tr>
<tr>
<td>CYSM</td>
<td>YSM</td>
<td><a href="/wiki/Fort_Smith_Airport" title="Fort Smith Airport">Fort Smith Airport</a></td>
<td><a href="/wiki/Fort_Smith,_Northwest_Territories" title="Fort Smith, Northwest Territories">Fort Smith</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYSN</td>
<td>YCM</td>
<td><a href="/wiki/St._Catharines/Niagara_District_Airport" title="St. Catharines/Niagara District Airport">St. Catharines/Niagara District Airport</a></td>
<td><a href="/wiki/St._Catharines" title="St. Catharines">St. Catharines</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYSP</td>
<td>YSP</td>
<td><a href="/wiki/Marathon_Aerodrome" title="Marathon Aerodrome">Marathon Aerodrome</a></td>
<td><a href="/wiki/Marathon,_Ontario" title="Marathon, Ontario">Marathon</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYSQ</td>
<td></td>
<td><a href="/wiki/Atlin_Airport" title="Atlin Airport">Atlin Airport</a></td>
<td><a href="/wiki/Atlin,_British_Columbia" title="Atlin, British Columbia">Atlin</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYST</td>
<td>YST</td>
<td><a href="/wiki/St._Theresa_Point_Airport" title="St. Theresa Point Airport">St. Theresa Point Airport</a></td>
<td><a href="/wiki/St._Theresa_Point_First_Nation" title="St. Theresa Point First Nation">St. Theresa Point First Nation</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYSU</td>
<td>YSU</td>
<td><a href="/wiki/Summerside_Airport" title="Summerside Airport">Summerside Airport</a></td>
<td><a href="/wiki/Summerside,_Prince_Edward_Island" title="Summerside, Prince Edward Island">Summerside</a></td>
<td><a href="/wiki/Prince_Edward_Island" title="Prince Edward Island">PE</a>
</td></tr>
<tr>
<td>CYSW</td>
<td></td>
<td><a href="/wiki/Sparwood/Elk_Valley_Airport" title="Sparwood/Elk Valley Airport">Sparwood/Elk Valley Airport</a></td>
<td><a href="/wiki/Sparwood" title="Sparwood">Sparwood</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYSY</td>
<td>YSY</td>
<td><a href="/wiki/Sachs_Harbour_(David_Nasogaluak_Jr._Saaryuaq)_Airport" title="Sachs Harbour (David Nasogaluak Jr. Saaryuaq) Airport">Sachs Harbour (David Nasogaluak Jr. Saaryuaq) Airport</a></td>
<td><a href="/wiki/Sachs_Harbour" title="Sachs Harbour">Sachs Harbour</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYSZ</td>
<td></td>
<td><a href="/wiki/Sainte-Anne-des-Monts_Aerodrome" title="Sainte-Anne-des-Monts Aerodrome">Sainte-Anne-des-Monts Aerodrome</a></td>
<td><a href="/wiki/Sainte-Anne-des-Monts,_Quebec" class="mw-redirect" title="Sainte-Anne-des-Monts, Quebec">Sainte-Anne-Des-Monts</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYTA</td>
<td>YTA</td>
<td><a href="/wiki/Pembroke_Airport" title="Pembroke Airport">Pembroke Airport</a></td>
<td><a href="/wiki/Pembroke,_Ontario" title="Pembroke, Ontario">Pembroke</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYTB</td>
<td></td>
<td><a href="/wiki/Tillsonburg_Airport" title="Tillsonburg Airport">Tillsonburg Airport</a></td>
<td><a href="/wiki/Tillsonburg" title="Tillsonburg">Tillsonburg</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYTE</td>
<td>YTE</td>
<td><a href="/wiki/Cape_Dorset_Airport" title="Cape Dorset Airport">Cape Dorset Airport</a></td>
<td><a href="/wiki/Kinngait" title="Kinngait">Kinngait</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYTF</td>
<td>YTF</td>
<td><a href="/wiki/Alma_Airport" title="Alma Airport">Alma Airport</a></td>
<td><a href="/wiki/Alma,_Quebec" title="Alma, Quebec">Alma</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYTH</td>
<td>YTH</td>
<td><a href="/wiki/Thompson_Airport" title="Thompson Airport">Thompson Airport</a></td>
<td><a href="/wiki/Thompson,_Manitoba" title="Thompson, Manitoba">Thompson</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYTL</td>
<td>YTL</td>
<td><a href="/wiki/Big_Trout_Lake_Airport" title="Big Trout Lake Airport">Big Trout Lake Airport</a></td>
<td><a href="/wiki/Kitchenuhmaykoosib_Inninuwug_First_Nation" title="Kitchenuhmaykoosib Inninuwug First Nation">Kitchenuhmaykoosib Inninuwug First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYTN</td>
<td></td>
<td><a href="/wiki/Trenton_Aerodrome" title="Trenton Aerodrome">Trenton Aerodrome</a></td>
<td><a href="/wiki/Trenton,_Nova_Scotia" title="Trenton, Nova Scotia">Trenton</a></td>
<td><a href="/wiki/Nova_Scotia" title="Nova Scotia">NS</a>
</td></tr>
<tr>
<td>CYTQ</td>
<td>YTQ</td>
<td><a href="/wiki/Tasiujaq_Airport" title="Tasiujaq Airport">Tasiujaq Airport</a></td>
<td><a href="/wiki/Tasiujaq" title="Tasiujaq">Tasiujaq</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYTR</td>
<td>YTR</td>
<td><a href="/wiki/CFB_Trenton" title="CFB Trenton">CFB Trenton</a> (Trenton Airport)</td>
<td><a href="/wiki/Trenton,_Ontario" title="Trenton, Ontario">Trenton</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYTS</td>
<td>YTS</td>
<td><a href="/wiki/Timmins/Victor_M._Power_Airport" class="mw-redirect" title="Timmins/Victor M. Power Airport">Timmins/Victor M. Power Airport</a></td>
<td><a href="/wiki/Timmins" title="Timmins">Timmins</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYTZ</td>
<td>YTZ</td>
<td><a href="/wiki/Billy_Bishop_Toronto_City_Airport" title="Billy Bishop Toronto City Airport">Billy Bishop Toronto City Airport</a> (Toronto City Centre Airport, Toronto Island Airport)</td>
<td><a href="/wiki/Toronto" title="Toronto">Toronto</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYUB</td>
<td>YUB</td>
<td><a href="/wiki/Tuktoyaktuk/James_Gruben_Airport" title="Tuktoyaktuk/James Gruben Airport">Tuktoyaktuk/James Gruben Airport</a></td>
<td><a href="/wiki/Tuktoyaktuk" title="Tuktoyaktuk">Tuktoyaktuk</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYUL</td>
<td>YUL</td>
<td><em><a href="/wiki/Montr%C3%A9al%E2%80%93Trudeau_International_Airport" title="Montréal–Trudeau International Airport">Montréal–Trudeau International Airport</a></em></td>
<td><a href="/wiki/Montreal" title="Montreal">Montreal</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYUT</td>
<td>YUT</td>
<td><a href="/wiki/Naujaat_Airport" title="Naujaat Airport">Naujaat Airport</a></td>
<td><a href="/wiki/Naujaat" title="Naujaat">Naujaat</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYUX</td>
<td>YUX</td>
<td><a href="/wiki/Hall_Beach_Airport" title="Hall Beach Airport">Hall Beach Airport</a></td>
<td><a href="/wiki/Sanirajak" title="Sanirajak">Sanirajak</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYUY</td>
<td>YUY</td>
<td><a href="/wiki/Rouyn-Noranda_Airport" title="Rouyn-Noranda Airport">Rouyn-Noranda Airport</a></td>
<td><a href="/wiki/Rouyn-Noranda" title="Rouyn-Noranda">Rouyn-Noranda</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYVB</td>
<td>YVB</td>
<td><a href="/wiki/Bonaventure_Airport" title="Bonaventure Airport">Bonaventure Airport</a></td>
<td><a href="/wiki/Bonaventure,_Quebec" title="Bonaventure, Quebec">Bonaventure</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYVC</td>
<td>YVC</td>
<td><a href="/wiki/La_Ronge_(Barber_Field)_Airport" title="La Ronge (Barber Field) Airport">La Ronge (Barber Field) Airport</a></td>
<td><a href="/wiki/La_Ronge" title="La Ronge">La Ronge</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYVD</td>
<td></td>
<td><a href="/wiki/Virden/R.J._(Bob)_Andrew_Field_Regional_Aerodrome" title="Virden/R.J. (Bob) Andrew Field Regional Aerodrome">Virden/R.J. (Bob) Andrew Field Regional Aerodrome</a></td>
<td><a href="/wiki/Virden,_Manitoba" title="Virden, Manitoba">Virden</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYVG</td>
<td></td>
<td><a href="/wiki/Vermilion_Airport" title="Vermilion Airport">Vermilion Airport</a></td>
<td><a href="/wiki/Vermilion,_Alberta" title="Vermilion, Alberta">Vermilion</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYVK</td>
<td>YVE</td>
<td><a href="/wiki/Vernon_Regional_Airport" title="Vernon Regional Airport">Vernon Regional Airport</a></td>
<td><a href="/wiki/Vernon,_British_Columbia" title="Vernon, British Columbia">Vernon</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYVL</td>
<td>YCK</td>
<td><a href="/wiki/Colville_Lake/Tommy_Kochon_Aerodrome" title="Colville Lake/Tommy Kochon Aerodrome">Colville Lake/Tommy Kochon Aerodrome</a></td>
<td><a href="/wiki/Colville_Lake,_Northwest_Territories" title="Colville Lake, Northwest Territories">Colville Lake</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYVM</td>
<td>YVM</td>
<td><a href="/wiki/Qikiqtarjuaq_Airport" title="Qikiqtarjuaq Airport">Qikiqtarjuaq Airport</a></td>
<td><a href="/wiki/Qikiqtarjuaq" title="Qikiqtarjuaq">Qikiqtarjuaq</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYVO</td>
<td>YVO</td>
<td><a href="/wiki/Val-d%27Or_Airport" title="Val-d'Or Airport">Val-d'Or Airport</a></td>
<td><a href="/wiki/Val-d%27Or" title="Val-d'Or">Val-d'Or</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYVP</td>
<td>YVP</td>
<td><a href="/wiki/Kuujjuaq_Airport" title="Kuujjuaq Airport">Kuujjuaq Airport</a></td>
<td><a href="/wiki/Kuujjuaq" title="Kuujjuaq">Kuujjuaq</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYVQ</td>
<td>YVQ</td>
<td><a href="/wiki/Norman_Wells_Airport" title="Norman Wells Airport">Norman Wells Airport</a></td>
<td><a href="/wiki/Norman_Wells" title="Norman Wells">Norman Wells</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYVR</td>
<td>YVR</td>
<td><em><a href="/wiki/Vancouver_International_Airport" title="Vancouver International Airport">Vancouver International Airport</a></em></td>
<td><a href="/wiki/Vancouver" title="Vancouver">Vancouver</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYVT</td>
<td>YVT</td>
<td><a href="/wiki/Buffalo_Narrows_Airport" title="Buffalo Narrows Airport">Buffalo Narrows Airport</a></td>
<td><a href="/wiki/Buffalo_Narrows" title="Buffalo Narrows">Buffalo Narrows</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYVV</td>
<td>YVV</td>
<td><a href="/wiki/Wiarton_Airport" title="Wiarton Airport">Wiarton Airport</a></td>
<td><a href="/wiki/Wiarton,_Ontario" class="mw-redirect" title="Wiarton, Ontario">Wiarton</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYVZ</td>
<td>YVZ</td>
<td><a href="/wiki/Deer_Lake_Airport" title="Deer Lake Airport">Deer Lake Airport</a></td>
<td><a href="/wiki/Deer_Lake_First_Nation" title="Deer Lake First Nation">Deer Lake First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYWA</td>
<td>YWA</td>
<td><a href="/wiki/Petawawa_Heliport" title="Petawawa Heliport">Petawawa Heliport</a></td>
<td><a href="/wiki/Garrison_Petawawa" title="Garrison Petawawa">Garrison Petawawa</a> (<a href="/wiki/Petawawa" title="Petawawa">Petawawa</a>)</td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYWE</td>
<td></td>
<td><a href="/wiki/Wekwe%C3%A8t%C3%AC_Airport" title="Wekweètì Airport">Wekweètì Airport</a></td>
<td><a href="/wiki/Wekweeti" class="mw-redirect" title="Wekweeti">Wekweeti</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYWG</td>
<td>YWG</td>
<td><em><a href="/wiki/Winnipeg_James_Armstrong_Richardson_International_Airport" title="Winnipeg James Armstrong Richardson International Airport">Winnipeg James Armstrong Richardson International Airport</a></em></td>
<td><a href="/wiki/Winnipeg" title="Winnipeg">Winnipeg</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYWH</td>
<td>YWH</td>
<td><a href="/wiki/Victoria_Inner_Harbour_Airport" title="Victoria Inner Harbour Airport">Victoria Inner Harbour Airport</a> (Victoria Harbour Water Airport)</td>
<td><a href="/wiki/Victoria,_British_Columbia" title="Victoria, British Columbia">Victoria</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYWJ</td>
<td>YWJ</td>
<td><a href="/wiki/D%C3%A9line_Airport" title="Déline Airport">Déline Airport</a></td>
<td><a href="/wiki/D%C3%A9l%C4%B1%CC%A8n%C4%99" title="Délı̨nę">Délı̨nę</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYWK</td>
<td>YWK</td>
<td><a href="/wiki/Wabush_Airport" title="Wabush Airport">Wabush Airport</a></td>
<td><a href="/wiki/Wabush" title="Wabush">Wabush</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYWL</td>
<td>YWL</td>
<td><a href="/wiki/Williams_Lake_Airport" title="Williams Lake Airport">Williams Lake Airport</a></td>
<td><a href="/wiki/Williams_Lake,_British_Columbia" title="Williams Lake, British Columbia">Williams Lake</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYWM</td>
<td></td>
<td><a href="/wiki/Athabasca_Regional_Airport" title="Athabasca Regional Airport">Athabasca Regional Airport</a></td>
<td><a href="/wiki/Athabasca,_Alberta" title="Athabasca, Alberta">Athabasca</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYWN</td>
<td></td>
<td><a href="/wiki/Wainwright/Wainwright_(Field_21)_Airport" title="Wainwright/Wainwright (Field 21) Airport">Wainwright/Wainwright (Field 21) Airport</a> (CFB Wainwright)</td>
<td><a href="/wiki/Wainwright,_Alberta" title="Wainwright, Alberta">Wainwright</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYWP</td>
<td>YWP</td>
<td><a href="/wiki/Webequie_Airport" title="Webequie Airport">Webequie Airport</a></td>
<td><a href="/wiki/Webequie_First_Nation" title="Webequie First Nation">Webequie First Nation</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYWV</td>
<td>YWV</td>
<td><a href="/wiki/Wainwright_Aerodrome" title="Wainwright Aerodrome">Wainwright Aerodrome</a></td>
<td><a href="/wiki/Wainwright,_Alberta" title="Wainwright, Alberta">Wainwright</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYWY</td>
<td>YWY</td>
<td><a href="/wiki/Wrigley_Airport" title="Wrigley Airport">Wrigley Airport</a></td>
<td><a href="/wiki/Wrigley,_Northwest_Territories" title="Wrigley, Northwest Territories">Wrigley</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYXC</td>
<td>YXC</td>
<td><a href="/wiki/Cranbrook/Canadian_Rockies_International_Airport" title="Cranbrook/Canadian Rockies International Airport">Cranbrook/Canadian Rockies International Airport</a></td>
<td><a href="/wiki/Cranbrook,_British_Columbia" title="Cranbrook, British Columbia">Cranbrook</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYXE</td>
<td>YXE</td>
<td><em><a href="/wiki/Saskatoon_John_G._Diefenbaker_International_Airport" title="Saskatoon John G. Diefenbaker International Airport">Saskatoon John G. Diefenbaker International Airport</a></em> (Saskatoon International Airport)</td>
<td><a href="/wiki/Saskatoon" title="Saskatoon">Saskatoon</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYXH</td>
<td>YXH</td>
<td><a href="/wiki/Medicine_Hat_Airport" title="Medicine Hat Airport">Medicine Hat Airport</a></td>
<td><a href="/wiki/Medicine_Hat" title="Medicine Hat">Medicine Hat</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYXJ</td>
<td>YXJ</td>
<td><a href="/wiki/Fort_St._John_Airport" title="Fort St. John Airport">Fort St. John Airport</a> (North Peace Airport)</td>
<td><a href="/wiki/Fort_St._John,_British_Columbia" title="Fort St. John, British Columbia">Fort St. John</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYXK</td>
<td>YXK</td>
<td><a href="/wiki/Rimouski_Aerodrome" title="Rimouski Aerodrome">Rimouski Aerodrome</a></td>
<td><a href="/wiki/Rimouski" title="Rimouski">Rimouski</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYXL</td>
<td>YXL</td>
<td><a href="/wiki/Sioux_Lookout_Airport" title="Sioux Lookout Airport">Sioux Lookout Airport</a></td>
<td><a href="/wiki/Sioux_Lookout" title="Sioux Lookout">Sioux Lookout</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYXN</td>
<td>YXN</td>
<td><a href="/wiki/Whale_Cove_Airport" title="Whale Cove Airport">Whale Cove Airport</a></td>
<td><a href="/wiki/Whale_Cove,_Nunavut" title="Whale Cove, Nunavut">Whale Cove</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYXP</td>
<td>YXP</td>
<td><a href="/wiki/Pangnirtung_Airport" title="Pangnirtung Airport">Pangnirtung Airport</a></td>
<td><a href="/wiki/Pangnirtung" title="Pangnirtung">Pangnirtung</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYXQ</td>
<td>YXQ</td>
<td><a href="/wiki/Beaver_Creek_Airport" title="Beaver Creek Airport">Beaver Creek Airport</a></td>
<td><a href="/wiki/Beaver_Creek,_Yukon" title="Beaver Creek, Yukon">Beaver Creek</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CYXR</td>
<td>YXR</td>
<td><a href="/wiki/Earlton_(Timiskaming_Regional)_Airport" title="Earlton (Timiskaming Regional) Airport">Earlton (Timiskaming Regional) Airport</a></td>
<td><a href="/wiki/Armstrong,_Ontario" title="Armstrong, Ontario">Earlton</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYXS</td>
<td>YXS</td>
<td><em><a href="/wiki/Prince_George_Airport" title="Prince George Airport">Prince George Airport</a></em></td>
<td><a href="/wiki/Prince_George,_British_Columbia" title="Prince George, British Columbia">Prince George</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYXT</td>
<td>YXT</td>
<td><a href="/wiki/Northwest_Regional_Airport_Terrace-Kitimat" title="Northwest Regional Airport Terrace-Kitimat">Northwest Regional Airport Terrace-Kitimat</a> (Terrace Airport)</td>
<td><a href="/wiki/Terrace,_British_Columbia" title="Terrace, British Columbia">Terrace</a> and <a href="/wiki/Kitimat" title="Kitimat">Kitimat</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYXU</td>
<td>YXU</td>
<td><em><a href="/wiki/London_International_Airport" title="London International Airport">London International Airport</a></em></td>
<td><a href="/wiki/London,_Ontario" title="London, Ontario">London</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYXX</td>
<td>YXX</td>
<td><a href="/wiki/Abbotsford_International_Airport" title="Abbotsford International Airport">Abbotsford International Airport</a></td>
<td><a href="/wiki/Abbotsford,_British_Columbia" title="Abbotsford, British Columbia">Abbotsford</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYXY</td>
<td>YXY</td>
<td><em><a href="/wiki/Erik_Nielsen_Whitehorse_International_Airport" title="Erik Nielsen Whitehorse International Airport">Erik Nielsen Whitehorse International Airport</a></em></td>
<td><a href="/wiki/Whitehorse,_Yukon" class="mw-redirect" title="Whitehorse, Yukon">Whitehorse</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CYXZ</td>
<td>YXZ</td>
<td><a href="/wiki/Wawa_Airport" title="Wawa Airport">Wawa Airport</a></td>
<td><a href="/wiki/Wawa,_Ontario" title="Wawa, Ontario">Wawa</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYYB</td>
<td>YYB</td>
<td><a href="/wiki/North_Bay/Jack_Garland_Airport" title="North Bay/Jack Garland Airport">North Bay/Jack Garland Airport</a> (North Bay Airport)</td>
<td><a href="/wiki/North_Bay,_Ontario" title="North Bay, Ontario">North Bay</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYYC</td>
<td>YYC</td>
<td><em><a href="/wiki/Calgary_International_Airport" title="Calgary International Airport">Calgary International Airport</a></em></td>
<td><a href="/wiki/Calgary" title="Calgary">Calgary</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYYD</td>
<td>YYD</td>
<td><a href="/wiki/Smithers_Airport" title="Smithers Airport">Smithers Airport</a></td>
<td><a href="/wiki/Smithers,_British_Columbia" title="Smithers, British Columbia">Smithers</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYYE</td>
<td>YYE</td>
<td><a href="/wiki/Fort_Nelson_Airport" title="Fort Nelson Airport">Fort Nelson Airport</a></td>
<td><a href="/wiki/Fort_Nelson,_British_Columbia" title="Fort Nelson, British Columbia">Fort Nelson</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYYF</td>
<td>YYF</td>
<td><a href="/wiki/Penticton_Regional_Airport" title="Penticton Regional Airport">Penticton Regional Airport</a></td>
<td><a href="/wiki/Penticton" title="Penticton">Penticton</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYYG</td>
<td>YYG</td>
<td><em><a href="/wiki/Charlottetown_Airport" title="Charlottetown Airport">Charlottetown Airport</a></em></td>
<td><a href="/wiki/Charlottetown" title="Charlottetown">Charlottetown</a></td>
<td><a href="/wiki/Prince_Edward_Island" title="Prince Edward Island">PE</a>
</td></tr>
<tr>
<td>CYYH</td>
<td>YYH</td>
<td><a href="/wiki/Taloyoak_Airport" title="Taloyoak Airport">Taloyoak Airport</a></td>
<td><a href="/wiki/Taloyoak" title="Taloyoak">Taloyoak</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYYJ</td>
<td>YYJ</td>
<td><em><a href="/wiki/Victoria_International_Airport" title="Victoria International Airport">Victoria International Airport</a></em></td>
<td><a href="/wiki/Victoria,_British_Columbia" title="Victoria, British Columbia">Victoria</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYYL</td>
<td>YYL</td>
<td><a href="/wiki/Lynn_Lake_Airport" title="Lynn Lake Airport">Lynn Lake Airport</a></td>
<td><a href="/wiki/Lynn_Lake" title="Lynn Lake">Lynn Lake</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYYM</td>
<td></td>
<td><a href="/wiki/Cowley_Airport" title="Cowley Airport">Cowley Airport</a></td>
<td><a href="/wiki/Cowley,_Alberta" title="Cowley, Alberta">Cowley</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYYN</td>
<td>YYN</td>
<td><a href="/wiki/Swift_Current_Airport" title="Swift Current Airport">Swift Current Airport</a></td>
<td><a href="/wiki/Swift_Current" title="Swift Current">Swift Current</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYYO</td>
<td></td>
<td><a href="/wiki/Wynyard/W._B._Needham_Field_Aerodrome" title="Wynyard/W. B. Needham Field Aerodrome">Wynyard/W. B. Needham Field Aerodrome</a></td>
<td><a href="/wiki/Wynyard,_Saskatchewan" title="Wynyard, Saskatchewan">Wynyard</a></td>
<td><a href="/wiki/Saskatchewan" title="Saskatchewan">SK</a>
</td></tr>
<tr>
<td>CYYQ</td>
<td>YYQ</td>
<td><a href="/wiki/Churchill_Airport" title="Churchill Airport">Churchill Airport</a></td>
<td><a href="/wiki/Churchill,_Manitoba" title="Churchill, Manitoba">Churchill</a></td>
<td><a href="/wiki/Manitoba" title="Manitoba">MB</a>
</td></tr>
<tr>
<td>CYYR</td>
<td>YYR</td>
<td><a href="/wiki/CFB_Goose_Bay" title="CFB Goose Bay">CFB Goose Bay</a> (Goose Bay Airport)</td>
<td><a href="/wiki/Happy_Valley-Goose_Bay" title="Happy Valley-Goose Bay">Happy Valley-Goose Bay</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYYT</td>
<td>YYT</td>
<td><em><a href="/wiki/St._John%27s_International_Airport" title="St. John's International Airport">St. John's International Airport</a></em></td>
<td><a href="/wiki/St._John%27s,_Newfoundland_and_Labrador" title="St. John's, Newfoundland and Labrador">St. John's</a></td>
<td><a href="/wiki/Newfoundland_and_Labrador" title="Newfoundland and Labrador">NL</a>
</td></tr>
<tr>
<td>CYYU</td>
<td>YYU</td>
<td><a href="/wiki/Kapuskasing_Airport" title="Kapuskasing Airport">Kapuskasing Airport</a></td>
<td><a href="/wiki/Kapuskasing" title="Kapuskasing">Kapuskasing</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYYW</td>
<td>YYW</td>
<td><a href="/wiki/Armstrong_Airport" title="Armstrong Airport">Armstrong Airport</a></td>
<td><a href="/wiki/Armstrong,_Thunder_Bay_District,_Ontario" title="Armstrong, Thunder Bay District, Ontario">Armstrong</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYYY</td>
<td>YYY</td>
<td><a href="/wiki/Mont-Joli_Airport" title="Mont-Joli Airport">Mont-Joli Airport</a></td>
<td><a href="/wiki/Mont-Joli" title="Mont-Joli">Mont-Joli</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYYZ</td>
<td>YYZ</td>
<td><em><a href="/wiki/Toronto_Pearson_International_Airport" title="Toronto Pearson International Airport">Toronto Pearson International Airport</a></em></td>
<td><a href="/wiki/Toronto" title="Toronto">Toronto</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYZD</td>
<td>YZD</td>
<td><a href="/wiki/Downsview_Airport" title="Downsview Airport">Downsview Airport</a> (Toronto/Downsview Airport)</td>
<td><a href="/wiki/Toronto" title="Toronto">Toronto</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYZE</td>
<td>YZE</td>
<td><a href="/wiki/Gore_Bay-Manitoulin_Airport" title="Gore Bay-Manitoulin Airport">Gore Bay-Manitoulin Airport</a></td>
<td><a href="/wiki/Gore_Bay,_Ontario" title="Gore Bay, Ontario">Gore Bay</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYZF</td>
<td>YZF</td>
<td><em><a href="/wiki/Yellowknife_Airport" title="Yellowknife Airport">Yellowknife Airport</a></em></td>
<td><a href="/wiki/Yellowknife" title="Yellowknife">Yellowknife</a></td>
<td><a href="/wiki/Northwest_Territories" title="Northwest Territories">NT</a>
</td></tr>
<tr>
<td>CYZG</td>
<td>YZG</td>
<td><a href="/wiki/Salluit_Airport" title="Salluit Airport">Salluit Airport</a></td>
<td><a href="/wiki/Salluit" title="Salluit">Salluit</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYZH</td>
<td>YZH</td>
<td><a href="/wiki/Slave_Lake_Airport" title="Slave Lake Airport">Slave Lake Airport</a></td>
<td><a href="/wiki/Slave_Lake" title="Slave Lake">Slave Lake</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYZP</td>
<td>YZP</td>
<td><a href="/wiki/Sandspit_Airport" title="Sandspit Airport">Sandspit Airport</a></td>
<td><a href="/wiki/Sandspit,_British_Columbia" title="Sandspit, British Columbia">Sandspit</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYZR</td>
<td>YZR</td>
<td><a href="/wiki/Sarnia_Chris_Hadfield_Airport" title="Sarnia Chris Hadfield Airport">Sarnia Chris Hadfield Airport</a></td>
<td><a href="/wiki/Sarnia" title="Sarnia">Sarnia</a></td>
<td><a href="/wiki/Ontario" title="Ontario">ON</a>
</td></tr>
<tr>
<td>CYZS</td>
<td>YZS</td>
<td><a href="/wiki/Coral_Harbour_Airport" title="Coral Harbour Airport">Coral Harbour Airport</a></td>
<td><a href="/wiki/Coral_Harbour" title="Coral Harbour">Coral Harbour</a></td>
<td><a href="/wiki/Nunavut" title="Nunavut">NU</a>
</td></tr>
<tr>
<td>CYZT</td>
<td>YZT</td>
<td><a href="/wiki/Port_Hardy_Airport" title="Port Hardy Airport">Port Hardy Airport</a></td>
<td><a href="/wiki/Port_Hardy" title="Port Hardy">Port Hardy</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr>
<tr>
<td>CYZU</td>
<td>YZU</td>
<td><a href="/wiki/Whitecourt_Airport" title="Whitecourt Airport">Whitecourt Airport</a></td>
<td><a href="/wiki/Whitecourt" title="Whitecourt">Whitecourt</a></td>
<td><a href="/wiki/Alberta" title="Alberta">AB</a>
</td></tr>
<tr>
<td>CYZV</td>
<td>YZV</td>
<td><a href="/wiki/Sept-%C3%8Eles_Airport" title="Sept-Îles Airport">Sept-Îles Airport</a></td>
<td><a href="/wiki/Sept-%C3%8Eles,_Quebec" title="Sept-Îles, Quebec">Sept-Îles</a></td>
<td><a href="/wiki/Quebec" title="Quebec">QC</a>
</td></tr>
<tr>
<td>CYZW</td>
<td>YZW</td>
<td><a href="/wiki/Teslin_Airport" title="Teslin Airport">Teslin Airport</a></td>
<td><a href="/wiki/Teslin,_Yukon" title="Teslin, Yukon">Teslin</a></td>
<td><a href="/wiki/Yukon" title="Yukon">YT</a>
</td></tr>
<tr>
<td>CYZX</td>
<td>YZX</td>
<td><a href="/wiki/CFB_Greenwood" title="CFB Greenwood">CFB Greenwood</a> (Greenwood Airport)</td>
<td><a href="/wiki/Greenwood,_Nova_Scotia" title="Greenwood, Nova Scotia">Greenwood</a></td>
<td><a href="/wiki/Nova_Scotia" title="Nova Scotia">NS</a>
</td></tr>
<tr>
<td>CYZY</td>
<td>YZY</td>
<td><a href="/wiki/Mackenzie_Airport" title="Mackenzie Airport">Mackenzie Airport</a></td>
<td><a href="/wiki/Mackenzie,_British_Columbia" title="Mackenzie, British Columbia">Mackenzie</a></td>
<td><a href="/wiki/British_Columbia" title="British Columbia">BC</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open('CY – Canada - CAN.csv', mode='w', newline='', encoding='utf-8') as csv_file:
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