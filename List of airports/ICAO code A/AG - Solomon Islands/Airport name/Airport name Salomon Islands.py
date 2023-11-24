from bs4 import BeautifulSoup
import csv

html_content = '''
<table class="wikitable sortable jquery-tablesorter">

<thead><tr valign="baseline">
<th style="text-align:left; white-space:nowrap;" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Airport name
</th>
<th style="text-align:left; white-space:nowrap;" class="headerSort headerSortDown" tabindex="0" role="columnheader button" title="Sort initial"><a href="/wiki/List_of_cities,_towns_and_villages_in_the_Solomon_Islands" class="mw-redirect" title="List of cities, towns and villages in the Solomon Islands">Location</a>
</th>
<th style="text-align:left; white-space:nowrap;" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/Provinces_of_the_Solomon_Islands" class="mw-redirect" title="Provinces of the Solomon Islands">Province</a>
</th>
<th style="text-align:left; width:4em;" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/ICAO_airport_code" title="ICAO airport code">ICAO</a>
</th>
<th style="text-align:left; width:4em;" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending"><a href="/wiki/IATA_airport_code" title="IATA airport code">IATA</a>
</th></tr></thead><tbody>








































<tr valign="top">
<td><a href="/wiki/Balalae" class="mw-redirect" title="Balalae">Balalae</a>, <a href="/wiki/Shortland_Island" title="Shortland Island">Shortland Island</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGGE
</td>
<td>BAS
</td>
<td><b><a href="/wiki/Balalae_Airport" title="Balalae Airport">Balalae Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Barora,_Solomon_Islands&amp;action=edit&amp;redlink=1" class="new" title="Barora, Solomon Islands (page does not exist)">Barora</a>, <a href="/wiki/New_Georgia_Island" class="mw-redirect" title="New Georgia Island">New Georgia Island</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>
</td>
<td>RRI
</td>
<td><a href="/w/index.php?title=Barora_Airport&amp;action=edit&amp;redlink=1" class="new" title="Barora Airport (page does not exist)">Barora Airport</a>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Batuna&amp;action=edit&amp;redlink=1" class="new" title="Batuna (page does not exist)">Batuna</a>, <a href="/wiki/Vangunu" title="Vangunu">Vangunu Island</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGBT
</td>
<td>BPF
</td>
<td><a href="/w/index.php?title=Batuna_Airport&amp;action=edit&amp;redlink=1" class="new" title="Batuna Airport (page does not exist)">Batuna Airport</a>
</td></tr><tr valign="top">
<td><a href="/wiki/Gatokae" class="mw-redirect" title="Gatokae">Gatokae</a> (Nggatokae Island), <a href="/wiki/New_Georgia_Islands" title="New Georgia Islands">New Georgia Islands</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGOK
</td>
<td>GTA
</td>
<td><b><a href="/wiki/Gatokae_Aerodrome" title="Gatokae Aerodrome">Gatokae Aerodrome</a></b> (Gatokae Airport)
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Geva,_Solomon_Islands&amp;action=edit&amp;redlink=1" class="new" title="Geva, Solomon Islands (page does not exist)">Geva</a>, <a href="/wiki/Vella_Lavella_Island" class="mw-redirect" title="Vella Lavella Island">Vella Lavella Island</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGEV
</td>
<td>GEF
</td>
<td><a href="/w/index.php?title=Geva_Airport&amp;action=edit&amp;redlink=1" class="new" title="Geva Airport (page does not exist)">Geva Airport</a>
</td></tr><tr valign="top">
<td><a href="/wiki/Gizo,_Solomon_Islands" title="Gizo, Solomon Islands">Gizo</a>, <a href="/wiki/Ghizo_Island" title="Ghizo Island">Ghizo Island</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGGN
</td>
<td>GZO
</td>
<td><b><a href="/wiki/Nusatupe_Airport" title="Nusatupe Airport">Nusatupe Airport</a></b> (Gizo Airport)
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Kukudu&amp;action=edit&amp;redlink=1" class="new" title="Kukudu (page does not exist)">Kukudu</a> (Kukundu), <a href="/wiki/Kolombangara" title="Kolombangara">Kolombangara</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGKU
</td>
<td>KUE
</td>
<td><a href="/w/index.php?title=Kukudu_Airport&amp;action=edit&amp;redlink=1" class="new" title="Kukudu Airport (page does not exist)">Kukudu Airport</a>
</td></tr><tr valign="top">
<td><a href="/wiki/Mono_Island" title="Mono Island">Mono Island</a>, <a href="/wiki/Treasury_Islands" title="Treasury Islands">Treasury Islands</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGGO
</td>
<td>MNY
</td>
<td><b><a href="/wiki/Mono_Airport" title="Mono Airport">Mono Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/wiki/Munda,_Solomon_Islands" title="Munda, Solomon Islands">Munda</a>, <a href="/wiki/New_Georgia" title="New Georgia">New Georgia Island</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGGM
</td>
<td>MUA
</td>
<td><b><a href="/wiki/Munda_Airport" title="Munda Airport">Munda Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/wiki/Ramata_Airport" title="Ramata Airport">Ramata Airport</a> (Ramata Island)
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGRM
</td>
<td>RBV
</td>
<td><b><a href="/wiki/Ramata_Airport" title="Ramata Airport">Ramata Airport</a></b> (Ramata Island Airstrip)
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Ringgi_Cove&amp;action=edit&amp;redlink=1" class="new" title="Ringgi Cove (page does not exist)">Ringgi Cove</a>, <a href="/wiki/Kolombangara" title="Kolombangara">Kolombangara</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGRC
</td>
<td>RIN
</td>
<td><a href="/w/index.php?title=Ringgi_Cove_Airport&amp;action=edit&amp;redlink=1" class="new" title="Ringgi Cove Airport (page does not exist)">Ringgi Cove Airport</a><sup id="cite_ref-IATA_1-0" class="reference"><a href="#cite_note-IATA-1">[1]</a></sup> (Vila Airport)
</td></tr><tr valign="top">
<td><a href="/wiki/Seghe" class="mw-redirect" title="Seghe">Seghe</a>, <a href="/wiki/New_Georgia" title="New Georgia">New Georgia Island</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>AGGS
</td>
<td>EGM
</td>
<td><b><a href="/wiki/Seghe_Airport" title="Seghe Airport">Seghe Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Viru,_Solomon_Islands&amp;action=edit&amp;redlink=1" class="new" title="Viru, Solomon Islands (page does not exist)">Viru</a>, <a href="/wiki/New_Georgia_Island" class="mw-redirect" title="New Georgia Island">New Georgia Island</a>
</td>
<td><a href="/wiki/Western_Province_(Solomon_Islands)" title="Western Province (Solomon Islands)">Western</a>
</td>
<td>
</td>
<td>VIU
</td>
<td><a href="/w/index.php?title=Viru_Airport&amp;action=edit&amp;redlink=1" class="new" title="Viru Airport (page does not exist)">Viru Airport</a> (Viru Harbour Airstrip)
</td></tr><tr>
<td><a href="/wiki/Lomlom" title="Lomlom">Lomlom</a>, <a href="/wiki/Reef_Islands" title="Reef Islands">Reef Islands</a>
</td>
<td><a href="/wiki/Temotu_Province" title="Temotu Province">Temotu</a>
</td>
<td>AGLM
</td>
<td>LLM
</td>
<td><b><a href="/wiki/Lomlom_Airport" title="Lomlom Airport">Lomlom Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/wiki/Santa_Cruz_Islands" title="Santa Cruz Islands">Santa Cruz Islands</a>, <a href="/wiki/Nendo_Island" class="mw-redirect" title="Nendo Island">Nendo Island</a>
</td>
<td><a href="/wiki/Temotu_Province" title="Temotu Province">Temotu</a>
</td>
<td>AGGL
</td>
<td>SCZ
</td>
<td><b><a href="/wiki/Luova_Airport" title="Luova Airport">Luova Airport</a></b> (Santa Cruz Airport)
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Anua,_Solomon_Islands&amp;action=edit&amp;redlink=1" class="new" title="Anua, Solomon Islands (page does not exist)">Anua</a>, <a href="/wiki/Bellona_Island" title="Bellona Island">Bellona Island</a>
</td>
<td><span class="nowrap"><a href="/wiki/Rennell_and_Bellona_Province" title="Rennell and Bellona Province">Rennell and Bellona</a></span>
</td>
<td>AGGB
</td>
<td>BNY
</td>
<td><b><a href="/wiki/Anua_Airport" title="Anua Airport">Bellona/Anua Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/wiki/Tingoa" class="mw-redirect" title="Tingoa">Tingoa</a>, <a href="/wiki/Rennell_Island" title="Rennell Island">Rennell Island</a>
</td>
<td><a href="/wiki/Rennell_and_Bellona_Province" title="Rennell and Bellona Province">Rennell and Bellona</a>
</td>
<td>AGGR
</td>
<td>RNL
</td>
<td><b><a href="/wiki/Tingoa_Airport" title="Tingoa Airport">Rennell/Tingoa Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Afutara&amp;action=edit&amp;redlink=1" class="new" title="Afutara (page does not exist)">Afutara</a>, <a href="/wiki/Malaita" title="Malaita">Malaita Island</a>
</td>
<td><a href="/wiki/Malaita_Province" title="Malaita Province">Malaita</a>
</td>
<td>AGAF
</td>
<td>AFT
</td>
<td><b><a href="/wiki/Afutara_Airport" title="Afutara Airport">Afutara Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Atoifi&amp;action=edit&amp;redlink=1" class="new" title="Atoifi (page does not exist)">Atoifi</a>, <a href="/wiki/Malaita" title="Malaita">Malaita Island</a>
</td>
<td><a href="/wiki/Malaita_Province" title="Malaita Province">Malaita</a>
</td>
<td>AGAT
</td>
<td>ATD
</td>
<td><b><a href="/wiki/Uru_Harbour_Airport" title="Uru Harbour Airport">Uru Harbour Airport</a></b> (Atoifi Airport)
</td></tr><tr valign="top">
<td><a href="/wiki/Auki" title="Auki">Auki</a>, <a href="/wiki/Malaita" title="Malaita">Malaita Island</a>
</td>
<td><a href="/wiki/Malaita_Province" title="Malaita Province">Malaita</a>
</td>
<td>AGGA
</td>
<td>AKS
</td>
<td><b><a href="/wiki/Auki_Gwaunaru%27u_Airport" title="Auki Gwaunaru'u Airport">Auki Gwaunaru'u Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Kwai_Harbour&amp;action=edit&amp;redlink=1" class="new" title="Kwai Harbour (page does not exist)">Kwai Harbour</a>
</td>
<td><a href="/wiki/Malaita_Province" title="Malaita Province">Malaita</a>
</td>
<td>
</td>
<td>KWR
</td>
<td><a href="/w/index.php?title=Kwai_Harbour_Airport&amp;action=edit&amp;redlink=1" class="new" title="Kwai Harbour Airport (page does not exist)">Kwai Harbour Airport</a>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Onepusu&amp;action=edit&amp;redlink=1" class="new" title="Onepusu (page does not exist)">Onepusu</a>
</td>
<td><a href="/wiki/Malaita_Province" title="Malaita Province">Malaita</a>
</td>
<td>
</td>
<td>ONE
</td>
<td><a href="/w/index.php?title=Onepusu_Airport&amp;action=edit&amp;redlink=1" class="new" title="Onepusu Airport (page does not exist)">Onepusu Airport</a>
</td></tr><tr valign="top">
<td><a href="/wiki/Ontong_Java" class="mw-redirect" title="Ontong Java">Ontong Java</a>
</td>
<td><a href="/wiki/Malaita_Province" title="Malaita Province">Malaita</a>
</td>
<td>AGGQ
</td>
<td>
</td>
<td><a href="/w/index.php?title=Ontong_Java_Airport&amp;action=edit&amp;redlink=1" class="new" title="Ontong Java Airport (page does not exist)">Ontong Java Airport</a>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Parasi,_Solomon_Islands&amp;action=edit&amp;redlink=1" class="new" title="Parasi, Solomon Islands (page does not exist)">Parasi</a>
</td>
<td><a href="/wiki/Malaita_Province" title="Malaita Province">Malaita</a>
</td>
<td>
</td>
<td>PRS
</td>
<td><a href="/w/index.php?title=Parasi_Airport&amp;action=edit&amp;redlink=1" class="new" title="Parasi Airport (page does not exist)">Parasi Airport</a>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Tarapaina&amp;action=edit&amp;redlink=1" class="new" title="Tarapaina (page does not exist)">Tarapaina</a>
</td>
<td><a href="/wiki/Malaita_Province" title="Malaita Province">Malaita</a>
</td>
<td>
</td>
<td>TAA
</td>
<td><a href="/w/index.php?title=Tarapaina_Airport&amp;action=edit&amp;redlink=1" class="new" title="Tarapaina Airport (page does not exist)">Tarapaina Airport</a>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Arona,_Solomon_Islands&amp;action=edit&amp;redlink=1" class="new" title="Arona, Solomon Islands (page does not exist)">Arona</a>, <a href="/wiki/Ulawa_Island" title="Ulawa Island">Ulawa Island</a>
</td>
<td><a href="/wiki/Makira-Ulawa_Province" title="Makira-Ulawa Province">Makira-Ulawa</a>
</td>
<td>AGAR
</td>
<td>RNA
</td>
<td><b><a href="/wiki/Ulawa_Airport" title="Ulawa Airport">Ulawa Airport</a></b> (Arona Airport)
</td></tr><tr valign="top">
<td><a href="/wiki/Kirakira" title="Kirakira">Kirakira</a>, <a href="/wiki/Makira" title="Makira">Makira Island</a>
</td>
<td><a href="/wiki/Makira-Ulawa_Province" title="Makira-Ulawa Province">Makira-Ulawa</a>
</td>
<td>AGGK
</td>
<td>IRA
</td>
<td><b><a href="/wiki/Kirakira_Airport" title="Kirakira Airport">Kirakira Airport</a></b> (Ngorangora Airstrip)
</td></tr><tr valign="top">
<td><a href="/wiki/Santa_Ana_Island" class="mw-redirect" title="Santa Ana Island">Santa Ana Island</a> (Owaraha)
</td>
<td><a href="/wiki/Makira-Ulawa_Province" title="Makira-Ulawa Province">Makira-Ulawa</a>
</td>
<td>AGGT
</td>
<td>NNB
</td>
<td><b><a href="/wiki/Santa_Ana_Airport_(Solomon_Islands)" title="Santa Ana Airport (Solomon Islands)">Santa Ana Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Maringe&amp;action=edit&amp;redlink=1" class="new" title="Maringe (page does not exist)">Maringe</a>, <a href="/wiki/Fera_Island" title="Fera Island">Fera Island</a> (near <a href="/wiki/Santa_Isabel_Island" title="Santa Isabel Island">Santa Isabel Island</a>)
</td>
<td><a href="/wiki/Isabel_Province" title="Isabel Province">Isabel</a>
</td>
<td>AGGF
</td>
<td>FRE
</td>
<td><b><a href="/wiki/Fera_Airport" title="Fera Airport">Fera Airport</a></b> (Fera/Maringe Airport)
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Suavanao&amp;action=edit&amp;redlink=1" class="new" title="Suavanao (page does not exist)">Suavanao</a>, <a href="/wiki/Santa_Isabel_Island" title="Santa Isabel Island">Santa Isabel Island</a>
</td>
<td><a href="/wiki/Isabel_Province" title="Isabel Province">Isabel</a>
</td>
<td>AGGV
</td>
<td>VAO
</td>
<td><b><a href="/wiki/Suavanao_Airport" title="Suavanao Airport">Suavanao Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Avu_Avu&amp;action=edit&amp;redlink=1" class="new" title="Avu Avu (page does not exist)">Avu Avu</a>
</td>
<td><a href="/wiki/Guadalcanal_Province" title="Guadalcanal Province">Guadalcanal</a>
</td>
<td>AGGJ
</td>
<td>AVU
</td>
<td><b><a href="/w/index.php?title=Avu_Avu_Airport&amp;action=edit&amp;redlink=1" class="new" title="Avu Avu Airport (page does not exist)">Avu Avu Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/wiki/Honiara" title="Honiara">Honiara</a>, <a href="/wiki/Guadalcanal" title="Guadalcanal">Guadalcanal Island</a>
</td>
<td><a href="/wiki/Guadalcanal_Province" title="Guadalcanal Province">Guadalcanal</a>
</td>
<td>AGGH
</td>
<td>HIR
</td>
<td><b><a href="/wiki/Honiara_International_Airport" title="Honiara International Airport">Honiara International Airport</a></b> <small>(formerly Henderson Field)</small>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Marau,_Solomon_Islands&amp;action=edit&amp;redlink=1" class="new" title="Marau, Solomon Islands (page does not exist)">Marau</a>, <a href="/wiki/Guadalcanal" title="Guadalcanal">Guadalcanal Island</a>
</td>
<td><a href="/wiki/Guadalcanal_Province" title="Guadalcanal Province">Guadalcanal</a>
</td>
<td>AGGU
</td>
<td>RUS
</td>
<td><b><a href="/wiki/Marau_Airport" title="Marau Airport">Marau Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Parasi,_Solomon_Islands&amp;action=edit&amp;redlink=1" class="new" title="Parasi, Solomon Islands (page does not exist)">Parasi</a>, <a href="/wiki/Marau_Sound" title="Marau Sound">Marau Sound Island</a>
</td>
<td><a href="/wiki/Guadalcanal_Province" title="Guadalcanal Province">Guadalcanal</a>
</td>
<td>AGGP
</td>
<td>PRS
</td>
<td><a href="/wiki/Marau_Airport" title="Marau Airport">Marau Airport</a> (Parasi Airport)
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Mbambanakira&amp;action=edit&amp;redlink=1" class="new" title="Mbambanakira (page does not exist)">Mbambanakira</a>, <a href="/wiki/Guadalcanal" title="Guadalcanal">Guadalcanal Island</a>
</td>
<td><a href="/wiki/Guadalcanal_Province" title="Guadalcanal Province">Guadalcanal</a>
</td>
<td>AGGI
</td>
<td>MBU
</td>
<td><b><a href="/wiki/Mbambanakira_Airport" title="Mbambanakira Airport">Mbambanakira Airport</a></b> (Babanakira Airfield)
</td></tr><tr valign="top">
<td><a href="/wiki/Choiseul_Bay" title="Choiseul Bay">Choiseul Bay</a>, <a href="/wiki/Taro_Island" title="Taro Island">Taro Island</a>
</td>
<td><a href="/wiki/Choiseul_Province" title="Choiseul Province">Choiseul</a>
</td>
<td>AGGC
</td>
<td>CHY
</td>
<td><b><a href="/wiki/Choiseul_Bay_Airport" title="Choiseul Bay Airport">Choiseul Bay Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/w/index.php?title=Kaghau_Island&amp;action=edit&amp;redlink=1" class="new" title="Kaghau Island (page does not exist)">Kaghau Island</a>
</td>
<td><a href="/wiki/Choiseul_Province" title="Choiseul Province">Choiseul</a>
</td>
<td>AGKG
</td>
<td>KGE
</td>
<td><b><a href="/wiki/Kaghau_Airport" title="Kaghau Airport">Kaghau Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/wiki/Yandina,_Solomon_Islands" title="Yandina, Solomon Islands">Yandina</a>, <a href="/wiki/Mbanika_Island" class="mw-redirect" title="Mbanika Island">Mbanika Island</a>, <a href="/wiki/Russell_Islands" title="Russell Islands">Russell Islands</a>
</td>
<td><a href="/wiki/Central_Province_(Solomon_Islands)" title="Central Province (Solomon Islands)">Central Province</a>
</td>
<td>AGGY
</td>
<td>XYA
</td>
<td><b><a href="/wiki/Yandina_Airport" title="Yandina Airport">Yandina Airport</a></b>
</td></tr><tr valign="top">
<td><a href="/wiki/Anuha_Island" class="mw-redirect" title="Anuha Island">Anuha Island</a>, <a href="/wiki/Nggela_Islands" title="Nggela Islands">Nggela Islands</a>
</td>
<td><a href="/wiki/Central_Province_(Solomon_Islands)" title="Central Province (Solomon Islands)">Central</a>
</td>
<td>
</td>
<td>ANH
</td>
<td><a href="/w/index.php?title=Anuha_Airport&amp;action=edit&amp;redlink=1" class="new" title="Anuha Airport (page does not exist)">Anuha Airport</a>
</td></tr><tr valign="top">
<td><a href="/wiki/Savo_Island" title="Savo Island">Savo Island</a>
</td>
<td><a href="/wiki/Central_Province_(Solomon_Islands)" title="Central Province (Solomon Islands)">Central</a>
</td>
<td>
</td>
<td>SVY
</td>
<td><a href="/w/index.php?title=Savo_Airport&amp;action=edit&amp;redlink=1" class="new" title="Savo Airport (page does not exist)">Savo Airport</a>
</td></tr><tr valign="top">
<td><a href="/wiki/Tulagi_Island" class="mw-redirect" title="Tulagi Island">Tulagi Island</a> (Tulaghi)
</td>
<td><a href="/wiki/Central_Province_(Solomon_Islands)" title="Central Province (Solomon Islands)">Central</a>
</td>
<td>
</td>
<td>TLG
</td>
<td><a href="/w/index.php?title=Tulagi_Island_Airport&amp;action=edit&amp;redlink=1" class="new" title="Tulagi Island Airport (page does not exist)">Tulagi Island Airport</a>
</td></tr></tbody><tfoot></tfoot></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

# Trouver le tableau dans le HTML
table = soup.find('table', {'class': 'wikitable'})

# Initialiser une liste pour stocker les noms des aéroports
airport_names = []

# Trouver toutes les lignes du tableau sauf la première (l'entête)
rows = table.find_all('tr')[1:]

# Parcourir chaque ligne et extraire le nom de l'aéroport de la première colonne
for row in rows:
    columns = row.find_all('td')
    airport_name = columns[0].text.strip()  # La première colonne contient le nom de l'aéroport
    airport_names.append(airport_name)

# Écrire les noms des aéroports dans un fichier CSV
csv_file_path = 'Airport name Salomon Islands.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Airport Name'])  # Écrire l'entête
    for name in airport_names:
        writer.writerow([name])

print(f"Les noms des aéroports ont été enregistrés dans {csv_file_path}.")
