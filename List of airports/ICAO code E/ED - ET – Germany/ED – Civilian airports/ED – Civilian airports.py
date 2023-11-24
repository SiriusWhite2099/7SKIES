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
<td>EDAC</td>
<td>AOC</td>
<td><a href="/wiki/Leipzig-Altenburg_Airport" class="mw-redirect" title="Leipzig-Altenburg Airport">Leipzig-Altenburg Airport</a></td>
<td><a href="/wiki/Altenburg" title="Altenburg">Altenburg</a>/<a href="/wiki/Leipzig" title="Leipzig">Leipzig</a>
</td></tr>
<tr>
<td>EDAD</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Dessau&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Dessau (page does not exist)">Flugplatz Dessau</a></td>
<td><a href="/wiki/Dessau" title="Dessau">Dessau</a>
</td></tr>
<tr>
<td>EDAH</td>
<td></td>
<td><a href="/wiki/Heringsdorf_Airport" title="Heringsdorf Airport">Heringsdorf Airport</a> (Flugplatz Heringsdorf)</td>
<td><a href="/wiki/Heringsdorf" title="Heringsdorf">Heringsdorf</a>
</td></tr>
<tr>
<td>EDAP</td>
<td></td>
<td><a href="/wiki/Cottbus-Neuhausen_Airport" title="Cottbus-Neuhausen Airport">Cottbus-Neuhausen Airport</a></td>
<td><a href="/wiki/Cottbus" title="Cottbus">Cottbus</a>
</td></tr>
<tr>
<td>EDAV</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Finow&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Finow (page does not exist)">Flugplatz Finow</a></td>
<td><a href="/wiki/Finow" title="Finow">Finow</a>
</td></tr>
<tr>
<td>EDAX</td>
<td></td>
<td><a href="/wiki/Rechlin-L%C3%A4rz_Airfield" class="mw-redirect" title="Rechlin-Lärz Airfield">Rechlin-Lärz Airfield</a></td>
<td><a href="/wiki/Rechlin" title="Rechlin">Rechlin</a>
</td></tr>
<tr>
<td>EDAY</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Strausberg&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Strausberg (page does not exist)">Flugplatz Strausberg</a></td>
<td><a href="/wiki/Strausberg" title="Strausberg">Strausberg</a></td>
<td><a href="/wiki/Brandenburg" title="Brandenburg">Brandenburg</a>
</td></tr>
<tr>
<td>EDAZ</td>
<td></td>
<td><a href="/wiki/Sch%C3%B6nhagen_Airport" title="Schönhagen Airport">Schönhagen Airport</a></td>
<td><a href="/wiki/Trebbin" title="Trebbin">Trebbin</a></td>
<td><a href="/wiki/Brandenburg" title="Brandenburg">Brandenburg</a>
</td></tr>
<tr>
<td>EDBC</td>
<td>CSO</td>
<td><a href="/wiki/Magdeburg%E2%80%93Cochstedt_Airport" title="Magdeburg–Cochstedt Airport">Magdeburg–Cochstedt Airport</a></td>
<td><a href="/wiki/Magdeburg" title="Magdeburg">Magdeburg</a>
</td></tr>
<tr>
<td><s>EDBG</s></td>
<td><s>GWW</s></td>
<td><s><a href="/wiki/RAF_Gatow" title="RAF Gatow">Gatow Airfield</a></s></td>
<td><a href="/wiki/Gatow" title="Gatow">Berlin-Gatow</a></td>
<td></td>
<td>closed for public traffic in 1994
</td></tr>
<tr>
<td>EDBH</td>
<td>BBH</td>
<td><a href="/wiki/Stralsund-Barth_Airport" class="mw-redirect" title="Stralsund-Barth Airport">Stralsund-Barth Airport</a></td>
<td><a href="/wiki/Barth,_Germany" title="Barth, Germany">Barth</a></td>
<td><a href="/wiki/Mecklenburg-Vorpommern" title="Mecklenburg-Vorpommern">Mecklenburg-Vorpommern</a>
</td></tr>
<tr>
<td>EDBM</td>
<td>ZMG</td>
<td><a href="/w/index.php?title=Magdeburg_City_Airport&amp;action=edit&amp;redlink=1" class="new" title="Magdeburg City Airport (page does not exist)">Magdeburg City Airport</a></td>
<td><a href="/wiki/Magdeburg" title="Magdeburg">Magdeburg</a>
</td></tr>
<tr>
<td>EDBN</td>
<td>FNB</td>
<td><a href="/wiki/Neubrandenburg_Airport" title="Neubrandenburg Airport">Neubrandenburg Airport</a></td>
<td><a href="/wiki/Neubrandenburg" title="Neubrandenburg">Neubrandenburg</a>
</td></tr>
<tr>
<td>EDBS</td>
<td></td>
<td><a href="/wiki/Flugplatz_S%C3%B6mmerda-Dermsdorf" title="Flugplatz Sömmerda-Dermsdorf">Sömmerda-Dermsdorf Airport</a></td>
<td><a href="/wiki/S%C3%B6mmerda" title="Sömmerda">Sömmerda</a>
</td></tr>
<tr>
<td>EDCA</td>
<td></td>
<td><a href="/w/index.php?title=Anklam_Airport&amp;action=edit&amp;redlink=1" class="new" title="Anklam Airport (page does not exist)">Anklam Airport</a></td>
<td><a href="/wiki/Anklam" title="Anklam">Anklam</a>
</td></tr>
<tr>
<td><s>EDCD</s></td>
<td><s>CBU</s></td>
<td><s><a href="/wiki/Cottbus-Drewitz_Airport" title="Cottbus-Drewitz Airport">Cottbus-Drewitz Airport</a></s></td>
<td><a href="/wiki/Cottbus" title="Cottbus">Cottbus</a></td>
<td></td>
<td>closed in 2020
</td></tr>
<tr>
<td>EDCG</td>
<td></td>
<td><a href="/wiki/R%C3%BCgen_Airport" title="Rügen Airport">Rügen Airport</a> (Bergen Airfield/Güttin Airfield)</td>
<td><a href="/wiki/R%C3%BCgen" title="Rügen">Rügen</a>
</td></tr>
<tr>
<td>EDCI</td>
<td></td>
<td><a href="/wiki/Klix_Airfield" title="Klix Airfield">Klix Airfield</a></td>
<td><a href="/wiki/Bautzen" title="Bautzen">Bautzen</a>
</td></tr>
<tr>
<td>EDCP</td>
<td></td>
<td><a href="/wiki/Peenem%C3%BCnde_Airfield" title="Peenemünde Airfield">Peenemünde Airfield</a></td>
<td><a href="/wiki/Peenem%C3%BCnde" title="Peenemünde">Peenemünde</a>
</td></tr>
<tr>
<td>EDDB</td>
<td>BER</td>
<td><a href="/wiki/Berlin_Brandenburg_Airport" title="Berlin Brandenburg Airport">Berlin Brandenburg Airport</a></td>
<td><a href="/wiki/Berlin" title="Berlin">Berlin</a></td>
<td></td>
<td>prior to opening in 2020, its code was designated for <a href="/wiki/Berlin_Sch%C3%B6nefeld_Airport" title="Berlin Schönefeld Airport">Berlin Schönefeld Airport</a> with IATA airport code <s>SXF</s>
</td></tr>
<tr>
<td>EDDC</td>
<td>DRS</td>
<td><a href="/wiki/Dresden_Airport" title="Dresden Airport">Dresden Airport</a> (Dresden-Klotzsche Airport)</td>
<td><a href="/wiki/Dresden" title="Dresden">Dresden</a>
</td></tr>
<tr>
<td>EDDE</td>
<td>ERF</td>
<td><a href="/wiki/Erfurt%E2%80%93Weimar_Airport" title="Erfurt–Weimar Airport">Erfurt–Weimar Airport</a></td>
<td><a href="/wiki/Erfurt" title="Erfurt">Erfurt</a>
</td></tr>
<tr>
<td>EDDF</td>
<td>FRA</td>
<td><a href="/wiki/Frankfurt_International_Airport" class="mw-redirect" title="Frankfurt International Airport">Frankfurt International Airport</a></td>
<td><a href="/wiki/Frankfurt_am_Main" class="mw-redirect" title="Frankfurt am Main">Frankfurt am Main</a>
</td></tr>
<tr>
<td>EDDG</td>
<td>FMO</td>
<td><a href="/wiki/M%C3%BCnster_Osnabr%C3%BCck_Airport" title="Münster Osnabrück Airport">Münster Osnabrück Airport</a></td>
<td><a href="/wiki/Greven" title="Greven">Greven</a>
</td></tr>
<tr>
<td>EDDH</td>
<td>HAM</td>
<td><a href="/wiki/Hamburg_Airport" title="Hamburg Airport">Hamburg Airport</a></td>
<td><a href="/wiki/Hamburg" title="Hamburg">Hamburg</a>
</td></tr>
<tr>
<td><s>EDDI</s></td>
<td><s>THF</s></td>
<td><s><a href="/wiki/Tempelhof_International_Airport" class="mw-redirect" title="Tempelhof International Airport">Tempelhof International Airport</a></s></td>
<td><a href="/wiki/Berlin" title="Berlin">Berlin</a></td>
<td></td>
<td>closed in 2008
</td></tr>
<tr>
<td>EDDK</td>
<td>CGN</td>
<td><a href="/wiki/Cologne_Bonn_Airport" title="Cologne Bonn Airport">Cologne Bonn Airport</a></td>
<td><a href="/wiki/Cologne" title="Cologne">Cologne</a>/<a href="/wiki/Bonn" title="Bonn">Bonn</a>
</td></tr>
<tr>
<td>EDDL</td>
<td>DUS</td>
<td><a href="/wiki/D%C3%BCsseldorf_Airport" title="Düsseldorf Airport">Düsseldorf Airport</a></td>
<td><a href="/wiki/D%C3%BCsseldorf" title="Düsseldorf">Düsseldorf</a>
</td></tr>
<tr>
<td>EDDM</td>
<td>MUC</td>
<td><a href="/wiki/Munich_International_Airport" class="mw-redirect" title="Munich International Airport">Munich International Airport</a> (Franz Josef Strauß International Airport)</td>
<td><a href="/wiki/Munich" title="Munich">Munich</a>
</td></tr>
<tr>
<td>EDDN</td>
<td>NUE</td>
<td><a href="/wiki/Nuremberg_Airport" title="Nuremberg Airport">Nuremberg Airport</a></td>
<td><a href="/wiki/Nuremberg" title="Nuremberg">Nuremberg</a>
</td></tr>
<tr>
<td>EDDP</td>
<td>LEJ</td>
<td><a href="/wiki/Leipzig/Halle_Airport" title="Leipzig/Halle Airport">Leipzig/Halle Airport</a></td>
<td><a href="/wiki/Leipzig" title="Leipzig">Leipzig</a>/<a href="/wiki/Halle,_Saxony-Anhalt" class="mw-redirect" title="Halle, Saxony-Anhalt">Halle</a>
</td></tr>
<tr>
<td>EDDR</td>
<td>SCN</td>
<td><a href="/wiki/Saarbr%C3%BCcken_Airport" title="Saarbrücken Airport">Saarbrücken Airport</a></td>
<td><a href="/wiki/Saarbr%C3%BCcken" title="Saarbrücken">Saarbrücken</a>
</td></tr>
<tr>
<td>EDDS</td>
<td>STR</td>
<td><a href="/wiki/Stuttgart_Airport" title="Stuttgart Airport">Stuttgart Echterdingen Airport</a></td>
<td><a href="/wiki/Stuttgart" title="Stuttgart">Stuttgart</a>
</td></tr>
<tr>
<td><s>EDDT</s></td>
<td><s>TXL</s></td>
<td><s><a href="/wiki/Berlin_Tegel_Airport" title="Berlin Tegel Airport">Tegel International Airport</a></s></td>
<td><a href="/wiki/Berlin" title="Berlin">Berlin</a></td>
<td></td>
<td>closed in 2020
</td></tr>
<tr>
<td>EDDV</td>
<td>HAJ</td>
<td><a href="/wiki/Hanover_Airport" class="mw-redirect" title="Hanover Airport">Hanover Airport</a></td>
<td><a href="/wiki/Hanover" title="Hanover">Hanover</a>
</td></tr>
<tr>
<td>EDDW</td>
<td>BRE</td>
<td><a href="/wiki/Bremen_Airport" title="Bremen Airport">Bremen Airport</a></td>
<td><a href="/wiki/Bremen" title="Bremen">Bremen</a>
</td></tr>
<tr>
<td>EDEB</td>
<td></td>
<td><a href="/wiki/Bad_Langensalza_Airfield" title="Bad Langensalza Airfield">Bad Langensalza Airfield</a></td>
<td><a href="/wiki/Bad_Langensalza" title="Bad Langensalza">Bad Langensalza</a>
</td></tr>
<tr>
<td>EDEH</td>
<td></td>
<td><a href="/w/index.php?title=Sonderlandeplatz_Herrenteich&amp;action=edit&amp;redlink=1" class="new" title="Sonderlandeplatz Herrenteich (page does not exist)">Sonderlandeplatz Herrenteich</a></td>
<td><a href="/wiki/Hockenheim#Geography" title="Hockenheim">Herrenteich</a>
</td></tr>
<tr>
<td>EDER</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Wasserkuppe&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Wasserkuppe (page does not exist)">Flugplatz Wasserkuppe</a></td>
<td><a href="/wiki/Wasserkuppe" title="Wasserkuppe">Wasserkuppe</a>
</td></tr>
<tr>
<td>EDFB</td>
<td></td>
<td><a href="/wiki/Reichelsheim_Airport" title="Reichelsheim Airport">Reichelsheim Airport</a></td>
<td><a href="/wiki/Reichelsheim_(Wetterau)" title="Reichelsheim (Wetterau)">Reichelsheim</a>
</td></tr>
<tr>
<td>EDFC</td>
<td></td>
<td><a href="/w/index.php?title=Aschaffenburg_Airport&amp;action=edit&amp;redlink=1" class="new" title="Aschaffenburg Airport (page does not exist)">Aschaffenburg Airport</a></td>
<td><a href="/wiki/Aschaffenburg" title="Aschaffenburg">Aschaffenburg</a>
</td></tr>
<tr>
<td>EDFE</td>
<td>QEF</td>
<td><a href="/wiki/Frankfurt_Egelsbach_Airport" title="Frankfurt Egelsbach Airport">Frankfurt Egelsbach Airport</a></td>
<td><a href="/wiki/Frankfurt_am_Main" class="mw-redirect" title="Frankfurt am Main">Frankfurt am Main</a>
</td></tr>
<tr>
<td>EDFG</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Gelnhausen&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Gelnhausen (page does not exist)">Flugplatz Gelnhausen</a></td>
<td><a href="/wiki/Gelnhausen" title="Gelnhausen">Gelnhausen</a>
</td></tr>
<tr>
<td>EDFH</td>
<td>HHN</td>
<td><a href="/wiki/Frankfurt-Hahn_Airport" class="mw-redirect" title="Frankfurt-Hahn Airport">Frankfurt-Hahn Airport</a></td>
<td><a href="/wiki/Rhineland-Palatinate" title="Rhineland-Palatinate">Rhineland-Palatinate</a>
</td></tr>
<tr>
<td>EDFK</td>
<td></td>
<td><a href="/wiki/Bad_Kissingen_Airfield" title="Bad Kissingen Airfield">Bad Kissingen Airfield</a></td>
<td><a href="/wiki/Bad_Kissingen" title="Bad Kissingen">Bad Kissingen</a>
</td></tr>
<tr>
<td>EDFM</td>
<td>MHG</td>
<td><a href="/wiki/Mannheim_City_Airport" title="Mannheim City Airport">Mannheim City Airport</a></td>
<td><a href="/wiki/Mannheim" title="Mannheim">Mannheim</a>
</td></tr>
<tr>
<td>EDFQ</td>
<td></td>
<td><a href="/wiki/Allendorf_Airport" title="Allendorf Airport">Allendorf Airport</a></td>
<td><a href="/wiki/Allendorf,_Waldeck-Frankenberg" class="mw-redirect" title="Allendorf, Waldeck-Frankenberg">Allendorf, Waldeck-Frankenberg</a>
</td></tr>
<tr>
<td>EDFT</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Lauterbach&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Lauterbach (page does not exist)">Flugplatz Lauterbach</a></td>
<td><a href="/wiki/Lauterbach,_Hesse" title="Lauterbach, Hesse">Lauterbach</a>
</td></tr>
<tr>
<td>EDFW</td>
<td></td>
<td><a href="/wiki/Airdrome_W%C3%BCrzburg-Schenkenturm" class="mw-redirect" title="Airdrome Würzburg-Schenkenturm">Airdrome Würzburg-Schenkenturm</a></td>
<td><a href="/wiki/W%C3%BCrzburg" title="Würzburg">Würzburg</a>
</td></tr>
<tr>
<td>EDFY</td>
<td></td>
<td><a href="/wiki/Elz,_Hesse#Air_transport" title="Elz, Hesse">Flugplatz Elz</a></td>
<td><a href="/wiki/Elz,_Hesse" title="Elz, Hesse">Elz</a>
</td></tr>
<tr>
<td>EDFZ</td>
<td>QMZ</td>
<td><a href="/wiki/Mainz-Finthen_Airport" class="mw-redirect" title="Mainz-Finthen Airport">Mainz-Finthen</a></td>
<td><a href="/wiki/Mainz" title="Mainz">Mainz</a>
</td></tr>
<tr>
<td>EDGA</td>
<td></td>
<td><a href="/wiki/Westerburg#Economy_and_infrastructure" title="Westerburg">Flugplatz Ailertchen</a></td>
<td><a href="/wiki/Westerburg" title="Westerburg">Westerburg</a>
</td></tr>
<tr>
<td>EDGB</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Breitscheid&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Breitscheid (page does not exist)">Flugplatz Breitscheid</a><span class="noprint" style="font-size:85%; font-style: normal;">&nbsp;[<a href="https://de.wikipedia.org/wiki/Flugplatz_Breitscheid" class="extiw" title="de:Flugplatz Breitscheid">de</a>]</span></td>
<td><a href="/wiki/Breitscheid,_Hesse" title="Breitscheid, Hesse">Breitscheid</a>
</td></tr>
<tr>
<td>EDGE</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Eisenach-Kindel&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Eisenach-Kindel (page does not exist)">Flugplatz Eisenach-Kindel</a></td>
<td><a href="/wiki/H%C3%B6rselberg-Hainich" title="Hörselberg-Hainich">Hörselberg-Hainich</a>
</td></tr>
<tr>
<td>EDGO</td>
<td></td>
<td>Oedheim Heliport</td>
<td><a href="/wiki/Oedheim" title="Oedheim">Oedheim</a>
</td></tr>
<tr>
<td>EDGP</td>
<td></td>
<td><a href="/w/index.php?title=Oppenheim_Airport&amp;action=edit&amp;redlink=1" class="new" title="Oppenheim Airport (page does not exist)">Oppenheim Airport</a></td>
<td><a href="/wiki/Oppenheim" title="Oppenheim">Oppenheim</a>
</td></tr>
<tr>
<td>EDGS</td>
<td>SGE</td>
<td><a href="/wiki/Siegerland_Airport" title="Siegerland Airport">Siegerland Airport</a></td>
<td><a href="/wiki/Burbach,_North_Rhine-Westphalia" title="Burbach, North Rhine-Westphalia">Burbach</a>
</td></tr>
<tr>
<td>EDGX</td>
<td></td>
<td><a href="/w/index.php?title=Sonderlandeplatz_Walldorf&amp;action=edit&amp;redlink=1" class="new" title="Sonderlandeplatz Walldorf (page does not exist)">Sonderlandeplatz Walldorf</a></td>
<td><a href="/wiki/Walldorf" title="Walldorf">Walldorf</a>
</td></tr>
<tr>
<td>EDGY</td>
<td>KZG</td>
<td><a href="/wiki/Kitzingen_Airport" title="Kitzingen Airport">Kitzingen Airport</a></td>
<td><a href="/wiki/Kitzingen" title="Kitzingen">Kitzingen</a>
</td></tr>
<tr>
<td>EDHE</td>
<td></td>
<td><a href="/wiki/Uetersen_Airfield" title="Uetersen Airfield">Uetersen Airfield</a></td>
<td><a href="/wiki/Heist,_Germany" title="Heist, Germany">Heist</a>
</td></tr>
<tr>
<td>EDHG</td>
<td></td>
<td><a href="/w/index.php?title=Sonderlandeplatz_L%C3%BCneburg&amp;action=edit&amp;redlink=1" class="new" title="Sonderlandeplatz Lüneburg (page does not exist)">Sonderlandeplatz Lüneburg</a></td>
<td><a href="/wiki/L%C3%BCneburg" title="Lüneburg">Lüneburg</a>
</td></tr>
<tr>
<td>EDHI</td>
<td>XFW</td>
<td><a href="/wiki/Hamburg_Finkenwerder_Airport" class="mw-redirect" title="Hamburg Finkenwerder Airport">Hamburg Finkenwerder Airport</a></td>
<td><a href="/wiki/Hamburg" title="Hamburg">Hamburg</a>
</td></tr>
<tr>
<td>EDHK</td>
<td>KEL</td>
<td><a href="/wiki/Kiel_Airport" title="Kiel Airport">Kiel Airport</a></td>
<td><a href="/wiki/Kiel" title="Kiel">Kiel</a>
</td></tr>
<tr>
<td>EDHL</td>
<td>LBC</td>
<td><a href="/wiki/L%C3%BCbeck_Airport" title="Lübeck Airport">Lübeck Airport</a></td>
<td><a href="/wiki/L%C3%BCbeck" title="Lübeck">Lübeck</a>
</td></tr>
<tr>
<td>EDHM</td>
<td></td>
<td><a href="/w/index.php?title=Hartenholm_Airport&amp;action=edit&amp;redlink=1" class="new" title="Hartenholm Airport (page does not exist)">Hartenholm Airport</a></td>
<td><a href="/wiki/Hartenholm" title="Hartenholm">Hartenholm</a>
</td></tr>
<tr>
<td>EDHS</td>
<td></td>
<td><a href="/w/index.php?title=Sonderlandeplatz_Stade&amp;action=edit&amp;redlink=1" class="new" title="Sonderlandeplatz Stade (page does not exist)">Sonderlandeplatz Stade</a></td>
<td><a href="/wiki/Stade" title="Stade">Stade</a>
</td></tr>
<tr>
<td>EDJA</td>
<td>FMM</td>
<td><a href="/wiki/Memmingen_Airport" title="Memmingen Airport">Memmingen Airport</a> (Allgäu Airport)</td>
<td><a href="/wiki/Memmingen" title="Memmingen">Memmingen</a>
</td></tr>
<tr>
<td>EDKA</td>
<td>AAH</td>
<td><a href="/wiki/Aachen_Merzbr%C3%BCck_Airfield" title="Aachen Merzbrück Airfield">Aachen Merzbrück Airfield</a></td>
<td><a href="/wiki/Aachen" title="Aachen">Aachen</a>
</td></tr>
<tr>
<td>EDKB</td>
<td></td>
<td><a href="/w/index.php?title=Bonn-Hangelar_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Bonn-Hangelar Airfield (page does not exist)">Bonn-Hangelar Airfield</a></td>
<td><a href="/wiki/Sankt_Augustin" title="Sankt Augustin">Sankt Augustin</a>
</td></tr>
<tr>
<td>EDKL</td>
<td></td>
<td><a href="/w/index.php?title=Leverkusen_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Leverkusen Airfield (page does not exist)">Leverkusen Airfield</a></td>
<td><a href="/wiki/Leverkusen" title="Leverkusen">Leverkusen</a>
</td></tr>
<tr>
<td>EDKU</td>
<td></td>
<td><a href="/wiki/Finnentrop#Economy_and_infrastructure" title="Finnentrop">Attendorn-Finnentrop Aerodrome</a></td>
<td><a href="/wiki/Finnentrop" title="Finnentrop">Finnentrop</a>
</td></tr>
<tr>
<td>EDKV</td>
<td></td>
<td><a href="/wiki/Dahlemer_Binz_Airfield" title="Dahlemer Binz Airfield">Dahlemer Binz Airfield</a></td>
<td><a href="/wiki/Dahlem,_Rhineland-Palatinate" title="Dahlem, Rhineland-Palatinate">Dahlem</a>
</td></tr>
<tr>
<td>EDLB</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Borkenberge&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Borkenberge (page does not exist)">Flugplatz Borkenberge</a></td>
<td><a href="/wiki/L%C3%BCdinghausen" title="Lüdinghausen">Lüdinghausen</a>
</td></tr>
<tr>
<td>EDLC</td>
<td></td>
<td><a href="/w/index.php?title=Kamp-Lintfort_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Kamp-Lintfort Airfield (page does not exist)">Kamp-Lintfort Airfield</a></td>
<td><a href="/wiki/Kamp-Lintfort" title="Kamp-Lintfort">Kamp-Lintfort</a>
</td></tr>
<tr>
<td>EDLD</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Schwarze_Heide&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Schwarze Heide (page does not exist)">Flugplatz Schwarze Heide</a></td>
<td><a href="/wiki/Dinslaken" title="Dinslaken">Dinslaken</a>
</td></tr>
<tr>
<td>EDLE</td>
<td>ESS</td>
<td><a href="/wiki/Essen/M%C3%BClheim_Airport" title="Essen/Mülheim Airport">Essen/Mülheim Airport</a></td>
<td><a href="/wiki/M%C3%BClheim" title="Mülheim">Mülheim</a>
</td></tr>
<tr>
<td>EDLF</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Grefrath-Niershorst&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Grefrath-Niershorst (page does not exist)">Flugplatz Grefrath-Niershorst</a></td>
<td><a href="/wiki/Grefrath" title="Grefrath">Grefrath</a>
</td></tr>
<tr>
<td>EDLG</td>
<td></td>
<td><a href="/w/index.php?title=Goch-Asperden_Airport&amp;action=edit&amp;redlink=1" class="new" title="Goch-Asperden Airport (page does not exist)">Goch-Asperden Airport</a></td>
<td><a href="/wiki/Asperden" title="Asperden">Asperden</a>
</td></tr>
<tr>
<td>EDLK</td>
<td>QKF</td>
<td><a href="/w/index.php?title=Krefeld-Egelsberg_Airport&amp;action=edit&amp;redlink=1" class="new" title="Krefeld-Egelsberg Airport (page does not exist)">Krefeld-Egelsberg Airport</a></td>
<td><a href="/wiki/Krefeld" title="Krefeld">Krefeld</a>
</td></tr>
<tr>
<td>EDLN</td>
<td>MGL</td>
<td><a href="/wiki/D%C3%BCsseldorf-M%C3%B6nchengladbach_Airport" class="mw-redirect" title="Düsseldorf-Mönchengladbach Airport">Düsseldorf-Mönchengladbach Airport</a></td>
<td><a href="/wiki/M%C3%B6nchengladbach" title="Mönchengladbach">Mönchengladbach</a>
</td></tr>
<tr>
<td>EDLO</td>
<td></td>
<td><a href="/wiki/Oerlinghausen_Airfield" title="Oerlinghausen Airfield">Oerlinghausen Airfield</a></td>
<td><a href="/wiki/Oerlinghausen" title="Oerlinghausen">Oerlinghausen</a>
</td></tr>
<tr>
<td>EDLP</td>
<td>PAD</td>
<td><a href="/wiki/Paderborn_Lippstadt_Airport" title="Paderborn Lippstadt Airport">Paderborn Lippstadt Airport</a></td>
<td><a href="/wiki/Paderborn" title="Paderborn">Paderborn</a> / <a href="/wiki/Lippstadt" title="Lippstadt">Lippstadt</a>
</td></tr>
<tr>
<td>EDLR</td>
<td></td>
<td><a href="/wiki/Paderborn#Infrastructure" title="Paderborn">Paderborn-Haxterberg Airfield</a></td>
<td><a href="/wiki/Paderborn" title="Paderborn">Paderborn</a>
</td></tr>
<tr>
<td>EDLS</td>
<td></td>
<td><a href="/wiki/Stadtlohn-Vreden_Airport" title="Stadtlohn-Vreden Airport">Stadtlohn-Vreden Airport</a></td>
<td><a href="/wiki/Stadtlohn" title="Stadtlohn">Stadtlohn</a>
</td></tr>
<tr>
<td>EDLT</td>
<td></td>
<td><a href="/w/index.php?title=Verkehrslandeplatz_M%C3%BCnster-Telgte&amp;action=edit&amp;redlink=1" class="new" title="Verkehrslandeplatz Münster-Telgte (page does not exist)">Verkehrslandeplatz Münster-Telgte</a></td>
<td><a href="/wiki/Telgte" title="Telgte">Telgte</a>
</td></tr>
<tr>
<td>EDLV</td>
<td>NRN</td>
<td><a href="/wiki/Weeze_Airport" title="Weeze Airport">Weeze Airport</a></td>
<td><a href="/wiki/Weeze" title="Weeze">Weeze</a></td>
<td></td>
<td>formerly Niederrhein Airport
</td></tr>
<tr>
<td>EDLW</td>
<td>DTM</td>
<td><a href="/wiki/Dortmund_Airport" title="Dortmund Airport">Dortmund Airport</a></td>
<td><a href="/wiki/Dortmund" title="Dortmund">Dortmund</a>
</td></tr>
<tr>
<td>EDLX</td>
<td></td>
<td><a href="/w/index.php?title=Wesel-R%C3%B6merwardt_Airport&amp;action=edit&amp;redlink=1" class="new" title="Wesel-Römerwardt Airport (page does not exist)">Wesel-Römerwardt Airport</a></td>
<td><a href="/wiki/Wesel" title="Wesel">Wesel</a>
</td></tr>
<tr>
<td>EDLZ</td>
<td></td>
<td><a href="/wiki/Soest-Bad_Sassendorf_Airfield" title="Soest-Bad Sassendorf Airfield">Soest-Bad Sassendorf Airfield</a></td>
<td><a href="/wiki/Soest,_Germany" title="Soest, Germany">Soest</a> / <a href="/wiki/Bad_Sassendorf" title="Bad Sassendorf">Bad Sassendorf</a>
</td></tr>
<tr>
<td>EDMA</td>
<td>AGB</td>
<td><a href="/wiki/Augsburg_Airport" title="Augsburg Airport">Augsburg Airport</a></td>
<td><a href="/wiki/Augsburg" title="Augsburg">Augsburg</a>
</td></tr>
<tr>
<td>EDME</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Eggenfelden&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Eggenfelden (page does not exist)">Flugplatz Eggenfelden</a></td>
<td><a href="/wiki/Pfarrkirchen" title="Pfarrkirchen">Pfarrkirchen</a>
</td></tr>
<tr>
<td>EDMO</td>
<td>OBF</td>
<td>Oberpfaffenhofen Airport</td>
<td><a href="/wiki/Oberpfaffenhofen" title="Oberpfaffenhofen">Oberpfaffenhofen</a>
</td></tr>
<tr>
<td>EDMQ</td>
<td></td>
<td><a href="/w/index.php?title=Donauw%C3%B6rth_Airport&amp;action=edit&amp;redlink=1" class="new" title="Donauwörth Airport (page does not exist)">Donauwörth Airport</a></td>
<td><a href="/wiki/Genderkingen" title="Genderkingen">Genderkingen</a>
</td></tr>
<tr>
<td>EDMS</td>
<td>RBM</td>
<td><a href="/wiki/Straubing_Wallmuhle_Airport" class="mw-redirect" title="Straubing Wallmuhle Airport">Straubing Wallmuhle Airport</a></td>
<td><a href="/wiki/Straubing" title="Straubing">Straubing</a>
</td></tr>
<tr>
<td>EDMT</td>
<td></td>
<td>Flugplatz Tannheim</td>
<td><a href="/wiki/Tannheim" title="Tannheim">Tannheim</a>
</td></tr>
<tr>
<td>EDMV</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Vilshofen&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Vilshofen (page does not exist)">Flugplatz Vilshofen</a></td>
<td><a href="/wiki/Vilshofen_an_der_Donau" title="Vilshofen an der Donau">Vilshofen an der Donau</a>
</td></tr>
<tr>
<td>EDNR</td>
<td></td>
<td><a href="https://de.wikipedia.org/wiki/Flugplatz_Regensburg-Oberhub" class="extiw" title="de:Flugplatz Regensburg-Oberhub">Regensburg-Oberhub</a></td>
<td><a href="/wiki/Regenstauf" title="Regenstauf">Regenstauf</a> / <a href="/wiki/Regensburg" title="Regensburg">Regensburg</a>
</td></tr>
<tr>
<td>EDNY</td>
<td>FDH</td>
<td><a href="/wiki/Friedrichshafen_Airport" title="Friedrichshafen Airport">Friedrichshafen Airport</a> (Bodensee Airport Friedrichshafen)</td>
<td><a href="/wiki/Friedrichshafen" title="Friedrichshafen">Friedrichshafen</a>
</td></tr>
<tr>
<td>EDOD</td>
<td></td>
<td><a href="/wiki/Reinsdorf_Airfield" title="Reinsdorf Airfield">Reinsdorf Airfield</a></td>
<td><a href="/wiki/Teltow-Fl%C3%A4ming" title="Teltow-Fläming">Teltow-Fläming</a>
</td></tr>
<tr>
<td>EDOJ</td>
<td></td>
<td><a href="https://de.wikipedia.org/wiki/Flugplatz_L%C3%BCsse" class="extiw" title="de:Flugplatz Lüsse">Lüsse Airport</a></td>
<td><a href="https://de.wikipedia.org/wiki/Lutherstadt_Wittenberg" class="extiw" title="de:Lutherstadt Wittenberg">Wittenberg</a>
</td></tr>
<tr>
<td>EDON</td>
<td></td>
<td>Neuhardenberg Airfield</td>
<td><a href="/wiki/Neuhardenberg" title="Neuhardenberg">Neuhardenberg</a></td>
<td></td>
<td>formerly Marxwalde Air Base
</td></tr>
<tr>
<td>EDOP</td>
<td>SZW</td>
<td><a href="/wiki/Parchim_International_Airport" title="Parchim International Airport">Parchim International Airport</a></td>
<td><a href="/wiki/Parchim" title="Parchim">Parchim</a>
</td></tr>
<tr>
<td>EDOV</td>
<td></td>
<td><a href="https://de.wikipedia.org/wiki/Flugplatz_Stendal-Borstel" class="extiw" title="de:Flugplatz Stendal-Borstel">Stendal-Borstel Airport</a></td>
<td><a href="/wiki/Stendal" title="Stendal">Stendal</a>
</td></tr>
<tr>
<td>EDQA</td>
<td></td>
<td><a href="https://de.wikipedia.org/wiki/Flugplatz_Bamberg-Breitenau" class="extiw" title="de:Flugplatz Bamberg-Breitenau">Bamberg-Breitenau Airfield</a></td>
<td><a href="/wiki/Bamberg" title="Bamberg">Bamberg</a>
</td></tr>
<tr>
<td>EDQB</td>
<td></td>
<td>Bad Windsheim Airport</td>
<td><a href="/wiki/Bad_Windsheim" title="Bad Windsheim">Bad Windsheim</a>
</td></tr>
<tr>
<td>EDQC</td>
<td></td>
<td><a href="/wiki/Coburg#Infrastructure" title="Coburg">Coburg Brandensteinsebene Airfield</a></td>
<td><a href="/wiki/Coburg" title="Coburg">Coburg</a>
</td></tr>
<tr>
<td>EDQD</td>
<td>BYU</td>
<td><a href="/wiki/Bindlacher_Berg_Airport" class="mw-redirect" title="Bindlacher Berg Airport">Bindlacher Berg Airport</a> (Bayreuth Airport)</td>
<td><a href="/wiki/Bayreuth" title="Bayreuth">Bayreuth</a>
</td></tr>
<tr>
<td>EDQE</td>
<td>URD</td>
<td>Burg Feuerstein Airfield</td>
<td><a href="/wiki/Feuerstein_Castle" title="Feuerstein Castle">Burg Feuerstein</a>
</td></tr>
<tr>
<td>EDQG</td>
<td></td>
<td><a href="/wiki/Giebelstadt_Airport" title="Giebelstadt Airport">Giebelstadt Airport</a></td>
<td><a href="/wiki/Giebelstadt" title="Giebelstadt">Giebelstadt</a>
</td></tr>
<tr>
<td>EDQH</td>
<td></td>
<td><a href="/wiki/Herzogenaurach_Airport" title="Herzogenaurach Airport">Herzogenaurach Airport</a></td>
<td><a href="/wiki/Herzogenaurach" title="Herzogenaurach">Herzogenaurach</a>
</td></tr>
<tr>
<td>EDQL</td>
<td></td>
<td><a href="/w/index.php?title=Lichtenfels_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Lichtenfels Airfield (page does not exist)">Lichtenfels Airfield</a></td>
<td><a href="/wiki/Lichtenfels,_Bavaria" title="Lichtenfels, Bavaria">Lichtenfels</a>
</td></tr>
<tr>
<td>EDQM</td>
<td>HOQ</td>
<td><a href="/wiki/Hof%E2%80%93Plauen_Airport" title="Hof–Plauen Airport">Hof–Plauen Airport</a></td>
<td><a href="/wiki/Hof,_Bavaria" title="Hof, Bavaria">Hof</a>/<a href="/wiki/Plauen" title="Plauen">Plauen</a>
</td></tr>
<tr>
<td>EDQY</td>
<td></td>
<td><a href="/wiki/Coburg#Infrastructure" title="Coburg">Coburg Steinrücken Airfield</a></td>
<td><a href="/wiki/Coburg" title="Coburg">Coburg</a>
</td></tr>
<tr>
<td>EDRB</td>
<td>BBJ</td>
<td><a href="/wiki/Bitburg_Airport" title="Bitburg Airport">Bitburg Airport</a></td>
<td><a href="/wiki/Bitburg" title="Bitburg">Bitburg</a>
</td></tr>
<tr>
<td>EDRE</td>
<td></td>
<td><a href="/wiki/Mendig_Air_Base#Current_use" title="Mendig Air Base">Mendig Airfield</a></td>
<td><a href="/wiki/Mendig" title="Mendig">Mendig</a></td>
<td></td>
<td>formerly <a href="/wiki/Mendig_Air_Base" title="Mendig Air Base">Mendig Air Base</a> - ETHM
</td></tr>
<tr>
<td>EDRH</td>
<td></td>
<td><a href="/wiki/Hoppst%C3%A4dten-Weiersbach_Airfield" title="Hoppstädten-Weiersbach Airfield">Hoppstädten-Weiersbach Airfield</a></td>
<td><a href="/wiki/Hoppst%C3%A4dten" title="Hoppstädten">Hoppstädten</a>
</td></tr>
<tr>
<td>EDRI</td>
<td></td>
<td><a href="/w/index.php?title=Linkenheim_Airport&amp;action=edit&amp;redlink=1" class="new" title="Linkenheim Airport (page does not exist)">Linkenheim Airport</a></td>
<td><a href="/wiki/Linkenheim-Hochstetten" title="Linkenheim-Hochstetten">Linkenheim-Hochstetten</a>
</td></tr>
<tr>
<td>EDRK</td>
<td></td>
<td><a href="/wiki/Koblenz-Winningen_Airport" title="Koblenz-Winningen Airport">Koblenz-Winningen Airport</a></td>
<td><a href="/wiki/Winningen" title="Winningen">Winningen</a>, <a href="/wiki/Moselle_(river)" class="mw-redirect" title="Moselle (river)">Mosel</a>
</td></tr>
<tr>
<td>EDRN</td>
<td></td>
<td><a href="/wiki/Nannhausen_Airfield" title="Nannhausen Airfield">Nannhausen Airfield</a>
</td></tr>
<tr>
<td>EDRT</td>
<td>ZQE</td>
<td><a href="/wiki/Trier-F%C3%B6hren_Airport" class="mw-redirect" title="Trier-Föhren Airport">Trier-Föhren Airport</a></td>
<td><a href="/wiki/Trier" title="Trier">Trier</a>
</td></tr>
<tr>
<td>EDRY</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Speyer&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Speyer (page does not exist)">Flugplatz Speyer</a></td>
<td><a href="/wiki/Speyer" title="Speyer">Speyer</a>
</td></tr>
<tr>
<td>EDRZ</td>
<td>ZQW</td>
<td><a href="/wiki/Zweibr%C3%BCcken_Air_Base" title="Zweibrücken Air Base">Zweibrücken Airport</a></td>
<td><a href="/wiki/Zweibr%C3%BCcken" title="Zweibrücken">Zweibrücken</a>
</td></tr>
<tr>
<td>EDSB</td>
<td>FKB</td>
<td><a href="/wiki/Karlsruhe/Baden-Baden_Airport" title="Karlsruhe/Baden-Baden Airport">Karlsruhe/Baden-Baden Airport</a></td>
<td><a href="/wiki/Baden-Baden" title="Baden-Baden">Baden-Baden</a> / <a href="/wiki/Karlsruhe" title="Karlsruhe">Karlsruhe</a>
</td></tr>
<tr>
<td>EDSN</td>
<td></td>
<td><a href="/wiki/Neuhausen_ob_Eck_Airfield" title="Neuhausen ob Eck Airfield">Neuhausen ob Eck Airfield</a></td>
<td><a href="/wiki/Neuhausen_ob_Eck" title="Neuhausen ob Eck">Neuhausen ob Eck</a>
</td></tr>
<tr>
<td>EDSP</td>
<td></td>
<td><a href="/wiki/Poltringen_Airfield" title="Poltringen Airfield">Poltringen Airfield</a></td>
<td><a href="/wiki/Poltringen" title="Poltringen">Poltringen</a>
</td></tr>
<tr>
<td>EDTB</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Baden-Oos&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Baden-Oos (page does not exist)">Flugplatz Baden-Oos</a></td>
<td><a href="/wiki/Baden-Baden" title="Baden-Baden">Baden-Baden</a>
</td></tr>
<tr>
<td>EDTD</td>
<td>ZQL</td>
<td><a href="/w/index.php?title=Flugplatz_Donaueschingen-Villingen&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Donaueschingen-Villingen (page does not exist)">Flugplatz Donaueschingen-Villingen</a></td>
<td><a href="/wiki/Donaueschingen" title="Donaueschingen">Donaueschingen</a>
</td></tr>
<tr>
<td>EDTE</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Eutingen&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Eutingen (page does not exist)">Flugplatz Eutingen</a></td>
<td><a href="/wiki/Eutingen_im_G%C3%A4u" title="Eutingen im Gäu">Eutingen im Gäu</a>
</td></tr>
<tr>
<td>EDTF</td>
<td>QFB</td>
<td><a href="/wiki/Freiburg_im_Breisgau#Transport" title="Freiburg im Breisgau">Flugplatz Freiburg</a></td>
<td><a href="/wiki/Freiburg_im_Breisgau" title="Freiburg im Breisgau">Freiburg</a>
</td></tr>
<tr>
<td>EDTG</td>
<td></td>
<td><a href="/w/index.php?title=Bremgarten_Airport&amp;action=edit&amp;redlink=1" class="new" title="Bremgarten Airport (page does not exist)">Bremgarten Airport</a></td>
<td><a href="/wiki/Hartheim_am_Rhein" title="Hartheim am Rhein">Bremgarten</a>
</td></tr>
<tr>
<td>EDTL</td>
<td>LHA</td>
<td><a href="/wiki/Flughafen_Lahr" class="mw-redirect" title="Flughafen Lahr">Flughafen Lahr</a></td>
<td><a href="/wiki/Lahr" title="Lahr">Lahr</a>
</td></tr>
<tr>
<td>EDTM</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Mengen-Hohentengen&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Mengen-Hohentengen (page does not exist)">Flugplatz Mengen-Hohentengen</a></td>
<td><a href="/wiki/Mengen,_Germany" title="Mengen, Germany">Mengen</a>
</td></tr>
<tr>
<td>EDTQ</td>
<td></td>
<td><a href="/w/index.php?title=Pattonville_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Pattonville Airfield (page does not exist)">Pattonville Airfield</a></td>
<td><a href="/wiki/Pattonville" title="Pattonville">Pattonville</a>
</td></tr>
<tr>
<td>EDTR</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Herten&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Herten (page does not exist)">Flugplatz Herten</a></td>
<td><a href="/wiki/Rheinfelden_(Baden)" title="Rheinfelden (Baden)">Rheinfelden (Baden)</a><sup id="cite_ref-6" class="reference"><a href="#cite_note-6">[6]</a></sup>
</td></tr>
<tr>
<td>EDTX</td>
<td></td>
<td><a href="/w/index.php?title=Weckrieden_Airport&amp;action=edit&amp;redlink=1" class="new" title="Weckrieden Airport (page does not exist)">Weckrieden Airport</a></td>
<td><a href="/wiki/Schw%C3%A4bisch_Hall" title="Schwäbisch Hall">Schwäbisch Hall</a>
</td></tr>
<tr>
<td>EDTY</td>
<td></td>
<td><a href="/w/index.php?title=Adolf_W%C3%BCrth_Airport&amp;action=edit&amp;redlink=1" class="new" title="Adolf Würth Airport (page does not exist)">Adolf Würth Airport</a></td>
<td><a href="/wiki/Schw%C3%A4bisch_Hall" title="Schwäbisch Hall">Schwäbisch Hall</a>
</td></tr>
<tr>
<td><s>EDUC</s></td>
<td></td>
<td><s><a href="/wiki/Brand-Briesen_Airfield" title="Brand-Briesen Airfield">Brand-Briesen Airfield</a></s></td>
<td><a href="/wiki/Halbe,_Brandenburg" title="Halbe, Brandenburg">Halbe</a>
</td></tr>
<tr>
<td><s>EDUW</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Wildenrath" title="RAF Wildenrath">RAF Wildenrath</a></s></td>
<td><a href="/wiki/Wildenrath" title="Wildenrath">Wildenrath</a>
</td></tr>
<tr>
<td>EDVA</td>
<td></td>
<td><a href="/wiki/Flugplatz_Bad_Gandersheim" class="mw-redirect" title="Flugplatz Bad Gandersheim">Flugplatz Bad Gandersheim</a></td>
<td><a href="/wiki/Bad_Gandersheim" title="Bad Gandersheim">Bad Gandersheim</a>
</td></tr>
<tr>
<td>EDVE</td>
<td>BWE</td>
<td><a href="/wiki/Braunschweig_Airport" class="mw-redirect" title="Braunschweig Airport">Braunschweig-Wolfsburg Airport</a></td>
<td><a href="/wiki/Braunschweig" title="Braunschweig">Braunschweig</a>
</td></tr>
<tr>
<td>EDVI</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_H%C3%B6xter-Holzminden&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Höxter-Holzminden (page does not exist)">Flugplatz Höxter-Holzminden</a></td>
<td><a href="/wiki/H%C3%B6xter" title="Höxter">Höxter</a> / <a href="/wiki/Holzminden" title="Holzminden">Holzminden</a>
</td></tr>
<tr>
<td>EDVK</td>
<td>KSF</td>
<td><a href="/wiki/Kassel_Calden_Airport" class="mw-redirect" title="Kassel Calden Airport">Kassel Calden Airport</a></td>
<td><a href="/wiki/Kassel" title="Kassel">Kassel</a>
</td></tr>
<tr>
<td>EDVM</td>
<td>ZNO</td>
<td><a href="/wiki/Flugplatz_Hildesheim-Drispenstedt" title="Flugplatz Hildesheim-Drispenstedt">Hildesheim Airfield</a></td>
<td><a href="/wiki/Hildesheim" title="Hildesheim">Hildesheim</a>
</td></tr>
<tr>
<td>EDVW</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Bad_Pyrmont&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Bad Pyrmont (page does not exist)">Flugplatz Bad Pyrmont</a></td>
<td><a href="/wiki/Bad_Pyrmont" title="Bad Pyrmont">Bad Pyrmont</a>
</td></tr>
<tr>
<td><s>EDWB</s></td>
<td><s>BRV</s></td>
<td><s><a href="/wiki/Bremerhaven_Airport" title="Bremerhaven Airport">Bremerhaven Airport</a></s></td>
<td><a href="/wiki/Bremerhaven" title="Bremerhaven">Bremerhaven</a></td>
<td></td>
<td>closed in 2016
</td></tr>
<tr>
<td>EDWC</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Damme&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Damme (page does not exist)">Flugplatz Damme</a></td>
<td><a href="/wiki/Damme_(D%C3%BCmmer)" title="Damme (Dümmer)">Damme</a>
</td></tr>
<tr>
<td>EDWE</td>
<td>EME</td>
<td><a href="/wiki/Emden_Airport" title="Emden Airport">Emden Airport</a></td>
<td><a href="/wiki/Emden" title="Emden">Emden</a>
</td></tr>
<tr>
<td>EDWF</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Leer_Papenburg&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Leer Papenburg (page does not exist)">Flugplatz Leer Papenburg</a></td>
<td><a href="/wiki/Leer,_Lower_Saxony" title="Leer, Lower Saxony">Leer</a>
</td></tr>
<tr>
<td>EDWG</td>
<td></td>
<td><a href="/wiki/Wangerooge_Airfield" title="Wangerooge Airfield">Wangerooge Airfield</a></td>
<td><a href="/wiki/Wangerooge" title="Wangerooge">Wangerooge</a>
</td></tr>
<tr>
<td>EDWH</td>
<td></td>
<td><a href="/wiki/Oldenburg_(city)#Economy_and_infrastructure" title="Oldenburg (city)">Flugplatz Oldenburg-Hatten</a></td>
<td><a href="/wiki/Hatten" title="Hatten">Hatten</a>
</td></tr>
<tr>
<td>EDWI</td>
<td>WVN</td>
<td><a href="/wiki/JadeWeser_Airport" title="JadeWeser Airport">JadeWeser Airport</a></td>
<td><a href="/wiki/Wilhelmshaven" title="Wilhelmshaven">Wilhelmshaven</a>
</td></tr>
<tr>
<td>EDWJ</td>
<td></td>
<td><a href="/w/index.php?title=Juist_Airport&amp;action=edit&amp;redlink=1" class="new" title="Juist Airport (page does not exist)">Juist Airport</a></td>
<td><a href="/wiki/Juist" title="Juist">Juist</a>
</td></tr>
<tr>
<td>EDWO</td>
<td></td>
<td><a href="/wiki/Atterheide_Airfield" title="Atterheide Airfield">Atterheide Airfield</a></td>
<td><a href="/wiki/Osnabr%C3%BCck" title="Osnabrück">Osnabrück</a>
</td></tr>
<tr>
<td>EDWR</td>
<td></td>
<td><a href="/wiki/Borkum_Airfield" title="Borkum Airfield">Borkum Airfield</a></td>
<td><a href="/wiki/Borkum" title="Borkum">Borkum</a>
</td></tr>
<tr>
<td>EDWS</td>
<td>NOD</td>
<td><a href="/w/index.php?title=Norden-Norddeich_Airport&amp;action=edit&amp;redlink=1" class="new" title="Norden-Norddeich Airport (page does not exist)">Norden-Norddeich Airport</a></td>
<td><a href="/wiki/Norden,_Lower_Saxony" title="Norden, Lower Saxony">Norden</a></td>
<td><a href="/wiki/Lower_Saxony" title="Lower Saxony">Lower Saxony</a>
</td></tr>
<tr>
<td>EDWU</td>
<td>VAC</td>
<td><a href="/wiki/Varrelbusch_Airport" title="Varrelbusch Airport">Varrelbusch Airport</a></td>
<td><a href="/wiki/Cloppenburg" title="Cloppenburg">Cloppenburg</a>
</td></tr>
<tr>
<td>EDWY</td>
<td></td>
<td><a href="/wiki/Norderney_Airfield" class="mw-redirect" title="Norderney Airfield">Norderney Airfield</a></td>
<td><a href="/wiki/Norderney" title="Norderney">Norderney</a>
</td></tr>
<tr>
<td>EDXA</td>
<td></td>
<td><a href="/wiki/Flugplatz_Achmer" class="mw-redirect" title="Flugplatz Achmer">Flugplatz Achmer</a></td>
<td><a href="/wiki/Achmer" class="mw-redirect" title="Achmer">Achmer</a>
</td></tr>
<tr>
<td>EDXB</td>
<td>HEI</td>
<td><a href="/wiki/Heide-B%C3%BCsum_Airport" class="mw-redirect" title="Heide-Büsum Airport">Heide-Büsum Airport</a></td>
<td><a href="/wiki/Heide" title="Heide">Heide</a>
</td></tr>
<tr>
<td>EDXF</td>
<td>FLF</td>
<td><a href="/wiki/Flensburg-Sch%C3%A4ferhaus_Airport" title="Flensburg-Schäferhaus Airport">Flensburg-Schäferhaus Airport</a></td>
<td><a href="/wiki/Flensburg" title="Flensburg">Flensburg</a>
</td></tr>
<tr>
<td>EDXH</td>
<td>HGL</td>
<td><a href="/wiki/Heligoland_Airfield" title="Heligoland Airfield">Heligoland Airfield</a></td>
<td><a href="/wiki/Heligoland" title="Heligoland">Heligoland</a>
</td></tr>
<tr>
<td>EDXJ</td>
<td>QHU</td>
<td><a href="/wiki/Husum_Schwesing_Airport" title="Husum Schwesing Airport">Husum Schwesing Airport</a></td>
<td><a href="/wiki/Husum" title="Husum">Husum</a>
</td></tr>
<tr>
<td>EDXK</td>
<td></td>
<td><a href="/wiki/Leck_Air_Base" title="Leck Air Base">Leck Air Base</a></td>
<td><a href="/wiki/Leck,_Nordfriesland" title="Leck, Nordfriesland">Leck</a></td>
<td></td>
<td>joint military/civilian use
</td></tr>
<tr>
<td>EDXM</td>
<td></td>
<td><a href="/w/index.php?title=Flugplatz_Sankt_Michaelisdonn&amp;action=edit&amp;redlink=1" class="new" title="Flugplatz Sankt Michaelisdonn (page does not exist)">Flugplatz Sankt Michaelisdonn</a></td>
<td><a href="/wiki/Sankt_Michaelisdonn" title="Sankt Michaelisdonn">Sankt Michaelisdonn</a>
</td></tr>
<tr>
<td>EDXO</td>
<td>PSH</td>
<td><a href="/wiki/Sankt_Peter-Ording_Airport" title="Sankt Peter-Ording Airport">Sankt Peter-Ording Airport</a></td>
<td><a href="/wiki/Sankt_Peter-Ording" title="Sankt Peter-Ording">Sankt Peter-Ording</a>
</td></tr>
<tr>
<td>EDXP</td>
<td></td>
<td><a href="/wiki/Harle_Airfield" title="Harle Airfield">Harle Airfield</a></td>
<td><a href="/wiki/Harlesiel" title="Harlesiel">Harlesiel</a>
</td></tr>
<tr>
<td>EDXW</td>
<td>GWT</td>
<td><a href="/wiki/Sylt_Airport" title="Sylt Airport">Sylt Airport</a></td>
<td><a href="/wiki/Westerland,_Germany" title="Westerland, Germany">Westerland</a></td>
<td><a href="/wiki/Sylt" title="Sylt">Sylt</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("ED – Civilian airports.csv", mode='w', newline='', encoding='utf-8') as csv_file:
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