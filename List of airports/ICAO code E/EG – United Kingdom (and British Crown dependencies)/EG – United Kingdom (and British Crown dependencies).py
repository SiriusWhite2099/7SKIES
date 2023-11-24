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
<th width="*">Region or<br>territory&nbsp;&nbsp;
</th>
<th width="*">Notes&nbsp;&nbsp;
</th></tr>
<tr>
<td>EGAA</td>
<td>BFS</td>
<td><a href="/wiki/Belfast_International_Airport" title="Belfast International Airport">Belfast International Airport</a></td>
<td><a href="/wiki/Aldergrove,_County_Antrim" title="Aldergrove, County Antrim">Aldergrove</a>, near <a href="/wiki/Belfast" title="Belfast">Belfast</a></td>
<td><a href="/wiki/Northern_Ireland" title="Northern Ireland">Northern Ireland</a>
</td></tr>
<tr>
<td>EGAB</td>
<td>ENK</td>
<td><a href="/wiki/Enniskillen/St_Angelo_Airport" title="Enniskillen/St Angelo Airport">Enniskillen/St Angelo Airport</a></td>
<td><a href="/wiki/Enniskillen" title="Enniskillen">Enniskillen</a></td>
<td>Northern Ireland
</td></tr>
<tr>
<td>EGAC</td>
<td>BHD</td>
<td><a href="/wiki/George_Best_Belfast_City_Airport" title="George Best Belfast City Airport">George Best Belfast City Airport</a></td>
<td><a href="/wiki/Belfast" title="Belfast">Belfast</a></td>
<td>Northern Ireland
</td></tr>
<tr>
<td>EGAD</td>
<td></td>
<td><a href="/wiki/Newtownards_Airport" title="Newtownards Airport">Newtownards Airport</a></td>
<td><a href="/wiki/Newtownards" title="Newtownards">Newtownards</a></td>
<td>Northern Ireland
</td></tr>
<tr>
<td>EGAE</td>
<td>LDY</td>
<td><a href="/wiki/City_of_Derry_Airport" title="City of Derry Airport">City of Derry Airport</a></td>
<td><a href="/wiki/Derry" title="Derry">Derry</a></td>
<td>Northern Ireland
</td></tr>
<tr>
<td>EGAH</td>
<td></td>
<td><a href="/wiki/Halley_Research_Station" title="Halley Research Station">Halley Research Station</a></td>
<td><a href="/wiki/Brunt_Ice_Shelf" title="Brunt Ice Shelf">Brunt Ice Shelf</a></td>
<td>Antarctica
</td></tr>
<tr>
<td><s>EGAL</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Langford_Lodge" title="RAF Langford Lodge">RAF Langford Lodge</a></s>
</td></tr>
<tr>
<td>EGAR</td>
<td></td>
<td><a href="/wiki/Rothera_Research_Station" title="Rothera Research Station">Rothera Research Station</a></td>
<td><a href="/wiki/Adelaide_Island" title="Adelaide Island">Adelaide Island</a></td>
<td>Antarctica
</td></tr>
<tr>
<td>EGBB</td>
<td>BHX</td>
<td><a href="/wiki/Birmingham_Airport" title="Birmingham Airport">Birmingham Airport</a></td>
<td><a href="/wiki/Birmingham" title="Birmingham">Birmingham</a></td>
<td>England
</td></tr>
<tr>
<td>EGBC</td>
<td></td>
<td><a href="/wiki/Cheltenham_Racecourse_Heliport" class="mw-redirect" title="Cheltenham Racecourse Heliport">Cheltenham Racecourse Heliport</a></td>
<td><a href="/wiki/Cheltenham_Racecourse" title="Cheltenham Racecourse">Cheltenham Racecourse</a></td>
<td>England
</td></tr>
<tr>
<td>EGBD</td>
<td></td>
<td><a href="/wiki/Derby_Airfield" title="Derby Airfield">Derby Airfield</a></td>
<td><a href="/wiki/Derby" title="Derby">Derby</a></td>
<td>England
</td></tr>
<tr>
<td>EGBE</td>
<td>CVT</td>
<td><a href="/wiki/Coventry_Airport" title="Coventry Airport">Coventry Airport</a></td>
<td><a href="/wiki/Coventry" title="Coventry">Coventry</a></td>
<td>England
</td></tr>
<tr>
<td>EGBF</td>
<td></td>
<td><a href="/wiki/Bedford_Aerodrome" title="Bedford Aerodrome">Bedford Aerodrome</a></td>
<td><a href="/wiki/Thurleigh" title="Thurleigh">Thurleigh</a></td>
<td>England
</td></tr>
<tr>
<td>EGBG</td>
<td></td>
<td><a href="/wiki/Leicester_Airport" title="Leicester Airport">Leicester Airport</a></td>
<td><a href="/wiki/Leicester" title="Leicester">Leicester</a></td>
<td>England
</td></tr>
<tr>
<td>EGBJ</td>
<td>GLO</td>
<td><a href="/wiki/Gloucestershire_Airport" title="Gloucestershire Airport">Gloucestershire Airport</a></td>
<td><a href="/wiki/Staverton,_Gloucestershire" title="Staverton, Gloucestershire">Staverton</a></td>
<td>England
</td></tr>
<tr>
<td>EGBK</td>
<td>ORM</td>
<td><a href="/wiki/Sywell_Aerodrome" title="Sywell Aerodrome">Sywell Aerodrome</a></td>
<td><a href="/wiki/Northampton" title="Northampton">Northampton</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGBL</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Long_Marston" title="RAF Long Marston">RAF Long Marston</a></s>
</td></tr>
<tr>
<td>EGBM</td>
<td></td>
<td><a href="/wiki/Tatenhill_Airfield" title="Tatenhill Airfield">Tatenhill Airfield</a></td>
<td><a href="/wiki/Tatenhill" title="Tatenhill">Tatenhill</a></td>
<td>England
</td></tr>
<tr>
<td>EGBN</td>
<td>NQT</td>
<td><a href="/wiki/Nottingham_Airport" title="Nottingham Airport">Nottingham Airport</a></td>
<td><a href="/wiki/Nottingham" title="Nottingham">Nottingham</a></td>
<td>England
</td></tr>
<tr>
<td>EGBO</td>
<td></td>
<td><a href="/wiki/Wolverhampton_Airport" title="Wolverhampton Airport">Wolverhampton Airport</a></td>
<td><a href="/wiki/Wolverhampton" title="Wolverhampton">Wolverhampton</a></td>
<td>England
</td></tr>
<tr>
<td>EGBP</td>
<td>GBA</td>
<td><a href="/wiki/Cotswold_Airport" title="Cotswold Airport">Cotswold Airport</a></td>
<td><a href="/wiki/Kemble,_Gloucestershire" title="Kemble, Gloucestershire">Kemble</a></td>
<td>England
</td></tr>
<tr>
<td>EGBS</td>
<td></td>
<td><a href="/wiki/Shobdon_Aerodrome" class="mw-redirect" title="Shobdon Aerodrome">Shobdon Aerodrome</a></td>
<td><a href="/wiki/Leominster" title="Leominster">Leominster</a></td>
<td>England
</td></tr>
<tr>
<td>EGBT</td>
<td></td>
<td><a href="/wiki/Turweston_Aerodrome" title="Turweston Aerodrome">Turweston Aerodrome</a></td>
<td><a href="/wiki/Turweston" title="Turweston">Turweston</a></td>
<td>England
</td></tr>
<tr>
<td>EGBV</td>
<td></td>
<td><a href="/wiki/Silverstone_Heliport" title="Silverstone Heliport">Silverstone Heliport</a></td>
<td><a href="/wiki/Silverstone" title="Silverstone">Silverstone</a></td>
<td>England
</td></tr>
<tr>
<td>EGBW</td>
<td></td>
<td><a href="/wiki/Wellesbourne_Mountford_Airfield" title="Wellesbourne Mountford Airfield">Wellesbourne Mountford Airfield</a></td>
<td><a href="/wiki/Wellesbourne" title="Wellesbourne">Wellesbourne</a></td>
<td>England
</td></tr>
<tr>
<td>EGCA</td>
<td></td>
<td><a href="/wiki/Coal_Aston_Airfield" title="Coal Aston Airfield">Coal Aston Airfield</a></td>
<td><a href="/wiki/Coal_Aston" title="Coal Aston">Coal Aston</a></td>
<td>England
</td></tr>
<tr>
<td>EGCB</td>
<td></td>
<td><a href="/wiki/City_Airport_Manchester" class="mw-redirect" title="City Airport Manchester">City Airport Manchester</a></td>
<td><a href="/wiki/Manchester" title="Manchester">Manchester</a></td>
<td>England
</td></tr>
<tr>
<td>EGCC</td>
<td>MAN</td>
<td><a href="/wiki/Manchester_Airport" title="Manchester Airport">Manchester Airport</a></td>
<td><a href="/wiki/Manchester" title="Manchester">Manchester</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGCD</s></td>
<td></td>
<td><s><a href="/wiki/Woodford_Aerodrome" title="Woodford Aerodrome">Woodford Aerodrome</a></s></td>
<td><a href="/wiki/Metropolitan_Borough_of_Stockport" title="Metropolitan Borough of Stockport">Stockport</a></td>
<td>England</td>
<td>closed 2012
</td></tr>
<tr>
<td><s>EGCE</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Wrexham" title="RAF Wrexham">RAF Wrexham</a></s>
</td></tr>
<tr>
<td>EGCF</td>
<td></td>
<td><a href="/wiki/Sandtoft_Airfield" title="Sandtoft Airfield">Sandtoft Airfield</a></td>
<td><a href="/wiki/Scunthorpe" title="Scunthorpe">Scunthorpe</a></td>
<td>England
</td></tr>
<tr>
<td>EGCG</td>
<td></td>
<td><a href="/wiki/Strubby_Airfield" class="mw-redirect" title="Strubby Airfield">Strubby Airfield</a></td>
<td><a href="/wiki/Strubby" title="Strubby">Strubby</a></td>
<td>England
</td></tr>
<tr>
<td>EGCH</td>
<td></td>
<td>Holyhead (Heliport)
</td></tr>
<tr>
<td><s>EGCI</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Doncaster" title="RAF Doncaster">Doncaster Airfield</a></s></td>
<td><a href="/wiki/Doncaster" title="Doncaster">Doncaster</a></td>
<td>England</td>
<td>closed 1992
</td></tr>
<tr>
<td>EGCJ</td>
<td></td>
<td><a href="/wiki/Sherburn-in-Elmet_Airfield" title="Sherburn-in-Elmet Airfield">Sherburn-in-Elmet Airfield</a></td>
<td><a href="/wiki/Sherburn-in-Elmet" class="mw-redirect" title="Sherburn-in-Elmet">Sherburn-in-Elmet</a></td>
<td>England
</td></tr>
<tr>
<td>EGCK</td>
<td></td>
<td><a href="/wiki/Caernarfon_Airport" title="Caernarfon Airport">Caernarfon Airport</a></td>
<td><a href="/wiki/Caernarfon" title="Caernarfon">Caernarfon</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGCL</td>
<td></td>
<td><a href="/wiki/Fenland_Airfield" title="Fenland Airfield">Fenland Airfield</a></td>
<td><a href="/wiki/Spalding,_Lincolnshire" title="Spalding, Lincolnshire">Spalding</a></td>
<td>England
</td></tr>
<tr>
<td>EGCM</td>
<td></td>
<td><a href="/wiki/Leeds_East_Airport" title="Leeds East Airport">Leeds East Airport</a></td>
<td><a href="/wiki/Church_Fenton" title="Church Fenton">Church Fenton</a></td>
<td>England
</td></tr>
<tr>
<td>EGCN</td>
<td>DSA</td>
<td><a href="/wiki/Doncaster_Sheffield_Airport" title="Doncaster Sheffield Airport">Doncaster Sheffield Airport</a></td>
<td><a href="/wiki/South_Yorkshire" title="South Yorkshire">South Yorkshire</a></td>
<td>England
</td></tr>
<tr>
<td>EGCO</td>
<td></td>
<td><a href="/w/index.php?title=Birkdale_Sands_Beach_Runway_Airport&amp;action=edit&amp;redlink=1" class="new" title="Birkdale Sands Beach Runway Airport (page does not exist)">Birkdale Sands Beach Runway Airport</a></td>
<td><a href="/wiki/Southport" title="Southport">Southport</a></td>
<td>England
</td></tr>
<tr>
<td>EGCP</td>
<td></td>
<td>Thorne
</td></tr>
<tr>
<td>EGCR</td>
<td></td>
<td><a href="/w/index.php?title=Ashcroft_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Ashcroft Airfield (page does not exist)">Ashcroft Airfield</a></td>
<td><a href="/wiki/Winsford" title="Winsford">Winsford</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGCR</s></td>
<td></td>
<td><s><a href="/wiki/Croydon_Airport" title="Croydon Airport">Croydon Airport</a></s></td>
<td><a href="/wiki/London" title="London">London</a></td>
<td>England</td>
<td>closed 1959
</td></tr>
<tr>
<td>EGCS</td>
<td></td>
<td><a href="/wiki/Sturgate_Airfield" title="Sturgate Airfield">Sturgate Airfield</a></td>
<td><a href="/wiki/Lincoln,_Lincolnshire" class="mw-redirect" title="Lincoln, Lincolnshire">Lincoln</a></td>
<td>England
</td></tr>
<tr>
<td>EGCT</td>
<td></td>
<td>Tilstock
</td></tr>
<tr>
<td>EGCV</td>
<td></td>
<td><a href="/wiki/Sleap_Airfield" title="Sleap Airfield">Sleap Airfield</a></td>
<td><a href="/wiki/Shrewsbury" title="Shrewsbury">Shrewsbury</a></td>
<td>England
</td></tr>
<tr>
<td>EGCW</td>
<td></td>
<td><a href="/wiki/Welshpool_Airport" title="Welshpool Airport">Welshpool Airport</a></td>
<td><a href="/wiki/Welshpool" title="Welshpool">Welshpool</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGDA</td>
<td></td>
<td><a href="/wiki/RAF_Brawdy" title="RAF Brawdy">RAF Brawdy</a></td>
<td><a href="/wiki/Pembrokeshire" title="Pembrokeshire">Pembrokeshire</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGDB</td>
<td></td>
<td>Mountwise
</td></tr>
<tr>
<td>EGDC</td>
<td></td>
<td><a href="/wiki/Royal_Marines_Base_Chivenor" class="mw-redirect" title="Royal Marines Base Chivenor">Royal Marines Base Chivenor</a></td>
<td><a href="/wiki/Braunton" title="Braunton">Braunton</a></td>
<td>England
</td></tr>
<tr>
<td>EGDD</td>
<td></td>
<td><a href="/wiki/Bicester_Airfield" title="Bicester Airfield">Bicester Airfield</a></td>
<td><a href="/wiki/Oxfordshire" title="Oxfordshire">Oxfordshire</a></td>
<td>England
</td></tr>
<tr>
<td>EGDF</td>
<td></td>
<td>Alfens (mobile)
</td></tr>
<tr>
<td>EGDH</td>
<td></td>
<td>HQ 2 Group (MOD)
</td></tr>
<tr>
<td>EGDI</td>
<td></td>
<td><a href="/wiki/RAF_Merryfield" title="RAF Merryfield">RAF Merryfield</a></td>
<td><a href="/wiki/Ilminster" title="Ilminster">Ilminster</a></td>
<td>England
</td></tr>
<tr>
<td>EGDJ</td>
<td>UPV</td>
<td><a href="/wiki/RAF_Upavon" title="RAF Upavon">Upavon Airfield</a></td>
<td><a href="/wiki/Upavon" title="Upavon">Upavon</a></td>
<td>England
</td></tr>
<tr>
<td>EGDL</td>
<td>LYE</td>
<td><a href="/wiki/RAF_Lyneham" title="RAF Lyneham">RAF Lyneham</a></td>
<td><a href="/wiki/Wiltshire" title="Wiltshire">Wiltshire</a></td>
<td>England
</td></tr>
<tr>
<td>EGDM</td>
<td></td>
<td><a href="/wiki/MoD_Boscombe_Down" class="mw-redirect" title="MoD Boscombe Down">MoD Boscombe Down</a></td>
<td><a href="/wiki/Amesbury" title="Amesbury">Amesbury</a></td>
<td>England
</td></tr>
<tr>
<td>EGDN</td>
<td></td>
<td><a href="/wiki/Netheravon_Airfield" title="Netheravon Airfield">Netheravon Airfield</a></td>
<td><a href="/wiki/Netheravon" title="Netheravon">Netheravon</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGDO</s></td>
<td></td>
<td><s><a href="/wiki/Predannack_Airfield" title="Predannack Airfield">RNAS Predannack</a></s> satellite of RNAS Culdrose</td>
<td><a href="/wiki/Mullion,_Cornwall" title="Mullion, Cornwall">Mullion</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGDP</s></td>
<td></td>
<td><s><a href="/w/index.php?title=RNAS/MCA_Portland_Heliport&amp;action=edit&amp;redlink=1" class="new" title="RNAS/MCA Portland Heliport (page does not exist)">RNAS/MCA Portland Heliport</a></s></td>
<td><a href="/wiki/Portland_Harbour" title="Portland Harbour">Portland Harbour</a></td>
<td>England</td>
<td>closed 2014
</td></tr>
<tr>
<td>EGDR</td>
<td></td>
<td><a href="/wiki/RNAS_Culdrose_(HMS_Seahawk)" title="RNAS Culdrose (HMS Seahawk)">RNAS Culdrose</a></td>
<td><a href="/wiki/Helston" title="Helston">Helston</a></td>
<td>England
</td></tr>
<tr>
<td>EGDS</td>
<td></td>
<td><a href="/w/index.php?title=Salisbury_Plain_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Salisbury Plain Airfield (page does not exist)">Salisbury Plain Airfield</a></td>
<td><a href="/wiki/Bulford" title="Bulford">Bulford</a></td>
<td>England
</td></tr>
<tr>
<td>EGDT</td>
<td></td>
<td><a href="/wiki/RAF_Wroughton" title="RAF Wroughton">RAF Wroughton</a></td>
<td><a href="/wiki/Wroughton" title="Wroughton">Wroughton</a></td>
<td>England
</td></tr>
<tr>
<td>EGDV</td>
<td></td>
<td><a href="/wiki/Hullavington_Airport" class="mw-redirect" title="Hullavington Airport">Hullavington Airport</a></td>
<td><a href="/wiki/Hullavington" title="Hullavington">Hullavington</a></td>
<td>England
</td></tr>
<tr>
<td>EGDW</td>
<td></td>
<td><a href="/wiki/RNAS_Merryfield" title="RNAS Merryfield">RNAS Merryfield</a></td>
<td><a href="/wiki/Yeovil" title="Yeovil">Yeovil</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGDX</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Saint_Athan" class="mw-redirect" title="RAF Saint Athan">MoD Saint Athan</a></s></td>
<td><a href="/wiki/St_Athan" title="St Athan">St Athan</a></td>
<td>Wales</td>
<td>reassigned to EGSY April 2019
</td></tr>
<tr>
<td>EGDY</td>
<td>YEO</td>
<td><a href="/wiki/RNAS_Yeovilton_(HMS_Heron)" title="RNAS Yeovilton (HMS Heron)">RNAS Yeovilton</a></td>
<td><a href="/wiki/Yeovil" title="Yeovil">Yeovil</a></td>
<td>England
</td></tr>
<tr>
<td>EGEA</td>
<td></td>
<td><a href="/w/index.php?title=Culter_Helipad&amp;action=edit&amp;redlink=1" class="new" title="Culter Helipad (page does not exist)">Culter Helipad</a></td>
<td><a href="/wiki/Aberdeen" title="Aberdeen">Aberdeen</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGEC</td>
<td>CAL</td>
<td><a href="/wiki/Campbeltown_Airport" title="Campbeltown Airport">Campbeltown Airport</a></td>
<td><a href="/wiki/Campbeltown" title="Campbeltown">Campbeltown</a></td>
<td>Scotland</td>
<td>formerly RAF Machrihanish - EGQJ
</td></tr>
<tr>
<td>EGED</td>
<td>EOI</td>
<td><a href="/wiki/Eday_Airport" title="Eday Airport">Eday Airport</a></td>
<td><a href="/wiki/Eday" title="Eday">Eday</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGEF</td>
<td>FIE</td>
<td><a href="/wiki/Fair_Isle_Airport" title="Fair Isle Airport">Fair Isle Airport</a></td>
<td><a href="/wiki/Fair_Isle" title="Fair Isle">Fair Isle</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGEG</td>
<td></td>
<td><a href="/wiki/Glasgow_City_Heliport" title="Glasgow City Heliport">Glasgow City Heliport</a></td>
<td><a href="/wiki/Glasgow" title="Glasgow">Glasgow</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGEH</td>
<td>WHS</td>
<td><a href="/wiki/Whalsay_Airport" class="mw-redirect" title="Whalsay Airport">Whalsay Airport</a></td>
<td><a href="/wiki/Whalsay" title="Whalsay">Whalsay</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGEL</td>
<td>COL</td>
<td><a href="/wiki/Coll_Airport" title="Coll Airport">Coll Airport</a></td>
<td><a href="/wiki/Coll" title="Coll">Coll</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGEN</td>
<td>NRL</td>
<td><a href="/wiki/North_Ronaldsay_Airport" title="North Ronaldsay Airport">North Ronaldsay Airport</a></td>
<td><a href="/wiki/North_Ronaldsay" title="North Ronaldsay">North Ronaldsay</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGEO</td>
<td>OBN</td>
<td><a href="/wiki/Oban_Airport" title="Oban Airport">Oban Airport</a></td>
<td><a href="/wiki/Oban" title="Oban">Oban</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGEP</td>
<td>PPW</td>
<td><a href="/wiki/Papa_Westray_Airport" title="Papa Westray Airport">Papa Westray Airport</a></td>
<td><a href="/wiki/Papa_Westray" title="Papa Westray">Papa Westray</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGER</td>
<td>SOY</td>
<td><a href="/wiki/Stronsay_Airport" title="Stronsay Airport">Stronsay Airport</a></td>
<td><a href="/wiki/Stronsay" title="Stronsay">Stronsay</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGES</td>
<td>NDY</td>
<td><a href="/wiki/Sanday_Airport" title="Sanday Airport">Sanday Airport</a></td>
<td><a href="/wiki/Sanday,_Orkney" title="Sanday, Orkney">Sanday</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGET</td>
<td>LWK</td>
<td><a href="/wiki/Tingwall_Airport" title="Tingwall Airport">Tingwall Airport</a></td>
<td><a href="/wiki/Lerwick" title="Lerwick">Lerwick</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGEW</td>
<td>WRY</td>
<td><a href="/wiki/Westray_Airport" title="Westray Airport">Westray Airport</a></td>
<td><a href="/wiki/Westray" title="Westray">Westray</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGEY</td>
<td>CSA</td>
<td><a href="/wiki/Colonsay_Airport" title="Colonsay Airport">Colonsay Airport</a></td>
<td><a href="/wiki/Colonsay" title="Colonsay">Colonsay</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGFA</td>
<td></td>
<td><a href="/wiki/Aberporth_Airport" title="Aberporth Airport">Aberporth Airport</a></td>
<td><a href="/wiki/Cardigan,_Ceredigion" title="Cardigan, Ceredigion">Cardigan</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGFC</td>
<td></td>
<td><a href="/wiki/Cardiff_Heliport" title="Cardiff Heliport">Cardiff Heliport</a></td>
<td><a href="/wiki/Cardiff" title="Cardiff">Cardiff</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGFE</td>
<td>HAW</td>
<td><a href="/wiki/Haverfordwest_Aerodrome" class="mw-redirect" title="Haverfordwest Aerodrome">Haverfordwest Aerodrome</a></td>
<td><a href="/wiki/Haverfordwest" title="Haverfordwest">Haverfordwest</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGFF</td>
<td>CWL</td>
<td><a href="/wiki/Cardiff_International_Airport" class="mw-redirect" title="Cardiff International Airport">Cardiff International Airport</a></td>
<td><a href="/wiki/Cardiff" title="Cardiff">Cardiff</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGFH</td>
<td>SWS</td>
<td><a href="/wiki/Swansea_Airport" title="Swansea Airport">Swansea Airport</a></td>
<td><a href="/wiki/Swansea" title="Swansea">Swansea</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGFP</td>
<td></td>
<td><a href="/wiki/Pembrey_Airport" title="Pembrey Airport">Pembrey Airport</a></td>
<td><a href="/wiki/Pembrey" title="Pembrey">Pembrey</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGGD</td>
<td>BRS</td>
<td><a href="/wiki/Bristol_Airport" title="Bristol Airport">Bristol Airport</a></td>
<td><a href="/wiki/Bristol" title="Bristol">Bristol</a></td>
<td>England
</td></tr>
<tr>
<td>EGGP</td>
<td>LPL</td>
<td><a href="/wiki/Liverpool_John_Lennon_Airport" title="Liverpool John Lennon Airport">Liverpool John Lennon Airport</a></td>
<td><a href="/wiki/Liverpool" title="Liverpool">Liverpool</a></td>
<td>England
</td></tr>
<tr>
<td>EGGW</td>
<td>LTN</td>
<td><a href="/wiki/London_Luton_Airport" class="mw-redirect" title="London Luton Airport">London Luton Airport</a></td>
<td><a href="/wiki/London" title="London">London</a></td>
<td>England
</td></tr>
<tr>
<td>EGHA</td>
<td></td>
<td><a href="/wiki/Compton_Abbas_Airfield" title="Compton Abbas Airfield">Compton Abbas Airfield</a></td>
<td><a href="/wiki/Shaftesbury" title="Shaftesbury">Shaftesbury</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGHB</s></td>
<td></td>
<td><s><a href="/wiki/Maypole_Airfield" title="Maypole Airfield">Maypole Airfield</a></s></td>
<td><a href="/w/index.php?title=Maypole,_Canterbury&amp;action=edit&amp;redlink=1" class="new" title="Maypole, Canterbury (page does not exist)">Maypole</a>, <a href="/wiki/Kent" title="Kent">Kent</a></td>
<td>England</td>
<td>closed 2021
</td></tr>
<tr>
<td>EGHC</td>
<td>LEQ</td>
<td><a href="/wiki/Land%27s_End_Airport" title="Land's End Airport">Land's End Airport</a></td>
<td><a href="/wiki/St_Just_in_Penwith" title="St Just in Penwith">St Just in Penwith</a></td>
<td>England
</td></tr>
<tr>
<td>EGHD</td>
<td>PLH</td>
<td><a href="/wiki/Plymouth_City_Airport" title="Plymouth City Airport">Plymouth City Airport</a></td>
<td><a href="/wiki/Plymouth" title="Plymouth">Plymouth</a></td>
<td>England</td>
<td>closed 2011
</td></tr>
<tr>
<td>EGHE</td>
<td>ISC</td>
<td><a href="/wiki/St._Mary%27s_Airport_(Isles_of_Scilly)" class="mw-redirect" title="St. Mary's Airport (Isles of Scilly)">St. Mary's Airport</a></td>
<td><a href="/wiki/St._Mary%27s,_Isles_of_Scilly" class="mw-redirect" title="St. Mary's, Isles of Scilly">St. Mary's</a></td>
<td>England
</td></tr>
<tr>
<td>EGHF</td>
<td></td>
<td>Lee on Solent</td>
<td><a href="/wiki/Lee-on-the-Solent" title="Lee-on-the-Solent">Lee-on-the-Solent</a></td>
<td>England</td>
<td>was <a href="/wiki/RNAS_Lee-on-Solent_(HMS_Daedalus)" title="RNAS Lee-on-Solent (HMS Daedalus)">RNAS Lee-on-Solent (HMS Daedalus)</a>
</td></tr>
<tr>
<td>EGHG</td>
<td></td>
<td><a href="/wiki/Yeovil/Westland_Airport" title="Yeovil/Westland Airport">Yeovil/Westland Airport</a></td>
<td><a href="/wiki/Yeovil" title="Yeovil">Yeovil</a></td>
<td>England
</td></tr>
<tr>
<td>EGHH</td>
<td>BOH</td>
<td><a href="/wiki/Bournemouth_Airport" title="Bournemouth Airport">Bournemouth Airport</a></td>
<td><a href="/wiki/Bournemouth" title="Bournemouth">Bournemouth</a></td>
<td>England
</td></tr>
<tr>
<td>EGHI</td>
<td>SOU</td>
<td><a href="/wiki/Southampton_Airport" title="Southampton Airport">Southampton Airport</a></td>
<td><a href="/wiki/Southampton" title="Southampton">Southampton</a></td>
<td>England
</td></tr>
<tr>
<td>EGHJ</td>
<td>BBP</td>
<td><a href="/wiki/Bembridge_Airport" title="Bembridge Airport">Bembridge Airport</a></td>
<td><a href="/wiki/Sandown" title="Sandown">Sandown</a></td>
<td>England
</td></tr>
<tr>
<td>EGHK</td>
<td>PZE</td>
<td><a href="/wiki/Penzance_Heliport" title="Penzance Heliport">Penzance Heliport</a></td>
<td><a href="/wiki/Penzance" title="Penzance">Penzance</a></td>
<td>England
</td></tr>
<tr>
<td>EGHL</td>
<td>QLA</td>
<td><a href="/wiki/Lasham_Airfield" title="Lasham Airfield">Lasham Airfield</a></td>
<td><a href="/wiki/Basingstoke" title="Basingstoke">Basingstoke</a></td>
<td>England
</td></tr>
<tr>
<td>EGHM</td>
<td></td>
<td>Hamble
</td></tr>
<tr>
<td>EGHN</td>
<td></td>
<td><a href="/wiki/Isle_of_Wight/Sandown_Airport" title="Isle of Wight/Sandown Airport">Isle of Wight/Sandown Airport</a></td>
<td><a href="/wiki/Sandown" title="Sandown">Sandown</a></td>
<td>England
</td></tr>
<tr>
<td>EGHO</td>
<td></td>
<td><a href="/wiki/Thruxton_Aerodrome" title="Thruxton Aerodrome">Thruxton Aerodrome</a></td>
<td><a href="/wiki/Andover,_Hampshire" title="Andover, Hampshire">Andover</a></td>
<td>England
</td></tr>
<tr>
<td>EGHP</td>
<td></td>
<td><a href="/wiki/Popham_Airfield" title="Popham Airfield">Popham Airfield</a></td>
<td><a href="/wiki/Popham,_Hampshire" title="Popham, Hampshire">Popham</a></td>
<td>England
</td></tr>
<tr>
<td>EGHQ</td>
<td>NQY</td>
<td><a href="/wiki/Newquay_Cornwall_Airport" class="mw-redirect" title="Newquay Cornwall Airport">Newquay Cornwall Airport</a></td>
<td><a href="/wiki/St_Mawgan" title="St Mawgan">St Mawgan</a>, <a href="/wiki/Cornwall" title="Cornwall">Cornwall</a></td>
<td>England
</td></tr>
<tr>
<td>EGHR</td>
<td></td>
<td><a href="/wiki/Chichester/Goodwood_Airport" title="Chichester/Goodwood Airport">Chichester/Goodwood Airport</a></td>
<td><a href="/wiki/Westhampnett" title="Westhampnett">Westhampnett</a>, <a href="/wiki/Chichester" title="Chichester">Chichester</a></td>
<td>England
</td></tr>
<tr>
<td>EGHS</td>
<td></td>
<td><a href="/wiki/Henstridge_Airfield" class="mw-redirect" title="Henstridge Airfield">Henstridge Airfield</a></td>
<td><a href="/wiki/Henstridge" title="Henstridge">Henstridge</a></td>
<td>England
</td></tr>
<tr>
<td>EGHT</td>
<td></td>
<td><a href="/wiki/Tresco_Heliport" title="Tresco Heliport">Tresco Heliport</a></td>
<td><a href="/wiki/Tresco,_Isles_of_Scilly" title="Tresco, Isles of Scilly">Tresco</a></td>
<td>England
</td></tr>
<tr>
<td>EGHU</td>
<td></td>
<td><a href="/wiki/Eaglescott_Airfield" title="Eaglescott Airfield">Eaglescott Airfield</a></td>
<td><a href="/wiki/Great_Torrington" title="Great Torrington">Great Torrington</a></td>
<td>England
</td></tr>
<tr>
<td>EGHY</td>
<td></td>
<td><a href="/wiki/Truro_Aerodrome" title="Truro Aerodrome">Truro Aerodrome</a></td>
<td><a href="/wiki/Truro" title="Truro">Truro</a></td>
<td>England
</td></tr>
<tr>
<td>EGJA</td>
<td>ACI</td>
<td><a href="/wiki/Alderney_Airport" title="Alderney Airport">Alderney Airport</a></td>
<td><a href="/wiki/Alderney" title="Alderney">Alderney</a></td>
<td>Channel Islands
</td></tr>
<tr>
<td>EGJB</td>
<td>GCI</td>
<td><a href="/wiki/Guernsey_Airport" title="Guernsey Airport">Guernsey Airport</a></td>
<td><a href="/wiki/Guernsey" title="Guernsey">Guernsey</a></td>
<td>Channel Islands
</td></tr>
<tr>
<td>EGJJ</td>
<td>JER</td>
<td><a href="/wiki/Jersey_Airport" title="Jersey Airport">Jersey Airport</a></td>
<td><a href="/wiki/Jersey" title="Jersey">Jersey</a></td>
<td>Channel Islands
</td></tr>
<tr>
<td>EGKA</td>
<td>ESH</td>
<td><a href="/wiki/Shoreham_Airport" class="mw-redirect" title="Shoreham Airport">Shoreham Airport</a></td>
<td><a href="/wiki/Shoreham-by-Sea" title="Shoreham-by-Sea">Shoreham-by-Sea</a></td>
<td>England
</td></tr>
<tr>
<td>EGKB</td>
<td>BQH</td>
<td><a href="/wiki/London_Biggin_Hill_Airport" title="London Biggin Hill Airport">London Biggin Hill Airport</a></td>
<td><a href="/wiki/London" title="London">London</a></td>
<td>England
</td></tr>
<tr>
<td>EGKC</td>
<td></td>
<td><a href="/wiki/LEC_Airfield" title="LEC Airfield">LEC Airfield</a> (Bognor Regis)</td>
<td><a href="/wiki/West_Sussex" title="West Sussex">West Sussex</a></td>
<td>England
</td></tr>
<tr>
<td>EGKD</td>
<td></td>
<td>Albourne
</td></tr>
<tr>
<td>EGKE</td>
<td></td>
<td><a href="/w/index.php?title=Challock_Airport&amp;action=edit&amp;redlink=1" class="new" title="Challock Airport (page does not exist)">Challock Airport</a></td>
<td><a href="/wiki/Challock" title="Challock">Challock</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGKF</s></td>
<td></td>
<td><s><a href="/wiki/RNAS_Ford" class="mw-redirect" title="RNAS Ford">RNAS Ford</a></s></td>
<td><a href="/wiki/Ford,_West_Sussex" title="Ford, West Sussex">Ford</a></td>
<td>England</td>
<td>closed 1958
</td></tr>
<tr>
<td>EGKG</td>
<td></td>
<td><a href="/wiki/Goodwood_Racecourse_Heliport" class="mw-redirect" title="Goodwood Racecourse Heliport">Goodwood Racecourse Heliport</a></td>
<td><a href="/wiki/Goodwood_Racecourse" title="Goodwood Racecourse">Goodwood Racecourse</a></td>
<td>England
</td></tr>
<tr>
<td>EGKH</td>
<td></td>
<td><a href="/wiki/Headcorn_Aerodrome" title="Headcorn Aerodrome">Headcorn Aerodrome</a></td>
<td><a href="/wiki/Maidstone" title="Maidstone">Maidstone</a></td>
<td>England
</td></tr>
<tr>
<td>EGKK</td>
<td>LGW</td>
<td><a href="/wiki/London_Gatwick_Airport" class="mw-redirect" title="London Gatwick Airport">London Gatwick Airport</a></td>
<td><a href="/wiki/London" title="London">London</a></td>
<td>England
</td></tr>
<tr>
<td>EGKL</td>
<td></td>
<td>Deanland</td>
<td><a href="/wiki/Lewes" title="Lewes">Lewes</a></td>
<td>England</td>
<td>was <a href="/wiki/RAF_Deanland" title="RAF Deanland">RAF Deanland</a>
</td></tr>
<tr>
<td>EGKR</td>
<td>KRH</td>
<td><a href="/wiki/Redhill_Aerodrome" title="Redhill Aerodrome">Redhill Aerodrome</a></td>
<td><a href="/wiki/Redhill,_Surrey" title="Redhill, Surrey">Redhill</a></td>
<td>England
</td></tr>
<tr>
<td>EGLA</td>
<td></td>
<td><a href="/wiki/Bodmin_Airfield" title="Bodmin Airfield">Bodmin Airfield</a></td>
<td><a href="/wiki/Bodmin" title="Bodmin">Bodmin</a></td>
<td>England
</td></tr>
<tr>
<td>EGLB</td>
<td></td>
<td><a href="/wiki/Brooklands" title="Brooklands">Brooklands</a>
</td></tr>
<tr>
<td>EGLC</td>
<td>LCY</td>
<td><a href="/wiki/London_City_Airport" title="London City Airport">London City Airport</a></td>
<td><a href="/wiki/London" title="London">London</a></td>
<td>England
</td></tr>
<tr>
<td>EGLD</td>
<td></td>
<td><a href="/wiki/Denham_Aerodrome" title="Denham Aerodrome">Denham Aerodrome</a></td>
<td><a href="/wiki/Gerrards_Cross" title="Gerrards Cross">Gerrards Cross</a></td>
<td>England
</td></tr>
<tr>
<td>EGLF</td>
<td>FAB</td>
<td><a href="/wiki/Farnborough_Airport" title="Farnborough Airport">Farnborough Airport</a></td>
<td><a href="/wiki/Farnborough,_Hampshire" title="Farnborough, Hampshire">Farnborough</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGLG</s></td>
<td></td>
<td><s><a href="/wiki/Panshanger_Airport" class="mw-redirect" title="Panshanger Airport">Panshanger Airport</a></s></td>
<td><a href="/wiki/Hertford" title="Hertford">Hertford</a></td>
<td>England</td>
<td>closed 2014; proposed reopening
</td></tr>
<tr>
<td>EGLI</td>
<td></td>
<td>Isleworth
</td></tr>
<tr>
<td>EGLJ</td>
<td></td>
<td><a href="/wiki/Chalgrove_Airfield" title="Chalgrove Airfield">Chalgrove Airfield</a></td>
<td><a href="/wiki/Oxford" title="Oxford">Oxford</a></td>
<td>England
</td></tr>
<tr>
<td>EGLK</td>
<td>BBS</td>
<td><a href="/wiki/Blackbushe_Airport" title="Blackbushe Airport">Blackbushe Airport</a></td>
<td><a href="/wiki/Camberley" title="Camberley">Camberley</a></td>
<td>England
</td></tr>
<tr>
<td>EGLL</td>
<td>LHR</td>
<td><a href="/wiki/London_Heathrow_Airport" class="mw-redirect" title="London Heathrow Airport">London Heathrow Airport</a></td>
<td><a href="/wiki/London" title="London">London</a></td>
<td>England
</td></tr>
<tr>
<td>EGLM</td>
<td></td>
<td><a href="/wiki/White_Waltham_Airfield" title="White Waltham Airfield">White Waltham Airfield</a></td>
<td><a href="/wiki/White_Waltham" title="White Waltham">White Waltham</a></td>
<td>England
</td></tr>
<tr>
<td>EGLP</td>
<td></td>
<td><a href="/wiki/Brimpton_Airfield" title="Brimpton Airfield">Brimpton (Wasing Lower Farm)</a></td>
<td><a href="/wiki/Upper_Bucklebury" class="mw-redirect" title="Upper Bucklebury">Upper Bucklebury</a></td>
<td>England
</td></tr>
<tr>
<td>EGLS</td>
<td></td>
<td><a href="/wiki/Old_Sarum_Airfield" title="Old Sarum Airfield">Old Sarum Airfield</a></td>
<td><a href="/wiki/Salisbury" title="Salisbury">Salisbury</a></td>
<td>England
</td></tr>
<tr>
<td>EGLT</td>
<td></td>
<td><a href="/wiki/Ascot_Racecourse_Heliport" class="mw-redirect" title="Ascot Racecourse Heliport">Ascot Racecourse Heliport</a></td>
<td><a href="/wiki/Ascot_Racecourse" title="Ascot Racecourse">Ascot Racecourse</a></td>
<td>England
</td></tr>
<tr>
<td>EGLW</td>
<td></td>
<td><a href="/wiki/London_Heliport" title="London Heliport">London Heliport</a></td>
<td><a href="/wiki/London" title="London">London</a></td>
<td>England
</td></tr>
<tr>
<td>EGMA</td>
<td></td>
<td><a href="/wiki/Fowlmere_Airfield" title="Fowlmere Airfield">Fowlmere Airfield</a></td>
<td><a href="/wiki/Cambridge" title="Cambridge">Cambridge</a></td>
<td>England
</td></tr>
<tr>
<td>EGMC</td>
<td>SEN</td>
<td><a href="/wiki/London_Southend_Airport" title="London Southend Airport">London Southend Airport</a></td>
<td><a href="/wiki/Southend-on-Sea" title="Southend-on-Sea">Southend-on-Sea</a></td>
<td>England
</td></tr>
<tr>
<td>EGMD</td>
<td>LYX</td>
<td><a href="/wiki/London_Ashford_Airport" class="mw-redirect" title="London Ashford Airport">London Ashford Airport</a></td>
<td><a href="/wiki/Lydd" title="Lydd">Lydd</a></td>
<td>England
</td></tr>
<tr>
<td>EGMF</td>
<td></td>
<td>Farthing Corner</td>
<td><a href="/wiki/Rainham,_Kent" title="Rainham, Kent">Rainham</a></td>
<td>England
</td></tr>
<tr>
<td>EGMH</td>
<td>MSE</td>
<td><a href="/wiki/Kent_International_Airport" class="mw-redirect" title="Kent International Airport">Kent International Airport</a></td>
<td><a href="/wiki/Ramsgate" title="Ramsgate">Ramsgate</a></td>
<td>England
</td></tr>
<tr>
<td>EGMJ</td>
<td></td>
<td><a href="/wiki/Little_Gransden_Airfield" title="Little Gransden Airfield">Little Gransden Airfield</a></td>
<td><a href="/wiki/St_Neots" title="St Neots">St Neots</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGMK</s></td>
<td><s>LYM</s></td>
<td><s><a href="/wiki/Lympne_Airport" title="Lympne Airport">Lympne Airport</a></s></td>
<td><a href="/wiki/Lympne" title="Lympne">Lympne</a>, Kent</td>
<td>England
</td></tr>
<tr>
<td>EGML</td>
<td></td>
<td><a href="/wiki/Damyns_Hall_Aerodrome" title="Damyns Hall Aerodrome">Damyns Hall Aerodrome</a></td>
<td><a href="/wiki/Upminster" title="Upminster">Upminster</a></td>
<td>England
</td></tr>
<tr>
<td>EGMT</td>
<td></td>
<td><a href="/w/index.php?title=Thurrock_Aerodrome&amp;action=edit&amp;redlink=1" class="new" title="Thurrock Aerodrome (page does not exist)">Thurrock Aerodrome</a></td>
<td><a href="/wiki/Thurrock" title="Thurrock">Thurrock</a></td>
<td>England
</td></tr>
<tr>
<td>EGNA</td>
<td></td>
<td><a href="/wiki/Hucknall_Airfield" class="mw-redirect" title="Hucknall Airfield">Hucknall Airfield</a></td>
<td><a href="/wiki/Nottingham" title="Nottingham">Nottingham</a></td>
<td>England
</td></tr>
<tr>
<td>EGNB</td>
<td></td>
<td><a href="/wiki/Brough_Aerodrome" title="Brough Aerodrome">Brough Aerodrome</a></td>
<td><a href="/wiki/Brough,_East_Riding_of_Yorkshire" title="Brough, East Riding of Yorkshire">Brough</a></td>
<td>England
</td></tr>
<tr>
<td>EGNC</td>
<td>CAX</td>
<td><a href="/wiki/Carlisle_Lake_District_Airport" title="Carlisle Lake District Airport">Carlisle Lake District Airport</a></td>
<td><a href="/wiki/Carlisle" title="Carlisle">Carlisle</a></td>
<td>England
</td></tr>
<tr>
<td>EGND</td>
<td></td>
<td><a href="/wiki/Crosland_Moor_Airfield" title="Crosland Moor Airfield">Crosland Moor Airfield</a></td>
<td><a href="/wiki/Huddersfield" title="Huddersfield">Brough</a></td>
<td>England
</td></tr>
<tr>
<td>EGNE</td>
<td>RGA</td>
<td><a href="/wiki/Gamston_Airport" class="mw-redirect" title="Gamston Airport">Gamston Airport</a></td>
<td><a href="/wiki/Retford" title="Retford">Retford</a></td>
<td>England
</td></tr>
<tr>
<td>EGNF</td>
<td></td>
<td><a href="/wiki/Netherthorpe_Airfield" title="Netherthorpe Airfield">Netherthorpe Airfield</a></td>
<td><a href="/wiki/Worksop" title="Worksop">Worksop</a></td>
<td>England
</td></tr>
<tr>
<td>EGNG</td>
<td></td>
<td><a href="/wiki/Bagby_airfield" class="mw-redirect" title="Bagby airfield">Bagby airfield</a></td>
<td><a href="/wiki/Bagby" title="Bagby">Bagby</a></td>
<td>England
</td></tr>
<tr>
<td>EGNI</td>
<td></td>
<td>Skegness (Ingoldmells)
</td></tr>
<tr>
<td>EGNH</td>
<td>BLK</td>
<td><a href="/wiki/Blackpool_International_Airport" class="mw-redirect" title="Blackpool International Airport">Blackpool International Airport</a></td>
<td><a href="/wiki/Blackpool" title="Blackpool">Blackpool</a></td>
<td>England
</td></tr>
<tr>
<td>EGNJ</td>
<td>HUY</td>
<td><a href="/wiki/Humberside_Airport" title="Humberside Airport">Humberside Airport</a></td>
<td><a href="/wiki/Kingston_upon_Hull" title="Kingston upon Hull">Kingston upon Hull</a></td>
<td>England
</td></tr>
<tr>
<td>EGNL</td>
<td>BWF</td>
<td><a href="/wiki/Barrow/Walney_Island_Airfield" class="mw-redirect" title="Barrow/Walney Island Airfield">Walney Aerodrome</a></td>
<td><a href="/wiki/Barrow-in-Furness" title="Barrow-in-Furness">Barrow-in-Furness</a></td>
<td>England
</td></tr>
<tr>
<td>EGNM</td>
<td>LBA</td>
<td><a href="/wiki/Leeds_Bradford_International_Airport" class="mw-redirect" title="Leeds Bradford International Airport">Leeds Bradford International Airport</a></td>
<td><a href="/wiki/West_Yorkshire" title="West Yorkshire">West Yorkshire</a></td>
<td>England
</td></tr>
<tr>
<td>EGNO</td>
<td>WRT</td>
<td><a href="/wiki/Warton_Aerodrome" title="Warton Aerodrome">Warton Aerodrome</a></td>
<td><a href="/wiki/Warton,_Fylde" title="Warton, Fylde">Warton</a>, <a href="/wiki/Lancashire" title="Lancashire">Lancashire</a></td>
<td>England
</td></tr>
<tr>
<td>EGNR</td>
<td>CEG</td>
<td><a href="/wiki/Hawarden_Airport" title="Hawarden Airport">Hawarden Airport</a></td>
<td><a href="/wiki/Chester" title="Chester">Chester</a></td>
<td>England
</td></tr>
<tr>
<td>EGNS</td>
<td>IOM</td>
<td><a href="/wiki/Isle_of_Man_Airport" title="Isle of Man Airport">Isle of Man Airport</a></td>
<td><a href="/wiki/Isle_of_Man" title="Isle of Man">Isle of Man</a>
</td></tr>
<tr>
<td>EGNT</td>
<td>NCL</td>
<td><a href="/wiki/Newcastle_International_Airport" title="Newcastle International Airport">Newcastle Airport</a></td>
<td><a href="/wiki/Newcastle_upon_Tyne" title="Newcastle upon Tyne">Newcastle upon Tyne</a></td>
<td>England
</td></tr>
<tr>
<td>EGNU</td>
<td></td>
<td><a href="/wiki/Full_Sutton_Airfield" title="Full Sutton Airfield">Full Sutton Airfield</a></td>
<td><a href="/wiki/York" title="York">York</a></td>
<td>England
</td></tr>
<tr>
<td>EGNV</td>
<td>MME</td>
<td><a href="/wiki/Teesside_International_Airport" title="Teesside International Airport">Teesside International Airport</a></td>
<td><a href="/wiki/Tees_Valley" title="Tees Valley">Tees Valley</a></td>
<td>England
</td></tr>
<tr>
<td>EGNW</td>
<td></td>
<td><a href="/wiki/Wickenby_Aerodrome" title="Wickenby Aerodrome">Wickenby Aerodrome</a></td>
<td><a href="/wiki/Lincoln,_Lincolnshire" class="mw-redirect" title="Lincoln, Lincolnshire">Lincoln</a></td>
<td>England
</td></tr>
<tr>
<td>EGNX</td>
<td>EMA</td>
<td><a href="/wiki/East_Midlands_Airport" title="East Midlands Airport">East Midlands Airport</a></td>
<td><a href="/wiki/East_Midlands" title="East Midlands">East Midlands</a></td>
<td>England
</td></tr>
<tr>
<td>EGNY</td>
<td></td>
<td><a href="/wiki/Beverley/Linley_Hill_Airfield" title="Beverley/Linley Hill Airfield">Beverley/Linley Hill Airfield</a></td>
<td><a href="/wiki/Beverley" title="Beverley">Beverley</a></td>
<td>England
</td></tr>
<tr>
<td>EGOA</td>
<td></td>
<td>Aldergrove
</td></tr>
<tr>
<td>EGOB</td>
<td></td>
<td><a href="/wiki/RAF_Burtonwood" title="RAF Burtonwood">RAF Burtonwood</a>
</td></tr>
<tr>
<td>EGOC</td>
<td></td>
<td><a href="/wiki/RAF_Bishops_Court" title="RAF Bishops Court">RAF Bishops Court</a>
</td></tr>
<tr>
<td>EGOD</td>
<td></td>
<td><a href="/wiki/Llanbedr_Airport" title="Llanbedr Airport">Llanbedr Airport</a></td>
<td><a href="/wiki/Llanbedr" title="Llanbedr">Llanbedr</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGOE</td>
<td></td>
<td><a href="/wiki/RAF_Ternhill" class="mw-redirect" title="RAF Ternhill">RAF Ternhill</a></td>
<td><a href="/wiki/Ternhill" title="Ternhill">Ternhill</a></td>
<td>England
</td></tr>
<tr>
<td>EGOJ</td>
<td></td>
<td><a href="/wiki/RAF_Jurby_Head" title="RAF Jurby Head">RAF Jurby Head</a>
</td></tr>
<tr>
<td>EGOM</td>
<td></td>
<td><a href="/wiki/RAF_Spadeadam" title="RAF Spadeadam">RAF Spadeadam</a>
</td></tr>
<tr>
<td>EGOQ</td>
<td></td>
<td><a href="/wiki/RAF_Mona" title="RAF Mona">RAF Mona</a></td>
<td><a href="/wiki/Anglesey" title="Anglesey">Anglesey</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGOS</td>
<td></td>
<td><a href="/wiki/RAF_Shawbury" title="RAF Shawbury">RAF Shawbury</a></td>
<td><a href="/wiki/Shawbury" title="Shawbury">Shawbury</a></td>
<td>England
</td></tr>
<tr>
<td>EGOV</td>
<td>VLY</td>
<td><a href="/wiki/RAF_Valley" title="RAF Valley">RAF Valley</a>/<a href="/wiki/Anglesey_Airport" title="Anglesey Airport">Anglesey Airport</a></td>
<td><a href="/wiki/Anglesey" title="Anglesey">Anglesey</a></td>
<td>Wales
</td></tr>
<tr>
<td>EGOW</td>
<td></td>
<td><a href="/wiki/RAF_Woodvale" title="RAF Woodvale">RAF Woodvale</a></td>
<td><a href="/wiki/Formby" title="Formby">Formby</a></td>
<td>England
</td></tr>
<tr>
<td>EGOY</td>
<td></td>
<td><a href="/wiki/RAF_West_Freugh" title="RAF West Freugh">RAF West Freugh</a>
</td></tr>
<tr>
<td>EGPA</td>
<td>KOI</td>
<td><a href="/wiki/Kirkwall_Airport" title="Kirkwall Airport">Kirkwall Airport</a></td>
<td><a href="/wiki/Kirkwall" title="Kirkwall">Kirkwall</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPB</td>
<td>LSI</td>
<td><a href="/wiki/Sumburgh_Airport" title="Sumburgh Airport">Sumburgh Airport</a></td>
<td><a href="/wiki/Shetland_Islands" class="mw-redirect" title="Shetland Islands">Shetland Islands</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPC</td>
<td>WIC</td>
<td><a href="/wiki/Wick_Airport" title="Wick Airport">Wick Airport</a></td>
<td><a href="/wiki/Wick,_Highland" class="mw-redirect" title="Wick, Highland">Wick</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPD</td>
<td>ABZ</td>
<td><a href="/wiki/Aberdeen_Airport" title="Aberdeen Airport">Aberdeen Airport</a></td>
<td><a href="/wiki/Aberdeen" title="Aberdeen">Aberdeen</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPE</td>
<td>INV</td>
<td><a href="/wiki/Inverness_Airport" title="Inverness Airport">Inverness Airport</a></td>
<td><a href="/wiki/Inverness" title="Inverness">Inverness</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPF</td>
<td>GLA</td>
<td><a href="/wiki/Glasgow_International_Airport" class="mw-redirect" title="Glasgow International Airport">Glasgow International Airport</a></td>
<td><a href="/wiki/Glasgow" title="Glasgow">Glasgow</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPG</td>
<td></td>
<td><a href="/wiki/Cumbernauld_Airport" title="Cumbernauld Airport">Cumbernauld Airport</a></td>
<td><a href="/wiki/Cumbernauld" title="Cumbernauld">Cumbernauld</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPH</td>
<td>EDI</td>
<td><a href="/wiki/Edinburgh_Airport" title="Edinburgh Airport">Edinburgh Airport</a></td>
<td><a href="/wiki/Edinburgh" title="Edinburgh">Edinburgh</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPI</td>
<td>ILY</td>
<td><a href="/wiki/Islay_Airport" title="Islay Airport">Islay Airport</a></td>
<td><a href="/wiki/Islay" title="Islay">Islay</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPJ</td>
<td></td>
<td><a href="/wiki/Fife_Airport" title="Fife Airport">Fife Airport</a></td>
<td><a href="/wiki/Glenrothes" title="Glenrothes">Glenrothes</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPK</td>
<td>PIK</td>
<td><a href="/wiki/Glasgow_Prestwick_International_Airport" class="mw-redirect" title="Glasgow Prestwick International Airport">Glasgow Prestwick International Airport</a></td>
<td><a href="/wiki/Glasgow" title="Glasgow">Glasgow</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPL</td>
<td>BEB</td>
<td><a href="/wiki/Benbecula_Airport" title="Benbecula Airport">Benbecula Airport</a></td>
<td><a href="/wiki/Benbecula" title="Benbecula">Benbecula</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPM</td>
<td>SCS</td>
<td><a href="/wiki/Scatsta_Airport" title="Scatsta Airport">Scatsta Airport</a></td>
<td><a href="/wiki/Lerwick" title="Lerwick">Lerwick</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPN</td>
<td>DND</td>
<td><a href="/wiki/Dundee_Airport" title="Dundee Airport">Dundee Airport</a></td>
<td><a href="/wiki/Dundee" title="Dundee">Dundee</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPO</td>
<td>SYY</td>
<td><a href="/wiki/Stornoway_Airport" title="Stornoway Airport">Stornoway Airport</a></td>
<td><a href="/wiki/Stornoway" title="Stornoway">Stornoway</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPR</td>
<td>BRR</td>
<td><a href="/wiki/Barra_Airport_(Scotland)" class="mw-redirect" title="Barra Airport (Scotland)">Barra Airport</a></td>
<td><a href="/wiki/Barra" title="Barra">Barra</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPS</td>
<td></td>
<td>Peterhead/Longside Heliport
</td></tr>
<tr>
<td>EGPT</td>
<td>PSL</td>
<td><a href="/wiki/Perth_Airport_(Scotland)" title="Perth Airport (Scotland)">Perth Airport (Scotland)</a></td>
<td><a href="/wiki/Perth,_Scotland" title="Perth, Scotland">Perth</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPU</td>
<td>TRE</td>
<td><a href="/wiki/Tiree_Airport" title="Tiree Airport">Tiree Airport</a></td>
<td><a href="/wiki/Tiree" title="Tiree">Tiree</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGPW</td>
<td>UNT</td>
<td><a href="/wiki/Unst_Airport" title="Unst Airport">Unst Airport</a></td>
<td><a href="/wiki/Shetland_Islands" class="mw-redirect" title="Shetland Islands">Shetland Islands</a></td>
<td>Scotland
</td></tr>
<tr>
<td><s>EGPY</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Dounreay" title="RAF Dounreay">RAF Dounreay</a></s></td>
<td>North Scotland
</td></tr>
<tr>
<td>EGQA</td>
<td></td>
<td><a href="/wiki/Tain_Air_Weapons_Range" title="Tain Air Weapons Range">Tain</a>
</td></tr>
<tr>
<td><s>EGQB</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Ballykelly" title="RAF Ballykelly">RAF Ballykelly</a></s>
</td></tr>
<tr>
<td>EGQC</td>
<td></td>
<td>Garvie Island
</td></tr>
<tr>
<td>EGQD</td>
<td></td>
<td>Lisburn
</td></tr>
<tr>
<td><s>EGQJ</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Machrihanish" title="RAF Machrihanish">RAF Machrihanish</a></s></td>
<td></td>
<td></td>
<td>later Campbeltown Airport - EGEC
</td></tr>
<tr>
<td>EGQK</td>
<td>FSS</td>
<td><a href="/wiki/RAF_Kinloss" title="RAF Kinloss">RAF Kinloss</a></td>
<td><a href="/wiki/Kinloss,_Scotland" title="Kinloss, Scotland">Kinloss</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGQL</td>
<td>ADX</td>
<td><a href="/wiki/RAF_Leuchars" title="RAF Leuchars">RAF Leuchars</a></td>
<td><a href="/wiki/Leuchars" title="Leuchars">Leuchars</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGQM</td>
<td></td>
<td><a href="/wiki/RAF_Boulmer" title="RAF Boulmer">RAF Boulmer</a></td>
<td><a href="/wiki/Alnwick" title="Alnwick">Alnwick</a></td>
<td>England
</td></tr>
<tr>
<td>EGQS</td>
<td>LMO</td>
<td><a href="/wiki/RAF_Lossiemouth" title="RAF Lossiemouth">RAF Lossiemouth</a></td>
<td><a href="/wiki/Lossiemouth" title="Lossiemouth">Lossiemouth</a></td>
<td>Scotland
</td></tr>
<tr>
<td>EGSA</td>
<td></td>
<td><a href="/wiki/RAF_Shipdham" title="RAF Shipdham">Shipdham Airfield</a></td>
<td><a href="/wiki/Shipdham" title="Shipdham">Shipdham</a></td>
<td>England</td>
<td>formerly RAF Shipdham
</td></tr>
<tr>
<td>EGSB</td>
<td></td>
<td><a href="/w/index.php?title=Castle_Mill_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Castle Mill Airfield (page does not exist)">Castle Mill Airfield</a></td>
<td><a href="/wiki/Bedford" title="Bedford">Bedford</a></td>
<td>England
</td></tr>
<tr>
<td>EGSC</td>
<td>CBG</td>
<td><a href="/wiki/Cambridge_Airport" class="mw-redirect" title="Cambridge Airport">Cambridge Airport</a></td>
<td><a href="/wiki/Cambridge" title="Cambridge">Cambridge</a></td>
<td>England
</td></tr>
<tr>
<td>EGSD</td>
<td></td>
<td><a href="/wiki/Great_Yarmouth_%E2%80%93_North_Denes_Airport" title="Great Yarmouth – North Denes Airport">Great Yarmouth – North Denes Airport</a></td>
<td><a href="/wiki/Great_Yarmouth" title="Great Yarmouth">Great Yarmouth</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGSE</s></td>
<td><s>IPW</s></td>
<td><s><a href="/wiki/Ipswich_Airport" title="Ipswich Airport">Ipswich Airport</a></s></td>
<td><a href="/wiki/Ipswich" title="Ipswich">Ipswich</a></td>
<td>England</td>
<td>closed 1998
</td></tr>
<tr>
<td>EGSF</td>
<td></td>
<td><a href="/wiki/Peterborough_Business_Airport" title="Peterborough Business Airport">Peterborough Business Airport</a></td>
<td><a href="/wiki/Peterborough" title="Peterborough">Peterborough</a></td>
<td>England
</td></tr>
<tr>
<td>EGSG</td>
<td></td>
<td><a href="/wiki/Stapleford_Aerodrome" title="Stapleford Aerodrome">Stapleford Aerodrome</a></td>
<td><a href="/wiki/Romford" title="Romford">Romford</a></td>
<td>England
</td></tr>
<tr>
<td>EGSH</td>
<td>NWI</td>
<td><a href="/wiki/Norwich_International_Airport" class="mw-redirect" title="Norwich International Airport">Norwich International Airport</a></td>
<td><a href="/wiki/Norwich" title="Norwich">Norwich</a></td>
<td>England
</td></tr>
<tr>
<td>EGSI</td>
<td></td>
<td>Marshland Airfield
</td></tr>
<tr>
<td>EGSJ</td>
<td></td>
<td><a href="/wiki/Seething_Airfield" title="Seething Airfield">Seething Airfield</a></td>
<td><a href="/wiki/Norwich" title="Norwich">Norwich</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGSK</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Hethel" title="RAF Hethel">Hethel Airfield</a></s></td>
<td><a href="/wiki/Hethel" title="Hethel">Hethel</a></td>
<td>England</td>
<td>closed 1948
</td></tr>
<tr>
<td>EGSL</td>
<td></td>
<td><a href="/wiki/Andrewsfield_aerodrome" class="mw-redirect" title="Andrewsfield aerodrome">Andrewsfield aerodrome</a></td>
<td><a href="/wiki/Braintree,_Essex" title="Braintree, Essex">Braintree</a></td>
<td>England
</td></tr>
<tr>
<td>EGSM</td>
<td></td>
<td><a href="/wiki/Beccles_Airport" class="mw-redirect" title="Beccles Airport">Beccles Airport</a></td>
<td><a href="/wiki/Beccles" title="Beccles">Beccles</a></td>
<td>England
</td></tr>
<tr>
<td>EGSN</td>
<td></td>
<td><a href="/wiki/Bourn_Airfield" title="Bourn Airfield">Bourn Airfield</a></td>
<td><a href="/wiki/Cambridge" title="Cambridge">Cambridge</a></td>
<td>England
</td></tr>
<tr>
<td>EGSO</td>
<td></td>
<td><a href="/wiki/Crowfield_Airfield" title="Crowfield Airfield">Crowfield Airfield</a></td>
<td><a href="/wiki/Ipswich" title="Ipswich">Ipswich</a></td>
<td>England
</td></tr>
<tr>
<td>EGSP</td>
<td></td>
<td><a href="/wiki/Peterborough/Sibson_Airfield" title="Peterborough/Sibson Airfield">Peterborough/Sibson Airfield</a></td>
<td><a href="/wiki/Peterborough" title="Peterborough">Peterborough</a></td>
<td>England
</td></tr>
<tr>
<td>EGSQ</td>
<td></td>
<td><a href="/wiki/Clacton_Airport" title="Clacton Airport">Clacton Airport</a></td>
<td><a href="/wiki/Clacton-on-Sea" title="Clacton-on-Sea">Clacton-on-Sea</a></td>
<td>England
</td></tr>
<tr>
<td>EGSR</td>
<td></td>
<td><a href="/wiki/Earls_Colne_Airfield" title="Earls Colne Airfield">Earls Colne Airfield</a></td>
<td><a href="/wiki/Halstead" title="Halstead">Halstead</a></td>
<td>England
</td></tr>
<tr>
<td>EGSS</td>
<td>STN</td>
<td><a href="/wiki/London_Stansted_Airport" title="London Stansted Airport">London Stansted Airport</a></td>
<td><a href="/wiki/London" title="London">London</a></td>
<td>England
</td></tr>
<tr>
<td>EGST</td>
<td></td>
<td><a href="/w/index.php?title=Elmsett_Airport&amp;action=edit&amp;redlink=1" class="new" title="Elmsett Airport (page does not exist)">Elmsett Airport</a></td>
<td><a href="/wiki/Ipswich" title="Ipswich">Ipswich</a></td>
<td>England
</td></tr>
<tr>
<td>EGSU</td>
<td></td>
<td><a href="/wiki/Duxford_Aerodrome" title="Duxford Aerodrome">Duxford Aerodrome</a></td>
<td><a href="/wiki/Cambridge" title="Cambridge">Cambridge</a></td>
<td>England
</td></tr>
<tr>
<td>EGSV</td>
<td></td>
<td><a href="/wiki/Old_Buckenham_Airport" class="mw-redirect" title="Old Buckenham Airport">Old Buckenham Airport</a></td>
<td><a href="/wiki/Norwich" title="Norwich">Norwich</a></td>
<td>England
</td></tr>
<tr>
<td>EGSW</td>
<td></td>
<td><a href="/w/index.php?title=Newmarket_Heath_Airfield&amp;action=edit&amp;redlink=1" class="new" title="Newmarket Heath Airfield (page does not exist)">Newmarket Heath Airfield</a>
</td></tr>
<tr>
<td>EGSX</td>
<td></td>
<td><a href="/wiki/North_Weald_Airfield" title="North Weald Airfield">North Weald Airfield</a></td>
<td><a href="/wiki/North_Weald" class="mw-redirect" title="North Weald">North Weald</a></td>
<td>England
</td></tr>
<tr>
<td>EGSY</td>
<td></td>
<td><a href="/wiki/RAF_Saint_Athan" class="mw-redirect" title="RAF Saint Athan">MoD Saint Athan</a></td>
<td><a href="/wiki/St_Athan" title="St Athan">St Athan</a></td>
<td>Wales</td>
<td>formerly <a href="/wiki/Sheffield_City_Airport" title="Sheffield City Airport">Sheffield City Airport</a> until 2008; code reassigned April 2019
</td></tr>
<tr>
<td><s>EGTA</s></td>
<td></td>
<td><s>Aylesbury Thame Airfield</s></td>
<td><a href="/wiki/Aylesbury" title="Aylesbury">Aylesbury</a></td>
<td>England
</td></tr>
<tr>
<td>EGTB</td>
<td>HYC</td>
<td><a href="/wiki/Wycombe_Air_Park/Booker_Airport" class="mw-redirect" title="Wycombe Air Park/Booker Airport">Wycombe Air Park/Booker Airport</a></td>
<td><a href="/wiki/High_Wycombe" title="High Wycombe">High Wycombe</a></td>
<td>England
</td></tr>
<tr>
<td>EGTC</td>
<td></td>
<td><a href="/wiki/Cranfield_Airport" title="Cranfield Airport">Cranfield Airport</a></td>
<td><a href="/wiki/Cranfield" title="Cranfield">Cranfield</a></td>
<td>England
</td></tr>
<tr>
<td>EGTD</td>
<td></td>
<td><a href="/wiki/Dunsfold_Aerodrome" title="Dunsfold Aerodrome">Dunsfold Aerodrome</a></td>
<td><a href="/wiki/Dunsfold" title="Dunsfold">Dunsfold</a></td>
<td>England
</td></tr>
<tr>
<td>EGTE</td>
<td>EXT</td>
<td><a href="/wiki/Exeter_International_Airport" class="mw-redirect" title="Exeter International Airport">Exeter International Airport</a></td>
<td><a href="/wiki/Exeter" title="Exeter">Exeter</a></td>
<td>England
</td></tr>
<tr>
<td>EGTF</td>
<td></td>
<td><a href="/wiki/Fairoaks_Airport" title="Fairoaks Airport">Fairoaks Airport</a></td>
<td><a href="/wiki/Chobham,_Surrey" class="mw-redirect" title="Chobham, Surrey">Chobham</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGTG</s></td>
<td><s>FZO</s></td>
<td><s><a href="/wiki/Bristol_Filton_Airport" title="Bristol Filton Airport">Bristol Filton Airport</a></s></td>
<td><a href="/wiki/Filton" title="Filton">Filton</a></td>
<td>England</td>
<td>closed 2012
</td></tr>
<tr>
<td><s>EGTH</s></td>
<td><s>HTF</s></td>
<td><s><a href="/wiki/Hatfield_Aerodrome" title="Hatfield Aerodrome">Hatfield Aerodrome</a></s></td>
<td><a href="/wiki/Hatfield,_Hertfordshire" title="Hatfield, Hertfordshire">Hatfield</a></td>
<td>England</td>
<td>closed 1994
</td></tr>
<tr>
<td>EGTH</td>
<td></td>
<td><a href="/wiki/Old_Warden_Aerodrome" title="Old Warden Aerodrome">Old Warden Aerodrome</a></td>
<td><a href="/wiki/Old_Warden" title="Old Warden">Old Warden</a>, <a href="/wiki/Bedfordshire" title="Bedfordshire">Bedfordshire</a></td>
<td>England</td>
<td>reallocated from <a href="/wiki/Hatfield_Aerodrome" title="Hatfield Aerodrome">Hatfield Aerodrome</a>
</td></tr>
<tr>
<td><s>EGTI</s></td>
<td></td>
<td><s><a href="/wiki/Leavesden_Aerodrome" class="mw-redirect" title="Leavesden Aerodrome">Leavesden Aerodrome</a></s></td>
<td><a href="/wiki/Watford" title="Watford">Watford</a></td>
<td>England</td>
<td>closed 1990s
</td></tr>
<tr>
<td>EGTK</td>
<td>OXF</td>
<td><a href="/wiki/Oxford_Airport" title="Oxford Airport">Oxford Airport</a></td>
<td><a href="/wiki/Oxford" title="Oxford">Oxford</a></td>
<td>England
</td></tr>
<tr>
<td>EGTN</td>
<td></td>
<td><a href="/wiki/Enstone_Airfield" title="Enstone Airfield">Enstone Airfield</a></td>
<td><a href="/wiki/Enstone" title="Enstone">Enstone</a></td>
<td>England
</td></tr>
<tr>
<td>EGTO</td>
<td>RCS</td>
<td><a href="/wiki/Rochester_Airport,_England" class="mw-redirect" title="Rochester Airport, England">Rochester Airport, England</a></td>
<td><a href="/wiki/Rochester,_Kent" title="Rochester, Kent">Rochester</a></td>
<td>England
</td></tr>
<tr>
<td>EGTP</td>
<td></td>
<td><a href="/wiki/Perranporth_Airfield" title="Perranporth Airfield">Perranporth Airfield</a></td>
<td><a href="/wiki/Perranporth" title="Perranporth">Perranporth</a></td>
<td>England
</td></tr>
<tr>
<td>EGTR</td>
<td></td>
<td><a href="/wiki/Elstree_Airfield" class="mw-redirect" title="Elstree Airfield">Elstree Airfield</a></td>
<td><a href="/wiki/Watford" title="Watford">Watford</a></td>
<td>England
</td></tr>
<tr>
<td>EGTU</td>
<td></td>
<td><a href="/wiki/Dunkeswell_Aerodrome" title="Dunkeswell Aerodrome">Dunkeswell Aerodrome</a></td>
<td><a href="/wiki/Honiton" title="Honiton">Honiton</a></td>
<td>England
</td></tr>
<tr>
<td>EGTW</td>
<td></td>
<td><a href="/w/index.php?title=Oaksey_Park_Airport&amp;action=edit&amp;redlink=1" class="new" title="Oaksey Park Airport (page does not exist)">Oaksey Park Airport</a></td>
<td><a href="/wiki/Oaksey" title="Oaksey">Oaksey</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGUA</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Upper_Heyford" title="RAF Upper Heyford">RAF Upper Heyford</a></s></td>
<td>Oxfordshire</td>
<td>England</td>
<td>closed 1993
</td></tr>
<tr>
<td>EGUB</td>
<td>BEX</td>
<td><a href="/wiki/RAF_Benson" title="RAF Benson">RAF Benson</a></td>
<td><a href="/wiki/Benson,_Oxfordshire" title="Benson, Oxfordshire">Benson</a></td>
<td>England
</td></tr>
<tr>
<td>EGUD</td>
<td>ABB</td>
<td><a href="/wiki/RAF_Abingdon" title="RAF Abingdon">RAF Abingdon</a></td>
<td><a href="/wiki/Abingdon,_Oxfordshire" class="mw-redirect" title="Abingdon, Oxfordshire">Abingdon</a></td>
<td>England
</td></tr>
<tr>
<td>EGUK</td>
<td></td>
<td><a href="/wiki/RAF_Waterbeach" title="RAF Waterbeach">RAF Waterbeach</a>
</td></tr>
<tr>
<td>EGUL</td>
<td>LKZ</td>
<td><a href="/wiki/RAF_Lakenheath" title="RAF Lakenheath">RAF Lakenheath</a></td>
<td><a href="/wiki/Lakenheath" title="Lakenheath">Lakenheath</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGUM</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Manston" title="RAF Manston">RAF Manston</a></s>
</td></tr>
<tr>
<td>EGUN</td>
<td>MHZ</td>
<td><a href="/wiki/RAF_Mildenhall" title="RAF Mildenhall">RAF Mildenhall</a></td>
<td><a href="/wiki/Mildenhall,_Suffolk" title="Mildenhall, Suffolk">Mildenhall</a></td>
<td>England
</td></tr>
<tr>
<td>EGUO</td>
<td></td>
<td><a href="/wiki/Colerne_Airfield" title="Colerne Airfield">Colerne Airfield</a></td>
<td><a href="/wiki/Colerne" title="Colerne">Colerne</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGUP</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Sculthorpe" class="mw-redirect" title="RAF Sculthorpe">RAF Sculthorpe</a></s></td>
<td><a href="/wiki/Fakenham" title="Fakenham">Fakenham</a></td>
<td>England</td>
<td>closed in the 1990s
</td></tr>
<tr>
<td>EGUU</td>
<td></td>
<td><a href="/wiki/RAF_Uxbridge" title="RAF Uxbridge">RAF Uxbridge</a>
</td></tr>
<tr>
<td>EGUW</td>
<td></td>
<td><a href="/wiki/RAF_Wattisham" title="RAF Wattisham">RAF Wattisham</a></td>
<td><a href="/wiki/Stowmarket" title="Stowmarket">Stowmarket</a></td>
<td>England
</td></tr>
<tr>
<td>EGUY</td>
<td>QUY</td>
<td><a href="/wiki/RAF_Wyton" title="RAF Wyton">RAF Wyton</a></td>
<td><a href="/wiki/St_Ives,_Cambridgeshire" title="St Ives, Cambridgeshire">St Ives</a></td>
<td>England
</td></tr>
<tr>
<td>EGVA</td>
<td>FFD</td>
<td><a href="/wiki/RAF_Fairford" title="RAF Fairford">RAF Fairford</a></td>
<td><a href="/wiki/Fairford" title="Fairford">Fairford</a></td>
<td>England
</td></tr>
<tr>
<td>EGVB</td>
<td></td>
<td><a href="/wiki/RAF_Bawdsey" title="RAF Bawdsey">RAF Bawdsey</a>
</td></tr>
<tr>
<td>EGVF</td>
<td></td>
<td><a href="/wiki/Fleetlands_Heliport" title="Fleetlands Heliport">Fleetlands Heliport</a>
</td></tr>
<tr>
<td>EGVG</td>
<td></td>
<td><a href="/wiki/RAF_Woodbridge" title="RAF Woodbridge">RAF Woodbridge</a>
</td></tr>
<tr>
<td>EGVH</td>
<td></td>
<td><a href="/wiki/RAF_Credenhill" title="RAF Credenhill">RAF Credenhill</a> (RAF Hereford)
</td></tr>
<tr>
<td>EGVI</td>
<td></td>
<td><a href="/wiki/RAF_Greenham_Common" title="RAF Greenham Common">RAF Greenham Common</a>
</td></tr>
<tr>
<td>EGVJ</td>
<td></td>
<td><a href="/wiki/RAF_Bentwaters" title="RAF Bentwaters">RAF Bentwaters</a>
</td></tr>
<tr>
<td>EGVL</td>
<td></td>
<td><a href="/wiki/RAF_Little_Rissington" title="RAF Little Rissington">RAF Little Rissington</a></td>
<td><a href="/wiki/Upper_Rissington" title="Upper Rissington">Upper Rissington</a></td>
<td>England
</td></tr>
<tr>
<td>EGVN</td>
<td>BZZ</td>
<td><a href="/wiki/RAF_Brize_Norton" title="RAF Brize Norton">RAF Brize Norton</a></td>
<td><a href="/wiki/Brize_Norton" title="Brize Norton">Brize Norton</a></td>
<td>England
</td></tr>
<tr>
<td>EGVO</td>
<td>ODH</td>
<td><a href="/wiki/RAF_Odiham" title="RAF Odiham">RAF Odiham</a></td>
<td><a href="/wiki/Odiham" title="Odiham">Odiham</a></td>
<td>England
</td></tr>
<tr>
<td>EGVP</td>
<td></td>
<td><a href="/wiki/AAC_Middle_Wallop" title="AAC Middle Wallop">AAC Middle Wallop</a></td>
<td><a href="/wiki/Andover,_Hampshire" title="Andover, Hampshire">Andover</a></td>
<td>England
</td></tr>
<tr>
<td>EGVW</td>
<td></td>
<td><a href="/wiki/RAE_Bedford" title="RAE Bedford">RAE Bedford</a>
</td></tr>
<tr>
<td><s>EGWA</s></td>
<td><s>ADV</s></td>
<td><s><a href="/wiki/RAF_Andover" title="RAF Andover">RAF Andover</a></s></td>
<td><a href="/wiki/Andover,_Hampshire" title="Andover, Hampshire">Andover</a></td>
<td>England</td>
<td>closed in the 2000s
</td></tr>
<tr>
<td>EGWC</td>
<td></td>
<td><a href="/wiki/RAF_Cosford" title="RAF Cosford">RAF Cosford</a></td>
<td><a href="/wiki/Albrighton,_Bridgnorth" class="mw-redirect" title="Albrighton, Bridgnorth">Albrighton</a></td>
<td>England
</td></tr>
<tr>
<td>EGWE</td>
<td></td>
<td><a href="/wiki/RAF_Henlow" title="RAF Henlow">RAF Henlow</a></td>
<td><a href="/wiki/Henlow" title="Henlow">Henlow</a></td>
<td>England
</td></tr>
<tr>
<td>EGWL</td>
<td></td>
<td><a href="/wiki/RAF_North_Luffenham" title="RAF North Luffenham">RAF North Luffenham</a>
</td></tr>
<tr>
<td>EGWN</td>
<td></td>
<td><a href="/wiki/RAF_Halton" title="RAF Halton">RAF Halton</a></td>
<td><a href="/wiki/Halton,_Buckinghamshire" title="Halton, Buckinghamshire">Halton</a></td>
<td>England
</td></tr>
<tr>
<td>EGWR</td>
<td></td>
<td><a href="/wiki/RAF_Croughton" title="RAF Croughton">RAF Croughton</a>
</td></tr>
<tr>
<td>EGWU</td>
<td>NHT</td>
<td><a href="/wiki/RAF_Northolt" title="RAF Northolt">RAF Northolt</a></td>
<td><a href="/wiki/Ruislip" title="Ruislip">Ruislip</a></td>
<td>England
</td></tr>
<tr>
<td>EGWZ</td>
<td></td>
<td><a href="/wiki/RAF_Alconbury" title="RAF Alconbury">RAF Alconbury</a>
</td></tr>
<tr>
<td>EGXB</td>
<td></td>
<td><a href="/wiki/RAF_Binbrook" title="RAF Binbrook">RAF Binbrook</a>
</td></tr>
<tr>
<td>EGXC</td>
<td>QCY</td>
<td><a href="/wiki/RAF_Coningsby" title="RAF Coningsby">RAF Coningsby</a></td>
<td><a href="/wiki/Coningsby" title="Coningsby">Coningsby</a></td>
<td>England
</td></tr>
<tr>
<td>EGXD</td>
<td></td>
<td><a href="/wiki/RAF_Dishforth" title="RAF Dishforth">RAF Dishforth</a></td>
<td><a href="/wiki/North_Yorkshire" title="North Yorkshire">North Yorkshire</a></td>
<td>England
</td></tr>
<tr>
<td>EGXE</td>
<td></td>
<td><a href="/wiki/RAF_Leeming" title="RAF Leeming">RAF Leeming</a></td>
<td><a href="/wiki/Leeming_Bar" title="Leeming Bar">Leeming Bar</a></td>
<td>England
</td></tr>
<tr>
<td>EGXF</td>
<td></td>
<td>Forest Moor
</td></tr>
<tr>
<td>EGXG</td>
<td></td>
<td><a href="/wiki/RAF_Church_Fenton" title="RAF Church Fenton">RAF Church Fenton</a></td>
<td><a href="/wiki/Church_Fenton" title="Church Fenton">Church Fenton</a></td>
<td>England
</td></tr>
<tr>
<td>EGXH</td>
<td>BEQ</td>
<td><a href="/wiki/RAF_Honington" title="RAF Honington">RAF Honington</a></td>
<td><a href="/wiki/Thetford" title="Thetford">Thetford</a></td>
<td>England
</td></tr>
<tr>
<td>EGXI</td>
<td></td>
<td><a href="/wiki/RAF_Finningley" title="RAF Finningley">RAF Finningley</a>
</td></tr>
<tr>
<td><s>EGXJ</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Cottesmore" title="RAF Cottesmore">RAF Cottesmore</a></s></td>
<td><a href="/wiki/Rutland" title="Rutland">Rutland</a></td>
<td>England</td>
<td>closed 2012
</td></tr>
<tr>
<td><s>EGXN</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Newton" title="RAF Newton">RAF Newton</a></s>
</td></tr>
<tr>
<td>EGXP</td>
<td>SQZ</td>
<td><a href="/wiki/RAF_Scampton" title="RAF Scampton">RAF Scampton</a></td>
<td><a href="/wiki/Scampton" title="Scampton">Scampton</a></td>
<td>England
</td></tr>
<tr>
<td>EGXT</td>
<td></td>
<td><a href="/wiki/RAF_Wittering" title="RAF Wittering">RAF Wittering</a></td>
<td><a href="/wiki/Stamford,_Lincolnshire" title="Stamford, Lincolnshire">Stamford</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGXU</s></td>
<td><s>HRT</s></td>
<td><s> <a href="/wiki/RAF_Linton-on-Ouse" title="RAF Linton-on-Ouse">RAF Linton-on-Ouse</a> </s></td>
<td><a href="/wiki/Linton-on-Ouse" title="Linton-on-Ouse">Linton-on-Ouse</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGXV</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Leconfield" title="RAF Leconfield">RAF Leconfield</a></s>
</td></tr>
<tr>
<td>EGXW</td>
<td>WTN</td>
<td><a href="/wiki/RAF_Waddington" title="RAF Waddington">RAF Waddington</a></td>
<td><a href="/wiki/Waddington,_Lincolnshire" title="Waddington, Lincolnshire">Waddington</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGXX</s></td>
<td></td>
<td><s><a href="/wiki/RAF_Donna_Nook" class="mw-redirect" title="RAF Donna Nook">RAF Donna Nook</a></s>
</td></tr>
<tr>
<td>EGXY</td>
<td></td>
<td><a href="/wiki/RAF_Syerston" title="RAF Syerston">RAF Syerston</a></td>
<td><a href="/wiki/Newark-on-Trent" title="Newark-on-Trent">Newark-on-Trent</a></td>
<td>England
</td></tr>
<tr>
<td>EGXZ</td>
<td></td>
<td><a href="/wiki/RAF_Topcliffe" title="RAF Topcliffe">RAF Topcliffe</a></td>
<td><a href="/wiki/Topcliffe,_North_Yorkshire" title="Topcliffe, North Yorkshire">Topcliffe</a></td>
<td>England
</td></tr>
<tr>
<td><s>EGYC</s></td>
<td><s>CLF</s></td>
<td><s><a href="/wiki/RAF_Coltishall" title="RAF Coltishall">RAF Coltishall</a></s></td>
<td><a href="/wiki/Norwich" title="Norwich">Norwich</a></td>
<td>England</td>
<td>closed 2006
</td></tr>
<tr>
<td>EGYD</td>
<td></td>
<td><a href="/wiki/RAF_Cranwell" title="RAF Cranwell">RAF Cranwell</a></td>
<td><a href="/wiki/Cranwell" title="Cranwell">Cranwell</a></td>
<td>England
</td></tr>
<tr>
<td>EGYE</td>
<td></td>
<td><a href="/wiki/RAF_Barkston_Heath" title="RAF Barkston Heath">RAF Barkston Heath</a></td>
<td><a href="/wiki/Grantham" title="Grantham">Grantham</a></td>
<td>England
</td></tr>
<tr>
<td>EGYH</td>
<td></td>
<td><a href="/wiki/RAF_Holbeach" class="mw-redirect" title="RAF Holbeach">RAF Holbeach</a></td>
<td>Dawsmere</td>
<td>England
</td></tr>
<tr>
<td>EGYM</td>
<td>KNF</td>
<td><a href="/wiki/RAF_Marham" title="RAF Marham">RAF Marham</a></td>
<td><a href="/wiki/Marham" title="Marham">Marham</a></td>
<td>England
</td></tr>
<tr>
<td>EGYP</td>
<td></td>
<td>MPN</td>
<td><a href="/wiki/RAF_Mount_Pleasant" title="RAF Mount Pleasant">RAF Mount Pleasant</a></td>
<td><a href="/wiki/Falkland_Islands" title="Falkland Islands">Falkland Islands</a>
</td></tr></tbody></table>
'''

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'wikitable', 'style': 'width:auto;'})

with open("EG – United Kingdom (and British Crown dependencies).csv", mode='w', newline='', encoding='utf-8') as csv_file:
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