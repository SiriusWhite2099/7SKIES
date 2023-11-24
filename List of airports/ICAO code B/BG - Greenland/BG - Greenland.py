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
<td>BGAA</td>
<td>JEG</td>
<td><a href="/wiki/Aasiaat_Airport" title="Aasiaat Airport">Aasiaat Airport</a></td>
<td><a href="/w/index.php?title=Aasiaat_(Egedesminde,_Ausiat)&amp;action=edit&amp;redlink=1" class="new" title="Aasiaat (Egedesminde, Ausiat) (page does not exist)">Aasiaat (Egedesminde, Ausiat)</a>
</td></tr>
<tr>
<td>BGAG</td>
<td>AOQ</td>
<td><a href="/wiki/Aappilattoq_Heliport_(Avannaata)" title="Aappilattoq Heliport (Avannaata)">Aappilattoq Heliport (Avannaata)</a></td>
<td><a href="/wiki/Aappilattoq,_Avannaata" title="Aappilattoq, Avannaata">Aappilattoq, Avannaata</a>
</td></tr>
<tr>
<td>BGAK</td>
<td></td>
<td><a href="/wiki/Akunnaaq_Heliport" title="Akunnaaq Heliport">Akunnaaq Heliport</a></td>
<td><a href="/wiki/Akunnaaq" title="Akunnaaq">Akunnaaq</a>
</td></tr>
<tr>
<td>BGAM</td>
<td>AGM</td>
<td><a href="/wiki/Tasiilaq_Heliport" title="Tasiilaq Heliport">Tasiilaq Heliport</a></td>
<td><a href="/w/index.php?title=Tasiilaq_(Ammassalik,_Angmagssalik)&amp;action=edit&amp;redlink=1" class="new" title="Tasiilaq (Ammassalik, Angmagssalik) (page does not exist)">Tasiilaq (Ammassalik, Angmagssalik)</a>
</td></tr>
<tr>
<td>BGAP</td>
<td>LLU</td>
<td><a href="/wiki/Alluitsup_Paa_Heliport" title="Alluitsup Paa Heliport">Alluitsup Paa Heliport</a></td>
<td><a href="/wiki/Alluitsup_Paa" title="Alluitsup Paa">Alluitsup Paa</a>
</td></tr>
<tr>
<td>BGAQ</td>
<td>QUV</td>
<td><a href="/wiki/Aappilattoq_Heliport_(Kujalleq)" title="Aappilattoq Heliport (Kujalleq)">Aappilattoq Heliport (Kujalleq)</a></td>
<td><a href="/wiki/Aappilattoq,_Kujalleq" title="Aappilattoq, Kujalleq">Aappilattoq, Kujalleq</a>
</td></tr>
<tr>
<td>BGAR</td>
<td>JRK</td>
<td><a href="/wiki/Arsuk_Heliport" title="Arsuk Heliport">Arsuk Heliport</a></td>
<td><a href="/wiki/Arsuk" title="Arsuk">Arsuk</a>
</td></tr>
<tr>
<td>BGAS</td>
<td>QUW</td>
<td><a href="/wiki/Ammassivik_Heliport" title="Ammassivik Heliport">Ammassivik Heliport</a></td>
<td><a href="/wiki/Ammassivik" title="Ammassivik">Ammassivik</a>
</td></tr>
<tr>
<td>BGAT</td>
<td>QGQ</td>
<td><a href="/wiki/Attu_Heliport" title="Attu Heliport">Attu Heliport</a></td>
<td><a href="/wiki/Attu_(Greenland)" class="mw-redirect" title="Attu (Greenland)">Attu</a>
</td></tr>
<tr>
<td>BGBW</td>
<td>UAK</td>
<td><a href="/wiki/Narsarsuaq_Airport" title="Narsarsuaq Airport">Narsarsuaq Airport</a></td>
<td><a href="/w/index.php?title=Narsarsuaq_(Narssarssuaq)&amp;action=edit&amp;redlink=1" class="new" title="Narsarsuaq (Narssarssuaq) (page does not exist)">Narsarsuaq (Narssarssuaq)</a>
</td></tr>
<tr>
<td>BGCH</td>
<td>JCH</td>
<td><a href="/w/index.php?title=Qasigiannguit_Heliport_(Christiansh%C3%A5b_Heliport)&amp;action=edit&amp;redlink=1" class="new" title="Qasigiannguit Heliport (Christianshåb Heliport) (page does not exist)">Qasigiannguit Heliport (Christianshåb Heliport)</a></td>
<td><a href="/w/index.php?title=Qasigiannguit_(Christiansh%C3%A5b)&amp;action=edit&amp;redlink=1" class="new" title="Qasigiannguit (Christianshåb) (page does not exist)">Qasigiannguit (Christianshåb)</a>
</td></tr>
<tr>
<td>BGCO</td>
<td>CNP</td>
<td><a href="/w/index.php?title=Nerlerit_Inaat_Airport_(Constable_Pynt_Airport)&amp;action=edit&amp;redlink=1" class="new" title="Nerlerit Inaat Airport (Constable Pynt Airport) (page does not exist)">Nerlerit Inaat Airport (Constable Pynt Airport)</a></td>
<td><a href="/wiki/Jameson_Land" title="Jameson Land">Jameson Land</a>
</td></tr>
<tr>
<td>BGEM</td>
<td></td>
<td>(see BGAA)</td>
<td>–
</td></tr>
<tr>
<td>BGET</td>
<td>QFG</td>
<td><a href="/wiki/Eqalugaarsuit_Heliport" title="Eqalugaarsuit Heliport">Eqalugaarsuit Heliport</a></td>
<td><a href="/wiki/Eqalugaarsuit" title="Eqalugaarsuit">Eqalugaarsuit</a>
</td></tr>
<tr>
<td>BGFD</td>
<td>QFN</td>
<td><a href="/wiki/Narsaq_Kujalleq_Heliport" title="Narsaq Kujalleq Heliport">Narsaq Kujalleq Heliport</a></td>
<td><a href="/wiki/Narsaq_Kujalleq" class="mw-redirect" title="Narsaq Kujalleq">Narsaq Kujalleq</a>
</td></tr>
<tr>
<td>BGFH</td>
<td></td>
<td>(see BGPT)</td>
<td>–
</td></tr>
<tr>
<td>BGGD</td>
<td>JGR</td>
<td><a href="/w/index.php?title=Kangilinnguit_Heliport_(Gr%C3%B8nnedal_Heliport)&amp;action=edit&amp;redlink=1" class="new" title="Kangilinnguit Heliport (Grønnedal Heliport) (page does not exist)">Kangilinnguit Heliport (Grønnedal Heliport)</a></td>
<td><a href="/w/index.php?title=Kangilinnguit_(Gr%C3%B8nnedal)&amp;action=edit&amp;redlink=1" class="new" title="Kangilinnguit (Grønnedal) (page does not exist)">Kangilinnguit (Grønnedal)</a>
</td></tr>
<tr>
<td>BGGH</td>
<td>GOH</td>
<td><a href="/wiki/Nuuk_Airport" title="Nuuk Airport">Nuuk Airport</a></td>
<td><a href="/w/index.php?title=Nuuk_(Godth%C3%A5b)&amp;action=edit&amp;redlink=1" class="new" title="Nuuk (Godthåb) (page does not exist)">Nuuk (Godthåb)</a>
</td></tr>
<tr>
<td>BGGN</td>
<td>JGO</td>
<td><a href="/w/index.php?title=Qeqertarsuaq_Heliport_(Godhavn_Heliport)&amp;action=edit&amp;redlink=1" class="new" title="Qeqertarsuaq Heliport (Godhavn Heliport) (page does not exist)">Qeqertarsuaq Heliport (Godhavn Heliport)</a></td>
<td><a href="/w/index.php?title=Qeqertarsuaq_(Godhavn)&amp;action=edit&amp;redlink=1" class="new" title="Qeqertarsuaq (Godhavn) (page does not exist)">Qeqertarsuaq (Godhavn)</a>
</td></tr>
<tr>
<td>BGHB</td>
<td></td>
<td>(see BGSS)</td>
<td>–
</td></tr>
<tr>
<td>BGIA</td>
<td>IKE</td>
<td><a href="/wiki/Ikerasak_Heliport" title="Ikerasak Heliport">Ikerasak Heliport</a></td>
<td><a href="/wiki/Ikerasak" title="Ikerasak">Ikerasak</a>
</td></tr>
<tr>
<td>BGIG</td>
<td></td>
<td><a href="/wiki/Iginniarfik_Heliport" title="Iginniarfik Heliport">Iginniarfik Heliport</a></td>
<td><a href="/wiki/Iginniarfik" title="Iginniarfik">Iginniarfik</a>
</td></tr>
<tr>
<td>BGIK</td>
<td>QRY</td>
<td><a href="/wiki/Ikerasaarsuk_Heliport" title="Ikerasaarsuk Heliport">Ikerasaarsuk Heliport</a></td>
<td><a href="/wiki/Ikerasaarsuk" title="Ikerasaarsuk">Ikerasaarsuk</a>
</td></tr>
<tr>
<td>BGIL</td>
<td></td>
<td><a href="/wiki/Ilimanaq_Heliport" title="Ilimanaq Heliport">Ilimanaq Heliport</a></td>
<td><a href="/wiki/Ilimanaq" title="Ilimanaq">Ilimanaq</a>
</td></tr>
<tr>
<td>BGIN</td>
<td>IUI</td>
<td><a href="/wiki/Innaarsuit_Heliport" title="Innaarsuit Heliport">Innaarsuit Heliport</a></td>
<td><a href="/wiki/Innarsuit" class="mw-redirect" title="Innarsuit">Innarsuit</a>
</td></tr>
<tr>
<td>BGIS</td>
<td>IOQ</td>
<td><a href="/wiki/Isortoq_Heliport" title="Isortoq Heliport">Isortoq Heliport</a></td>
<td><a href="/wiki/Isortoq" class="mw-redirect" title="Isortoq">Isortoq</a>
</td></tr>
<tr>
<td>BGIT</td>
<td>QJI</td>
<td><a href="/wiki/Ikamiut_Heliport" title="Ikamiut Heliport">Ikamiut Heliport</a></td>
<td><a href="/wiki/Ikamiut" title="Ikamiut">Ikamiut</a>
</td></tr>
<tr>
<td>BGJH</td>
<td>JJU</td>
<td><a href="/w/index.php?title=Qaqortoq_Heliport_(Julianehab_Heliport)&amp;action=edit&amp;redlink=1" class="new" title="Qaqortoq Heliport (Julianehab Heliport) (page does not exist)">Qaqortoq Heliport (Julianehab Heliport)</a></td>
<td><a href="/w/index.php?title=Qaqortoq_(Julianehab)&amp;action=edit&amp;redlink=1" class="new" title="Qaqortoq (Julianehab) (page does not exist)">Qaqortoq (Julianehab)</a>
</td></tr>
<tr>
<td>BGJN</td>
<td>JAV</td>
<td><a href="/w/index.php?title=Ilulissat_Airport_(Jakobshavn_Airport)&amp;action=edit&amp;redlink=1" class="new" title="Ilulissat Airport (Jakobshavn Airport) (page does not exist)">Ilulissat Airport (Jakobshavn Airport)</a></td>
<td><a href="/w/index.php?title=Ilulissat_(Jakobshavn)&amp;action=edit&amp;redlink=1" class="new" title="Ilulissat (Jakobshavn) (page does not exist)">Ilulissat (Jakobshavn)</a>
</td></tr>
<tr>
<td>BGKA</td>
<td></td>
<td><a href="/wiki/Kangaatsiaq_Heliport" title="Kangaatsiaq Heliport">Kangaatsiaq Heliport</a></td>
<td><a href="/wiki/Kangaatsiaq" title="Kangaatsiaq">Kangaatsiaq</a>
</td></tr>
<tr>
<td>BGKK</td>
<td>KUS</td>
<td><a href="/wiki/Kulusuk_Airport" title="Kulusuk Airport">Kulusuk Airport</a></td>
<td><a href="/wiki/Kulusuk" title="Kulusuk">Kulusuk</a>
</td></tr>
<tr>
<td>BGKL</td>
<td></td>
<td><a href="/wiki/Upernavik_Kujalleq_Heliport" title="Upernavik Kujalleq Heliport">Upernavik Kujalleq Heliport</a></td>
<td><a href="/wiki/Upernavik_Kujalleq" title="Upernavik Kujalleq">Upernavik Kujalleq</a>
</td></tr>
<tr>
<td>BGKM</td>
<td>KUZ</td>
<td><a href="/wiki/Kuummiit_Heliport" title="Kuummiit Heliport">Kuummiit Heliport</a></td>
<td><a href="/wiki/Kuummiit" title="Kuummiit">Kuummiit</a>
</td></tr>
<tr>
<td>BGKQ</td>
<td>KHQ</td>
<td><a href="/wiki/Kullorsuaq_Heliport" title="Kullorsuaq Heliport">Kullorsuaq Heliport</a></td>
<td><a href="/wiki/Kullorsuaq" title="Kullorsuaq">Kullorsuaq</a>
</td></tr>
<tr>
<td>BGKS</td>
<td>KGQ</td>
<td><a href="/wiki/Kangersuatsiaq_Heliport" title="Kangersuatsiaq Heliport">Kangersuatsiaq Heliport</a></td>
<td><a href="/wiki/Kangersuatsiaq" title="Kangersuatsiaq">Kangersuatsiaq</a>
</td></tr>
<tr>
<td>BGKT</td>
<td>QJE</td>
<td><a href="/wiki/Kitsissuarsuit_Heliport" title="Kitsissuarsuit Heliport">Kitsissuarsuit Heliport</a></td>
<td><a href="/wiki/Kitsissuarsuit" title="Kitsissuarsuit">Kitsissuarsuit</a>
</td></tr>
<tr>
<td>BGLL</td>
<td>IOT</td>
<td><a href="/wiki/Illorsuit_Heliport" title="Illorsuit Heliport">Illorsuit Heliport</a></td>
<td><a href="/wiki/Illorsuit" title="Illorsuit">Illorsuit</a>
</td></tr>
<tr>
<td>BGMO</td>
<td></td>
<td><a href="/wiki/Moriussaq_Heliport" class="mw-redirect" title="Moriussaq Heliport">Moriussaq Heliport</a></td>
<td><a href="/wiki/Moriusaq" title="Moriusaq">Moriusaq</a>
</td></tr>
<tr>
<td>BGMQ</td>
<td>JSU</td>
<td><a href="/wiki/Maniitsoq_Airport" title="Maniitsoq Airport">Maniitsoq Airport</a></td>
<td><a href="/w/index.php?title=Maniitsoq_(Sukkertoppen)&amp;action=edit&amp;redlink=1" class="new" title="Maniitsoq (Sukkertoppen) (page does not exist)">Maniitsoq (Sukkertoppen)</a>
</td></tr>
<tr>
<td>BGNK</td>
<td>QMK</td>
<td><a href="/wiki/Niaqornaarsuk_Heliport" title="Niaqornaarsuk Heliport">Niaqornaarsuk Heliport</a></td>
<td><a href="/wiki/Niaqornaarsuk" title="Niaqornaarsuk">Niaqornaarsuk</a>
</td></tr>
<tr>
<td>BGNL</td>
<td></td>
<td><a href="/w/index.php?title=Nalunaq_Heliport&amp;action=edit&amp;redlink=1" class="new" title="Nalunaq Heliport (page does not exist)">Nalunaq Heliport</a></td>
<td><a href="/w/index.php?title=Nalunaq&amp;action=edit&amp;redlink=1" class="new" title="Nalunaq (page does not exist)">Nalunaq</a>
</td></tr>
<tr>
<td>BGNN</td>
<td>JNN</td>
<td><a href="/wiki/Nanortalik_Heliport" title="Nanortalik Heliport">Nanortalik Heliport</a></td>
<td><a href="/wiki/Nanortalik" title="Nanortalik">Nanortalik</a>
</td></tr>
<tr>
<td>BGNQ</td>
<td>JUU</td>
<td><a href="/wiki/Nuugaatsiaq_Heliport" title="Nuugaatsiaq Heliport">Nuugaatsiaq Heliport</a></td>
<td><a href="/wiki/Nuugaatsiaq" title="Nuugaatsiaq">Nuugaatsiaq</a>
</td></tr>
<tr>
<td>BGNS</td>
<td>JNS</td>
<td><a href="/wiki/Narsaq_Heliport" title="Narsaq Heliport">Narsaq Heliport</a></td>
<td><a href="/wiki/Narsaq" title="Narsaq">Narsaq</a>
</td></tr>
<tr>
<td>BGNT</td>
<td>NIQ</td>
<td><a href="/wiki/Niaqornat_Heliport" title="Niaqornat Heliport">Niaqornat Heliport</a></td>
<td><a href="/wiki/Niaqornat" title="Niaqornat">Niaqornat</a>
</td></tr>
<tr>
<td>BGNU</td>
<td>NSQ</td>
<td><a href="/wiki/Nuussuaq_Heliport" title="Nuussuaq Heliport">Nuussuaq Heliport</a></td>
<td><a href="/wiki/Nuussuaq" title="Nuussuaq">Nuussuaq</a>
</td></tr>
<tr>
<td>BGPT</td>
<td>JFR</td>
<td><a href="/wiki/Paamiut_Airport" title="Paamiut Airport">Paamiut Airport</a></td>
<td><a href="/w/index.php?title=Paamiut_(Frederiksh%C3%A5b)&amp;action=edit&amp;redlink=1" class="new" title="Paamiut (Frederikshåb) (page does not exist)">Paamiut (Frederikshåb)</a>
</td></tr>
<tr>
<td>BGQA</td>
<td></td>
<td>(see BGQQ)</td>
<td>–
</td></tr>
<tr>
<td>BGQE</td>
<td>PQT</td>
<td><a href="/wiki/Qeqertaq_Heliport" title="Qeqertaq Heliport">Qeqertaq Heliport</a></td>
<td><a href="/wiki/Qeqertaq" title="Qeqertaq">Qeqertaq</a>
</td></tr>
<tr>
<td>BGQQ</td>
<td>NAQ</td>
<td><a href="/wiki/Qaanaaq_Airport" title="Qaanaaq Airport">Qaanaaq Airport</a></td>
<td><a href="/wiki/Qaanaaq" title="Qaanaaq">Qaanaaq</a>
</td></tr>
<tr>
<td>BGQT</td>
<td>QJH</td>
<td><a href="/wiki/Qassimiut_Heliport" title="Qassimiut Heliport">Qassimiut Heliport</a></td>
<td><a href="/wiki/Qassimiut" title="Qassimiut">Qassimiut</a>
</td></tr>
<tr>
<td>BGSC</td>
<td>OBY</td>
<td><a href="/w/index.php?title=Ittoqqortoormiit_Heliport_(Scoresbysund_Heliport)&amp;action=edit&amp;redlink=1" class="new" title="Ittoqqortoormiit Heliport (Scoresbysund Heliport) (page does not exist)">Ittoqqortoormiit Heliport (Scoresbysund Heliport)</a></td>
<td><a href="/w/index.php?title=Ittoqqortoormiit_(Scoresbysund)&amp;action=edit&amp;redlink=1" class="new" title="Ittoqqortoormiit (Scoresbysund) (page does not exist)">Ittoqqortoormiit (Scoresbysund)</a>
</td></tr>
<tr>
<td>BGSF</td>
<td>SFJ</td>
<td><a href="/w/index.php?title=Kangerlussuaq_Airport_(S%C3%B8ndre_Str%C3%B8mfjord_Airport)&amp;action=edit&amp;redlink=1" class="new" title="Kangerlussuaq Airport (Søndre Strømfjord Airport) (page does not exist)">Kangerlussuaq Airport (Søndre Strømfjord Airport)</a></td>
<td><a href="/w/index.php?title=Kangerlussuaq_(S%C3%B8ndre_Str%C3%B8mfjord)&amp;action=edit&amp;redlink=1" class="new" title="Kangerlussuaq (Søndre Strømfjord) (page does not exist)">Kangerlussuaq (Søndre Strømfjord)</a>
</td></tr>
<tr>
<td>BGSG</td>
<td>SGG</td>
<td><a href="/wiki/Sermiligaaq_Heliport" title="Sermiligaaq Heliport">Sermiligaaq Heliport</a></td>
<td><a href="/wiki/Sermiligaaq" title="Sermiligaaq">Sermiligaaq</a>
</td></tr>
<tr>
<td>BGSI</td>
<td>SRK</td>
<td><a href="/wiki/Siorapaluk_Heliport" title="Siorapaluk Heliport">Siorapaluk Heliport</a></td>
<td><a href="/wiki/Siorapaluk" title="Siorapaluk">Siorapaluk</a>
</td></tr>
<tr>
<td>BGSO</td>
<td>QOQ</td>
<td><a href="/wiki/Saarloq_Heliport" title="Saarloq Heliport">Saarloq Heliport</a></td>
<td><a href="/wiki/Saarloq" title="Saarloq">Saarloq</a>
</td></tr>
<tr>
<td>BGSQ</td>
<td></td>
<td><a href="/wiki/Saqqaq_Heliport" title="Saqqaq Heliport">Saqqaq Heliport</a></td>
<td><a href="/wiki/Saqqaq" title="Saqqaq">Saqqaq</a>
</td></tr>
<tr>
<td>BGSS</td>
<td>JHS</td>
<td><a href="/w/index.php?title=Sisimiut_Airport_(Holsteinsborg_Airport)&amp;action=edit&amp;redlink=1" class="new" title="Sisimiut Airport (Holsteinsborg Airport) (page does not exist)">Sisimiut Airport (Holsteinsborg Airport)</a></td>
<td><a href="/w/index.php?title=Sisimiut_(Holsteinsborg)&amp;action=edit&amp;redlink=1" class="new" title="Sisimiut (Holsteinsborg) (page does not exist)">Sisimiut (Holsteinsborg)</a>
</td></tr>
<tr>
<td>BGST</td>
<td>SAE</td>
<td><a href="/wiki/Saattut_Heliport" title="Saattut Heliport">Saattut Heliport</a></td>
<td><a href="/wiki/Saattut" title="Saattut">Saattut</a>
</td></tr>
<tr>
<td>BGSV</td>
<td>SVR</td>
<td><a href="/wiki/Savissivik_Heliport" title="Savissivik Heliport">Savissivik Heliport</a></td>
<td><a href="/wiki/Savissivik" title="Savissivik">Savissivik</a>
</td></tr>
<tr>
<td>BGTA</td>
<td>TQA</td>
<td><a href="/wiki/Tasiusaq_Heliport_(Avannaata)" title="Tasiusaq Heliport (Avannaata)">Tasiusaq Heliport (Avannaata)</a></td>
<td><a href="/wiki/Tasiusaq,_Avannaata" title="Tasiusaq, Avannaata">Tasiusaq, Avannaata</a>
</td></tr>
<tr>
<td>BGTL</td>
<td>THU</td>
<td><a href="/wiki/Pituffik_Space_Base" title="Pituffik Space Base">Pituffik Space Base</a></td>
<td><a href="/w/index.php?title=Pituffik,_Qaanaaq&amp;action=edit&amp;redlink=1" class="new" title="Pituffik, Qaanaaq (page does not exist)">Pituffik, Qaanaaq</a>
</td></tr>
<tr>
<td>BGTN</td>
<td>TQI</td>
<td><a href="/wiki/Tiniteqilaaq_Heliport" title="Tiniteqilaaq Heliport">Tiniteqilaaq Heliport</a></td>
<td><a href="/wiki/Tiniteqilaaq" class="mw-redirect" title="Tiniteqilaaq">Tiniteqilaaq</a>
</td></tr>
<tr>
<td>BGTQ</td>
<td>XEQ</td>
<td><a href="/wiki/Tasiusaq_Heliport_(Kujalleq)" title="Tasiusaq Heliport (Kujalleq)">Tasiusaq Heliport (Kujalleq)</a></td>
<td><a href="/wiki/Tasiusaq,_Kujalleq" title="Tasiusaq, Kujalleq">Tasiusaq, Kujalleq</a>
</td></tr>
<tr>
<td>BGUK</td>
<td>JUV</td>
<td><a href="/wiki/Upernavik_Airport" title="Upernavik Airport">Upernavik Airport</a></td>
<td><a href="/wiki/Upernavik" title="Upernavik">Upernavik</a>
</td></tr>
<tr>
<td>BGUM</td>
<td>UMD</td>
<td><a href="/wiki/Uummannaq_Heliport" title="Uummannaq Heliport">Uummannaq Heliport</a></td>
<td><a href="/wiki/Uummannaq" title="Uummannaq">Uummannaq</a>
</td></tr>
<tr>
<td>BGUQ</td>
<td>JQA</td>
<td><a href="/wiki/Qaarsut_Airport" title="Qaarsut Airport">Qaarsut Airport</a></td>
<td><a href="/wiki/Qaarsut" title="Qaarsut">Qaarsut</a>
</td></tr>
<tr>
<td>BGUT</td>
<td>JUK</td>
<td><a href="/wiki/Ukkusissat_Heliport" title="Ukkusissat Heliport">Ukkusissat Heliport</a></td>
<td><a href="/w/index.php?title=Ukkusisst&amp;action=edit&amp;redlink=1" class="new" title="Ukkusisst (page does not exist)">Ukkusisst</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

# Trouver la table dans le HTML
table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

# Ouvrir un fichier CSV pour écrire
with open('BG - Greenland.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    # Définir les noms de colonnes pour le fichier CSV
    fieldnames = ['ICAO', 'IATA', 'Airport Name', 'Community']
    # Créer un objet writer pour écrire dans le fichier CSV
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Écrire les noms de colonnes dans le fichier CSV
    writer.writeheader()

    # Trouver toutes les lignes de la table
    rows = table.find_all('tr')

    # Parcourir chaque ligne et écrire les données dans le fichier CSV
    for row in rows[1:]:  # Ignorer la première ligne car c'est l'en-tête
        columns = row.find_all('td')
        icao = columns[0].text.strip()
        iata = columns[1].text.strip()
        airport_name = columns[2].text.strip()
        community = columns[3].text.strip()

        # Écrire les données dans le fichier CSV
        writer.writerow({'ICAO': icao, 'IATA': iata, 'Airport Name': airport_name, 'Community': community})

print("Le fichier CSV a été créé avec succès.")

