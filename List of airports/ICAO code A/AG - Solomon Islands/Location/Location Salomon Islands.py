import pandas as pd

# Copiez-collez les données fournies dans votre question
data = """

Airport name	Location	Province	ICAO	IATA
Balalae, Shortland Island	Western	AGGE	BAS	Balalae Airport
Barora, New Georgia Island	Western		RRI	Barora Airport
Batuna, Vangunu Island	Western	AGBT	BPF	Batuna Airport
Gatokae (Nggatokae Island), New Georgia Islands	Western	AGOK	GTA	Gatokae Aerodrome (Gatokae Airport)
Geva, Vella Lavella Island	Western	AGEV	GEF	Geva Airport
Gizo, Ghizo Island	Western	AGGN	GZO	Nusatupe Airport (Gizo Airport)
Kukudu (Kukundu), Kolombangara	Western	AGKU	KUE	Kukudu Airport
Mono Island, Treasury Islands	Western	AGGO	MNY	Mono Airport
Munda, New Georgia Island	Western	AGGM	MUA	Munda Airport
Ramata Airport (Ramata Island)	Western	AGRM	RBV	Ramata Airport (Ramata Island Airstrip)
Ringgi Cove, Kolombangara	Western	AGRC	RIN	Ringgi Cove Airport[1] (Vila Airport)
Seghe, New Georgia Island	Western	AGGS	EGM	Seghe Airport
Viru, New Georgia Island	Western		VIU	Viru Airport (Viru Harbour Airstrip)
Lomlom, Reef Islands	Temotu	AGLM	LLM	Lomlom Airport
Santa Cruz Islands, Nendo Island	Temotu	AGGL	SCZ	Luova Airport (Santa Cruz Airport)
Anua, Bellona Island	Rennell and Bellona	AGGB	BNY	Bellona/Anua Airport
Tingoa, Rennell Island	Rennell and Bellona	AGGR	RNL	Rennell/Tingoa Airport
Afutara, Malaita Island	Malaita	AGAF	AFT	Afutara Airport
Atoifi, Malaita Island	Malaita	AGAT	ATD	Uru Harbour Airport (Atoifi Airport)
Auki, Malaita Island	Malaita	AGGA	AKS	Auki Gwaunaru'u Airport
Kwai Harbour	Malaita		KWR	Kwai Harbour Airport
Onepusu	Malaita		ONE	Onepusu Airport
Ontong Java	Malaita	AGGQ		Ontong Java Airport
Parasi	Malaita		PRS	Parasi Airport
Tarapaina	Malaita		TAA	Tarapaina Airport
Arona, Ulawa Island	Makira-Ulawa	AGAR	RNA	Ulawa Airport (Arona Airport)
Kirakira, Makira Island	Makira-Ulawa	AGGK	IRA	Kirakira Airport (Ngorangora Airstrip)
Santa Ana Island (Owaraha)	Makira-Ulawa	AGGT	NNB	Santa Ana Airport
Maringe, Fera Island (near Santa Isabel Island)	Isabel	AGGF	FRE	Fera Airport (Fera/Maringe Airport)
Suavanao, Santa Isabel Island	Isabel	AGGV	VAO	Suavanao Airport
Avu Avu	Guadalcanal	AGGJ	AVU	Avu Avu Airport
Honiara, Guadalcanal Island	Guadalcanal	AGGH	HIR	Honiara International Airport (formerly Henderson Field)
Marau, Guadalcanal Island	Guadalcanal	AGGU	RUS	Marau Airport
Parasi, Marau Sound Island	Guadalcanal	AGGP	PRS	Marau Airport (Parasi Airport)
Mbambanakira, Guadalcanal Island	Guadalcanal	AGGI	MBU	Mbambanakira Airport (Babanakira Airfield)
Choiseul Bay, Taro Island	Choiseul	AGGC	CHY	Choiseul Bay Airport
Kaghau Island	Choiseul	AGKG	KGE	Kaghau Airport
Yandina, Mbanika Island, Russell Islands	Central Province	AGGY	XYA	Yandina Airport
Anuha Island, Nggela Islands	Central		ANH	Anuha Airport
Savo Island	Central		SVY	Savo Airport
Tulagi Island (Tulaghi)	Central		TLG	Tulagi Island Airport
"""

import io
df = pd.read_csv(io.StringIO(data), delimiter='\t')

# Extraire uniquement la colonne "Location"
locations = df['Location']

# Enregistrer la colonne "Location" dans un fichier CSV
csv_file_path = 'locations Solomon islands.csv'
locations.to_csv(csv_file_path, index=False, header=['Location'])

print(f"Les données de la colonne 'Location' ont été enregistrées dans {csv_file_path}.")