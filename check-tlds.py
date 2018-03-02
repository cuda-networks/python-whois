#!/usr/bin/env python2

# This script will do an IANA lookup for a list of TLDs, and compare the
# response of IANA to the WHOIS server in the list. IANA does not appear to be
# aware of all the new TLDs yet, so this is a quick way to check what TLDs need
# an exception in the WHOIS lookup code.
from __future__ import absolute_import, unicode_literals, print_function

import pythonwhois

# List source: https://superuser.com/a/769448
tld_list = """
\.ac$ whois.nic.ac
\.academy$ whois.donuts.co
\.accountants$ whois.donuts.co
\.active$ whois.afilias-srs.net
\.actor$ whois.unitedtld.com
\.ae$ whois.aeda.net.ae
\.aero$ whois.aero
\.af$ whois.nic.af
\.ag$ whois.nic.ag
\.agency$ whois.donuts.co
\.ai$ whois.ai
\.airforce$ whois.unitedtld.com
\.am$ whois.amnic.net
\.archi$ whois.ksregistry.net
\.army$ whois.rightside.co
\.arpa$ whois.iana.org
\.as$ whois.nic.as
\.asia$ whois.nic.asia
\.associates$ whois.donuts.co
\.at$ whois.nic.at
\.attorney$ whois.rightside.co
\.au$ whois.audns.net.au
\.auction$ whois.unitedtld.com
\.audio$ whois.uniregistry.net
\.autos$ whois.afilias-srs.net
\.aw$ whois.nic.aw
\.ax$ whois.ax
\.bar$ whois.nic.bar
\.bargains$ whois.donuts.co
\.bayern$ whois-dub.mm-registry.com
\.be$ whois.dns.be
\.beer$ whois-dub.mm-registry.com
\.berlin$ whois.nic.berlin
\.best$ whois.nic.best
\.bg$ whois.register.bg
\.bi$ whois1.nic.bi
\.bid$ whois.nic.bid
\.bike$ whois.donuts.co
\.bio$ whois.ksregistry.net
\.biz$ whois.biz
\.bj$ whois.nic.bj
\.black$ whois.afilias.net
\.blackfriday$ whois.uniregistry.net
\.blue$ whois.afilias.net
\.bmw$ whois.ksregistry.net
\.bn$ whois.bn
\.bnpparibas$ whois.afilias-srs.net
\.bo$ whois.nic.bo
\.boutique$ whois.donuts.co
\.br$ whois.registro.br
\.brussels$ whois.nic.brussels
\.build$ whois.nic.build
\.builders$ whois.donuts.co
\.business$ whois.donuts.co
\.bw$ whois.nic.net.bw
\.by$ whois.cctld.by
\.bzh$ whois-bzh.nic.fr
\.ca$ whois.cira.ca
\.cab$ whois.donuts.co
\.camera$ whois.donuts.co
\.camp$ whois.donuts.co
\.cancerresearch$ whois.nic.cancerresearch
\.capetown$ capetown-whois.registry.net.za
\.capital$ whois.donuts.co
\.cards$ whois.donuts.co
\.care$ whois.donuts.co
\.career$ whois.nic.career
\.careers$ whois.donuts.co
\.cash$ whois.donuts.co
\.cat$ whois.cat
\.catering$ whois.donuts.co
\.cc$ ccwhois.verisign-grs.com
\.center$ whois.donuts.co
\.ceo$ whois.nic.ceo
\.cern$ whois.afilias-srs.net
\.cf$ whois.dot.cf
\.ch$ whois.nic.ch
\.cheap$ whois.donuts.co
\.christmas$ whois.uniregistry.net
\.church$ whois.donuts.co
\.ci$ whois.nic.ci
\.city$ whois.donuts.co
\.cl$ whois.nic.cl
\.claims$ whois.donuts.co
\.cleaning$ whois.donuts.co
\.click$ whois.uniregistry.net
\.clinic$ whois.donuts.co
\.clothing$ whois.donuts.co
\.club$ whois.nic.club
\.cn$ whois.cnnic.cn
\.co$ whois.nic.co
\.codes$ whois.donuts.co
\.coffee$ whois.donuts.co
\.college$ whois.centralnic.com
\.cologne$ whois-fe1.pdt.cologne.tango.knipp.de
\.com$ whois.verisign-grs.com
\.community$ whois.donuts.co
\.company$ whois.donuts.co
\.computer$ whois.donuts.co
\.condos$ whois.donuts.co
\.construction$ whois.donuts.co
\.consulting$ whois.unitedtld.com
\.contractors$ whois.donuts.co
\.cooking$ whois-dub.mm-registry.com
\.cool$ whois.donuts.co
\.coop$ whois.nic.coop
\.country$ whois-dub.mm-registry.com
\.credit$ whois.donuts.co
\.creditcard$ whois.donuts.co
\.cruises$ whois.donuts.co
\.cuisinella$ whois.nic.cuisinella
\.cx$ whois.nic.cx
\.cymru$ whois.nic.cymru
\.cz$ whois.nic.cz
\.dance$ whois.unitedtld.com
\.dating$ whois.donuts.co
\.de$ whois.denic.de
\.deals$ whois.donuts.co
\.degree$ whois.rightside.co
\.democrat$ whois.unitedtld.com
\.dental$ whois.donuts.co
\.dentist$ whois.rightside.co
\.desi$ whois.ksregistry.net
\.diamonds$ whois.donuts.co
\.diet$ whois.uniregistry.net
\.digital$ whois.donuts.co
\.direct$ whois.donuts.co
\.directory$ whois.donuts.co
\.discount$ whois.donuts.co
\.dk$ whois.dk-hostmaster.dk
\.dm$ whois.nic.dm
\.domains$ whois.donuts.co
\.durban$ durban-whois.registry.net.za
\.dz$ whois.nic.dz
\.ec$ whois.nic.ec
\.edu$ whois.educause.edu
\.education$ whois.donuts.co
\.ee$ whois.tld.ee
\.email$ whois.donuts.co
\.engineer$ whois.rightside.co
\.engineering$ whois.donuts.co
\.enterprises$ whois.donuts.co
\.equipment$ whois.donuts.co
\.es$ whois.nic.es
\.estate$ whois.donuts.co
\.eu$ whois.eu
\.eus$ whois.eus.coreregistry.net
\.events$ whois.donuts.co
\.exchange$ whois.donuts.co
\.expert$ whois.donuts.co
\.exposed$ whois.donuts.co
\.fail$ whois.donuts.co
\.farm$ whois.donuts.co
\.feedback$ whois.centralnic.com
\.fi$ whois.fi
\.finance$ whois.donuts.co
\.financial$ whois.donuts.co
\.fish$ whois.donuts.co
\.fishing$ whois-dub.mm-registry.com
\.fitness$ whois.donuts.co
\.flights$ whois.donuts.co
\.florist$ whois.donuts.co
\.fo$ whois.nic.fo
\.foo$ domain-registry-whois.l.google.com
\.foundation$ whois.donuts.co
\.fr$ whois.nic.fr
\.frogans$ whois-frogans.nic.fr
\.fund$ whois.donuts.co
\.furniture$ whois.donuts.co
\.futbol$ whois.unitedtld.com
\.gal$ whois.gal.coreregistry.net
\.gallery$ whois.donuts.co
\.gbiz$ domain-registry-whois.l.google.com
\.gd$ whois.nic.gd
\.gent$ whois.nic.gent
\.gg$ whois.gg
\.gi$ whois2.afilias-grs.net
\.gift$ whois.uniregistry.net
\.gifts$ whois.donuts.co
\.gives$ whois.rightside.co
\.gl$ whois.nic.gl
\.glass$ whois.donuts.co
\.global$ whois.afilias-srs.net
\.globo$ whois.gtlds.nic.br
\.gmail$ domain-registry-whois.l.google.com
\.gop$ whois-cl01.mm-registry.com
\.gov$ whois.dotgov.gov
\.graphics$ whois.donuts.co
\.gratis$ whois.donuts.co
\.green$ whois.afilias.net
\.gripe$ whois.donuts.co
\.gs$ whois.nic.gs
\.guide$ whois.donuts.co
\.guitars$ whois.uniregistry.net
\.guru$ whois.donuts.co
\.gy$ whois.registry.gy
\.hamburg$ whois.nic.hamburg
\.haus$ whois.unitedtld.com
\.healthcare$ whois.donuts.co
\.help$ whois.uniregistry.net
\.hiphop$ whois.uniregistry.net
\.hiv$ whois.afilias-srs.net
\.hk$ whois.hkirc.hk
\.hn$ whois.nic.hn
\.holdings$ whois.donuts.co
\.holiday$ whois.donuts.co
\.homes$ whois.afilias-srs.net
\.horse$ whois-dub.mm-registry.com
\.host$ whois.nic.host
\.hosting$ whois.uniregistry.net
\.house$ whois.donuts.co
\.how$ domain-registry-whois.l.google.com
\.hr$ whois.dns.hr
\.ht$ whois.nic.ht
\.hu$ whois.nic.hu
\.id$ whois.pandi.or.id
\.ie$ whois.domainregistry.ie
\.il$ whois.isoc.org.il
\.im$ whois.nic.im
\.immo$ whois.donuts.co
\.immobilien$ whois.unitedtld.com
\.in$ whois.inregistry.net
\.industries$ whois.donuts.co
\.info$ whois.afilias.net
\.ink$ whois.centralnic.com
\.institute$ whois.donuts.co
\.insure$ whois.donuts.co
\.int$ whois.iana.org
\.international$ whois.donuts.co
\.investments$ whois.donuts.co
\.io$ whois.nic.io
\.iq$ whois.cmc.iq
\.ir$ whois.nic.ir
\.is$ whois.isnic.is
\.it$ whois.nic.it
\.je$ whois.je
\.jobs$ jobswhois.verisign-grs.com
\.joburg$ joburg-whois.registry.net.za
\.jp$ whois.jprs.jp
\.juegos$ whois.uniregistry.net
\.kaufen$ whois.unitedtld.com
\.ke$ whois.kenic.or.ke
\.kg$ whois.domain.kg
\.ki$ whois.nic.ki
\.kim$ whois.afilias.net
\.kitchen$ whois.donuts.co
\.kiwi$ whois.nic.kiwi
\.koeln$ whois-fe1.pdt.koeln.tango.knipp.de
\.kr$ whois.kr
\.krd$ whois.aridnrs.net.au
\.kred$ whois.nic.kred
\.kz$ whois.nic.kz
\.la$ whois.nic.la
\.lacaixa$ whois.nic.lacaixa
\.land$ whois.donuts.co
\.lawyer$ whois.rightside.co
\.lease$ whois.donuts.co
\.lgbt$ whois.afilias.net
\.li$ whois.nic.li
\.life$ whois.donuts.co
\.lighting$ whois.donuts.co
\.limited$ whois.donuts.co
\.limo$ whois.donuts.co
\.link$ whois.uniregistry.net
\.loans$ whois.donuts.co
\.london$ whois-lon.mm-registry.com
\.lotto$ whois.afilias.net
\.lt$ whois.domreg.lt
\.ltda$ whois.afilias-srs.net
\.lu$ whois.dns.lu
\.luxe$ whois-dub.mm-registry.com
\.luxury$ whois.nic.luxury
\.lv$ whois.nic.lv
\.ly$ whois.nic.ly
\.ma$ whois.iam.net.ma
\.maison$ whois.donuts.co
\.management$ whois.donuts.co
\.mango$ whois.mango.coreregistry.net
\.market$ whois.rightside.co
\.marketing$ whois.donuts.co
\.md$ whois.nic.md
\.me$ whois.nic.me
\.media$ whois.donuts.co
\.meet$ whois.afilias.net
\.melbourne$ whois.aridnrs.net.au
\.menu$ whois.nic.menu
\.mg$ whois.nic.mg
\.miami$ whois-dub.mm-registry.com
\.mini$ whois.ksregistry.net
\.mk$ whois.marnet.mk
\.ml$ whois.dot.ml
\.mn$ whois.nic.mn
\.mo$ whois.monic.mo
\.mobi$ whois.dotmobiregistry.net
\.moda$ whois.unitedtld.com
\.monash$ whois.nic.monash
\.mortgage$ whois.rightside.co
\.moscow$ whois.nic.moscow
\.motorcycles$ whois.afilias-srs.net
\.mp$ whois.nic.mp
\.ms$ whois.nic.ms
\.mu$ whois.nic.mu
\.museum$ whois.museum
\.mx$ whois.mx
\.my$ whois.mynic.my
\.na$ whois.na-nic.com.na
\.nagoya$ whois.gmoregistry.net
\.name$ whois.nic.name
\.navy$ whois.rightside.co
\.nc$ whois.nc
\.net$ whois.verisign-grs.com
\.network$ whois.donuts.co
\.nf$ whois.nic.nf
\.ng$ whois.nic.net.ng
\.ngo$ whois.publicinterestregistry.net
\.ninja$ whois.unitedtld.com
\.nl$ whois.domain-registry.nl
\.no$ whois.norid.no
\.nra$ whois.afilias-srs.net
\.nrw$ whois.nic.nrw
\.nu$ whois.iis.nu
\.nyc$ whois.nic.nyc
\.nz$ whois.srs.net.nz
\.okinawa$ whois.gmoregistry.ne
\.om$ whois.registry.om
\.onl$ whois.afilias-srs.net
\.ooo$ whois.nic.ooo
\.org$ whois.pir.org
\.organic$ whois.afilias.net
\.ovh$ whois-ovh.nic.fr
\.paris$ whois-paris.nic.fr
\.partners$ whois.donuts.co
\.parts$ whois.donuts.co
\.pe$ kero.yachay.pe
\.pf$ whois.registry.pf
\.photo$ whois.uniregistry.net
\.photography$ whois.donuts.co
\.photos$ whois.donuts.co
\.physio$ whois.nic.physio
\.pics$ whois.uniregistry.net
\.pictures$ whois.donuts.co
\.pink$ whois.afilias.net
\.pizza$ whois.donuts.co
\.pl$ whois.dns.pl
\.place$ whois.donuts.co
\.plumbing$ whois.donuts.co
\.pm$ whois.nic.pm
\.post$ whois.dotpostregistry.net
\.pr$ whois.nic.pr
\.press$ whois.nic.press
\.pro$ whois.dotproregistry.net
\.productions$ whois.donuts.co
\.properties$ whois.donuts.co
\.property$ whois.uniregistry.net
\.pt$ whois.dns.pt
\.pub$ whois.unitedtld.com
\.pw$ whois.nic.pw
\.qa$ whois.registry.qa
\.qpon$ whois.nic.qpon
\.quebec$ whois.quebec.rs.corenic.net
\.re$ whois.nic.re
\.recipes$ whois.donuts.co
\.red$ whois.afilias.net
\.rehab$ whois.rightside.co
\.reise$ whois.nic.reise
\.reisen$ whois.donuts.co
\.rentals$ whois.donuts.co
\.repair$ whois.donuts.co
\.report$ whois.donuts.co
\.republican$ whois.rightside.co
\.rest$ whois.centralnic.com
\.restaurant$ whois.donuts.co
\.reviews$ whois.unitedtld.com
\.rich$ whois.afilias-srs.net
\.rio$ whois.gtlds.nic.br
\.ro$ whois.rotld.ro
\.rocks$ whois.unitedtld.com
\.rodeo$ whois-dub.mm-registry.com
\.rs$ whois.rnids.rs
\.ru$ whois.tcinet.ru
\.ruhr$ whois.nic.ruhr
\.sa$ whois.nic.net.sa
\.saarland$ whois.ksregistry.net
\.sarl$ whois.donuts.co
\.sb$ whois.nic.net.sb
\.sc$ whois2.afilias-grs.net
\.sca$ whois.nic.sca
\.scb$ whois.nic.scb
\.schmidt$ whois.nic.schmidt
\.schule$ whois.donuts.co
\.scot$ whois.scot.coreregistry.net
\.se$ whois.iis.se
\.services$ whois.donuts.co
\.sexy$ whois.uniregistry.net
\.sg$ whois.sgnic.sg
\.sh$ whois.nic.sh
\.shiksha$ whois.afilias.net
\.shoes$ whois.donuts.co
\.si$ whois.arnes.si
\.singles$ whois.donuts.co
\.sk$ whois.sk-nic.sk
\.sm$ whois.nic.sm
\.sn$ whois.nic.sn
\.so$ whois.nic.so
\.social$ whois.unitedtld.com
\.software$ whois.rightside.co
\.sohu$ whois.gtld.knet.cn
\.solar$ whois.donuts.co
\.solutions$ whois.donuts.co
\.soy$ domain-registry-whois.l.google.com
\.space$ whois.nic.space
\.spiegel$ whois.ksregistry.net
\.st$ whois.nic.st
\.su$ whois.tcinet.ru
\.supplies$ whois.donuts.co
\.supply$ whois.donuts.co
\.support$ whois.donuts.co
\.surf$ whois-dub.mm-registry.com
\.surgery$ whois.donuts.co
\.sx$ whois.sx
\.sy$ whois.tld.sy
\.systems$ whois.donuts.co
\.tatar$ whois.nic.tatar
\.tattoo$ whois.uniregistry.net
\.tax$ whois.donuts.co
\.tc$ whois.meridiantld.net
\.technology$ whois.donuts.co
\.tel$ whois.nic.tel
\.tf$ whois.nic.tf
\.th$ whois.thnic.co.th
\.tienda$ whois.donuts.co
\.tips$ whois.donuts.co
\.tirol$ whois.nic.tirol
\.tk$ whois.dot.tk
\.tl$ whois.nic.tl
\.tm$ whois.nic.tm
\.tn$ whois.ati.tn
\.to$ whois.tonic.to
\.today$ whois.donuts.co
\.tokyo$ whois.nic.tokyo
\.tools$ whois.donuts.co
\.top$ whois.nic.top
\.town$ whois.donuts.co
\.toys$ whois.donuts.co
\.tr$ whois.nic.tr
\.trade$ whois.nic.trade
\.training$ whois.donuts.co
\.travel$ whois.nic.travel
\.tv$ tvwhois.verisign-grs.com
\.tw$ whois.twnic.net.tw
\.tz$ whois.tznic.or.tz
\.ua$ whois.ua
\.ug$ whois.co.ug
\.uk$ whois.nic.uk
\.university$ whois.donuts.co
\.uol$ whois.gtlds.nic.br
\.us$ whois.nic.us
\.uy$ whois.nic.org.uy
\.uz$ whois.cctld.uz
\.vacations$ whois.donuts.co
\.vc$ whois2.afilias-grs.net
\.ve$ whois.nic.ve
\.vegas$ whois.afilias-srs.net
\.ventures$ whois.donuts.co
\.versicherung$ whois.nic.versicherung
\.vet$ whois.rightside.co
\.vg$ ccwhois.ksregistry.net
\.viajes$ whois.donuts.co
\.villas$ whois.donuts.co
\.vision$ whois.donuts.co
\.vlaanderen$ whois.nic.vlaanderen
\.vodka$ whois-dub.mm-registry.com
\.vote$ whois.afilias.net
\.voting$ whois.voting.tld-box.at
\.voto$ whois.afilias.net
\.voyage$ whois.donuts.co
\.vu$ vunic.vu
\.wales$ whois.nic.wales
\.wang$ whois.gtld.knet.cn
\.watch$ whois.donuts.co
\.webcam$ whois.nic.webcam
\.website$ whois.nic.website
\.wed$ whois.nic.wed
\.wf$ whois.nic.wf
\.wien$ whois.nic.wien
\.wiki$ whois.nic.wiki
\.works$ whois.donuts.co
\.ws$ whois.website.ws
\.wtc$ whois.nic.wtc
\.wtf$ whois.donuts.co
\.xn--1qqw23a$ whois.ngtld.cn
\.xn--3bst00m$ whois.gtld.knet.cn
\.xn--3ds443g$ whois.afilias-srs.net
\.xn--3e0b707e$ whois.kr
\.xn--4gbrim$ whois.afilias-srs.net
\.xn--55qw42g$ whois.conac.cn
\.xn--55qx5d$ whois.ngtld.cn
\.xn--6frz82g$ whois.afilias.net
\.xn--6qq986b3xl$ whois.gtld.knet.cn
\.xn--80adxhks$ whois.nic.xn--80adxhks
\.xn--80ao21a$ whois.nic.kz
\.xn--80asehdb$ whois.online.rs.corenic.net
\.xn--80aswg$ whois.site.rs.corenic.net
\.xn--c1avg$ whois.publicinterestregistry.net
\.xn--cg4bki$ whois.kr
\.xn--clchc0ea0b2g2a9gcd$ whois.sgnic.sg
\.xn--czru2d$ whois.gtld.knet.cn
\.xn--d1acj3b$ whois.nic.xn--d1acj3b
\.xn--fiq228c5hs$ whois.afilias-srs.net
\.xn--fiq64b$ whois.gtld.knet.cn
\.xn--fiqs8s$ cwhois.cnnic.cn
\.xn--fiqz9s$ cwhois.cnnic.cn
\.xn--i1b6b1a6a2e$ whois.publicinterestregistry.net
\.xn--io0a7i$ whois.ngtld.cn
\.xn--j1amh$ whois.dotukr.com
\.xn--j6w193g$ whois.hkirc.hk
\.xn--kprw13d$ whois.twnic.net.tw
\.xn--kpry57d$ whois.twnic.net.tw
\.xn--lgbbat1ad8j$ whois.nic.dz
\.xn--mgb9awbf$ whois.registry.om
\.xn--mgba3a4f16a$ whois.nic.ir
\.xn--mgbaam7a8h$ whois.aeda.net.ae
\.xn--mgbab2bd$ whois.bazaar.coreregistry.net
\.xn--mgberp4a5d4ar$ whois.nic.net.sa
\.xn--mgbx4cd0ab$ whois.mynic.my
\.xn--ngbc5azd$ whois.nic.xn--ngbc5azd
\.xn--nqv7f$ whois.publicinterestregistry.net
\.xn--nqv7fs00ema$ whois.publicinterestregistry.net
\.xn--o3cw4h$ whois.thnic.co.th
\.xn--ogbpf8fl$ whois.tld.sy
\.xn--p1ai$ whois.tcinet.ru
\.xn--q9jyb4c$ domain-registry-whois.l.google.com
\.xn--rhqv96g$ whois.nic.xn--rhqv96g
\.xn--unup4y$ whois.donuts.co
\.xn--vhquv$ whois.donuts.co
\.xn--wgbl6a$ whois.registry.qa
\.xn--xhq521b$ whois.ngtld.cn
\.xn--yfro4i67o$ whois.sgnic.sg
\.xn--ygbi2ammx$ whois.pnina.ps
\.xn--zfr164b$ whois.conac.cn
\.xxx$ whois.nic.xxx
\.xyz$ whois.nic.xyz
\.yachts$ whois.afilias-srs.net
\.yt$ whois.nic.yt
\.zm$ whois.nic.zm
\.zone$ whois.donuts.co
"""

for item in tld_list.split("\n"):
	if item.strip() == "":
		continue
	tld, server = item.strip().split(" ", 1)
	tld = tld.lstrip("\\").rstrip("$")
	target_domain = "domain%s" % tld

	try:
		root_server = pythonwhois.net.get_root_server(target_domain)

		if root_server.strip() != server.strip():
			print("[ERR] WHOIS server doesn't match for {}! List indicates %s, IANA said %s." % (tld, server, root_server))
		else:
			print("[OK ] IANA and list agree that the WHOIS server for %s is %s." % (tld, root_server))
	except Exception as e:
		print("[ERR] Unknown WHOIS server for %s! List indicates %s." % (tld, server))
