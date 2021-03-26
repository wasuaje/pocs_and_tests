
#! /usr/bin/env python
text="""
PDGNHBOBVPNSNHANAOENCNANHPNCPND,NUOCP
NNPNAPNMSMDKBMLPOWP,NAP,]NEENTGBTMLS
HHSSSTMALHFFTMOFPANSTP,NIOOIPNTPNROA
NTRSANTOTTAPOD,PLUADONNOANPBOOLL,PKUA
SASIMAB,PAGA,]PMOMTAVMAJAMMSSSLLAB
APMUTTCTCCATFGSHHILANRNPHTAOLP,]PST
WAAHASIOLAIOW,PSTWALOJTHTPATP,PSTWA
GAOKWOCWASAPSTWADVGWAIIRARBOSAO,]
PSTWAHPPAAETWW,PSTWAHTPMAESTCWE,]
PSTAOUCOOTIOWHAMPAPSTTPDNHA,PSTWAA
HAS,PAGA,PSTWAAIEHAPSTWARIEH,]PSTTPAI
DNBTVJEOAOU,PAGA,]PSTTOUWWTLWATOUWS
LWDSWGOBS,PSTWAHSAHVASASBTATWARH
SFAOT,PSTWAHBPITNRSTNOTROUHTTBPM,]
PSTVCADAFLAFESJMPLGCBGBMBATROURSSAS
FOHP,]PSTWAGAVWWOA,PAGA]PSTEIFFAWAU.]
TYAGFPFG,TYAGFLTMPAAT,TYAGFE,A-TYAGFE,AAA"""

conocida={"TY":" Thank you",
		  "AGF":" Almighty God for",
		  #"FE" :" for everything",			
		  "OFWAIH":" Our Father who art in Heaven",
		  "HBTN": " hallowed be thy name",
		  "OBS":" only begotten son ",
		  "LTMPAAT":" Thank you Almighty God for listening to my prayers and answering them",
		  "AHAS":" Please see that we are all happy and safe",
		  "PMOM":" peace may overtake me",
		  "TVMAJ":" the virgin mother and jesus",
		   "LOJ":" lamb of jesus",
		   "COOTIOWHAMP":" can overcome our troubles in our world, home, and many places",
		   "PKU":" Please keep us",
		   "ASAS":"  all safe and sound",
		   "HBP" :" Have bodily perfection",
		   "ITNR": " in the next realm",
		   "PST":" Please see that",
		   "PAGA":" praise almighty god amen",
		    "WAGA":" we all get a",
		    "PLU":" Please Love Us" ,
		    "WA":" we all",
		    "IFF":" is free from",
		    "VWW":" victory when we",
		    "WWO":" whereby we offer",
		    "HPP":" his passion prayed",
		    "AET":" and especially to",
		    "TOUW":" those of us who",
		    #"TOUW":" the organic unity with",		    
		    "PDG":" please dear god",
		    "PAI":" pain and illness",
		    "DNB":" does not befall ",
		    "WGOBS":" with God's only begotten son",		    
		    #"NH":" now have",
		     "WAU" :"wisdom and understanding",
		   ",":"\n"
		  }

for i in conocida:
	text=text.replace(i,conocida[i])

print text

