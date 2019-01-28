
from bs4 import BeautifulSoup
import requests
import unidecode

class BookHunter(object):
    def __init__(self):
        #index of main loop
        self.index = 0
        #all of the found book titles
        self.all = []
        #all of the element found on the web page
        self.found = []
        #all of the keywords
        self.keywords = ['Ztraceny kral', 'Sutnar', "Teige", "Drtikol", "Devětsil", "Friml", "Fulla", "Halabala", "Sudek",
                    "Hesoun", "Index Olomouc", "Jazzpetit", "Valoch", "Kalivoda", "Dyrynk", 'Rudolf Prokop',
                    '1947 skupiny ra', 'Umeni mladych vytvarniku Ceskoslovenska', '33 dopisy SSSR',
                    'abc dyalektyckeho materializmu', 'Acta incognitorum', 'adamus', 'Adolf Chaloupka', 'ADRIAPORT',
                    'AFK Bohemians', 'Aforismy Smazik Rudolf', 'Aka', 'akcni tvorba', 'akrobat', 'aktuality budovani',
                    'Alexandr blok', 'ALMANACH LOUNSKEHO STUDENTSTVA', 'Almanach Narodniho divadla',
                    'almanach pro poesii', 'Almanach secese', 'Alois Wachsman', 'amazonka 1928', 'amazonsky proud 1923',
                    'ambientni hudba industrial', 'American 1948 fast', 'Americane Leningrade', 'Amor psyche Souckova',
                    'Anebo 1918', 'anonym', 'Antar', 'Antonin Heythum', 'apollinaire fantasie', 'archipenko',
                    'Architektonicky Obzor', 'Architektonicky Obzor 1919', 'architektura prava leva', 'Archy 1929',
                    'Ardev', 'arjan', 'ARTIA 1960', 'avantgardnim stylu', 'aventina', 'aventinum', 'avion vrba',
                    'babicka 1923', ' Balada namorniku Lander', 'Baladran', 'Balzac divka', 'Barak pet be',
                    'bart nadrazi', 'Bartos souboj', 'Bartuska Josef', 'Bata', 'bata bankrot', 'Batika 1928', 'Beckett',
                    'Beckett 1963', 'Beckett kolar', 'Bednar', 'Bela kolarova', 'Belohlavek Kaleidoskop', 'Benda',
                    'Benisko', 'Benka', 'berta zenaty', 'Bez mista Polacek', 'Bezejmenni kucera', 'Bezici pas',
                    'Bibliofil 1924', 'Bila rakev', 'Bily admiral', 'blesk 1928', 'Blizenci 1927', 'Bobrove',
                    'Bochorakova Dittrichova', 'Bogarov', 'Bohatec Teige', 'Bohman', 'Boj job', 'boj milost',
                    'Bojacni rvac', 'Boleslav Vomacka', 'Bolsevicky raj', 'Bolsevikem 1921', 'Bolsevismu',
                    'bonaventury', 'Borecky', 'botas', 'BOUS', 'Nasi umelci', 'Bozi muka 1917', 'bozstva kulty',
                    'Bradac 1908', 'Bradac Ludvik', 'Bragozda', 'braillovo pismo', 'Brazda', 'brichomluvec', 'Brikcius',
                    'Brixenske basne', 'Brnenska Leva fronta', 'Brodheim', 'Buchler Pavel', 'Bude vojna bude',
                    'bydleni', 'Byt umeni', 'bytova kultura', 'Caje o pate', 'capek', 'capek nove doby',
                    'Casopis ceskoslovenky inzenyru architkturu', 'Casopis ceskoslovenky inzenyru architkturu 1924',
                    'Casopis ceskoslovenky inzenyru architkturu 1925', 'cechische', 'Cechoslovacka muzicka kultura',
                    'CEKANI NA GODOTA', 'Cellularni mysleni', 'celokozena', 'cerminova', 'Cerne ruze', 'cerven',
                    'Cesky Interieur', 'Cesta hosparske obrode', 'Cesta hospodarske obrode', 'Cesta jednoduchnosti',
                    'CESTA K JEDNODUCHOSTI', 'cestou necestou chalupecky', 'cetnicke humoresky', 'Chaplin',
                    'chaplin 1924', 'chatrny', 'chechische', 'chlapci ktery slunce hledat sel', 'chlebecek',
                    'cholinskeho', 'Chram prace', 'CHVALA REKLAMY', 'Cigler', 'civilisovana', 'Clovek dela saty',
                    'Clovek jest dobry', 'Clovek zahrada sira', 'co dalo lidstvu', 'Co se slovy vsechno povi', 'Csader',
                    'Czechoslovak Foreign Trade', 'darem republice', 'Das Moderne Lichtbild', 'Dav umenie',
                    'dejin spiritismu minulosti', 'Dejiny ruske revoluce 1936', 'Delluc Louis', 'Delnicka osveta',
                    'delnicka rocenka', 'delnicke olympiady', 'demokracie jedinec Melantrich', 'Der mensch 1921',
                    'Design plasticke hmoty', 'desinfekcni ustav', 'deste novak', 'DETSKA KNIZKA', 'Detske snahy',
                    'Devetsil', 'dialog 1969', 'Die Vier', 'Dikobraz 1957', 'Disk 1923', 'Disk 1924', 'Disk 1925',
                    'Diskutujeme moralce dneska', 'Divadelni promenady', 'divadlo nerudovce', 'Divadlo vsem',
                    'Divka na brehu jezera', 'Divka se zlatyma ocima 1907', 'divka sen nohejl', 'DIVOKE SRDCE vachek',
                    'Dnesni Moskva', 'Dobrodruh 1934', 'DOBRODRUH Tater', 'dojmy sssr', 'Dolmen',
                    'Donat sajner Cerveny kolotoc', 'Dorost', 'dos passos', 'Dr Stekel Onanie', 'drevoryt',
                    'Drobne umeni 1924', 'Drtikol', 'Duchampovske meditace', 'Duha 1930', 'Duha jirak',
                    'Dum na pokraji piscin', 'Dusan Skala', 'DUSE OSTRAVY', 'dvanact maju', 'dve balady hora',
                    'dve rozpravy 1923', 'Dvojbarve vidmo', 'Dymes 1929', 'dymes ze sveta do sveta', 'dzunglich evropy',
                    'Edice kvart', 'edice ra', 'edyce slunce', 'Egon Kisch', 'ehm', 'ehrenburg', 'eight umelcu',
                    'Ekran', 'Ekstase', 'Elegie 1932', 'ELIOT PUSTA ZEME', 'EM 89', 'Emil Pitter', 'erika frice',
                    'Es kommt der neue Fotograf', 'Eva kmentova', 'Evidentni basne', 'Evzen Linhart', 'Evzen Markalous',
                    'Exoticka krajina', 'Extase', 'Fabry hodiny', 'fanfarlo 1927', 'Fantasijni aspekty', 'Fantomas',
                    'Farma zvirat', 'Farrere', 'Fenomen Bata 2009', 'Ferenc Futurista', 'Filmovy kalendar 1947',
                    'Fleischmann Karel Navrat', 'Fleischner', 'Fluxus', 'Forum 1932', 'Forum 1933', 'Forum 1935',
                    'Forum 1936', 'Forum 1937', 'Forum 1939', 'fotograficky obzor',
                    'Fotografie jako zreni sveta zivota', 'fotomontaz', 'fotostrojka', 'fragment bydleni',
                    'Franz jung proletari', 'Friml', 'Fritta', 'Fulla', 'funkcich prace osobitosti', 'Funke',
                    'Fysiognomie 1921', 'galerie vaclava spaly', 'Garell', 'Generace 1945', 'Generace 1946',
                    'Gentleman', 'ghetto 1902', 'Golem 1917', 'graficke fantasie', 'graficky obzor',
                    'GROGEROVA BOJ JOB', 'Grossmann Balan', 'Guth', 'GYN ADAM', 'Hak Sudek', 'halabala', 'halas',
                    'Hanfova edice', 'Hanus Drastova', 'Havrani stribro', 'heartfield', 'Heisler', 'helios',
                    'Henri Poire', 'herrenvolk', 'hesoun', 'Heythum', 'Hledej co najdes ve meste', 'Hmly na usvite',
                    'hodinky balzac', 'Hodinky jeptisek Poissy', 'hoffmeister', 'Hofman', 'Honty', 'honzik', 'Honzl',
                    'hora proroku', 'Horizont', 'Horizont 1927', 'Horizont 1928', 'Hory a Lide', 'Host 1924', 'hovne',
                    'hrad smrti', 'Hrbas Jiri Laterna magika', 'Hrska', 'Huch posledni leto', 'hudba zvuk',
                    'hudebni letak', 'Hurbanovia vo vazeniach', 'Husi 1916', 'hutnicka polka', 'hygieny 1933',
                    'idea skypala', 'Idioteon', 'iljin hory', 'In orbe artium', 'index 1937', 'index 1938',
                    'Index 1984', 'Index Olomouc', 'Indiani Jindy Dnes', 'Informacni bulletin', 'Insiders',
                    'interni zpravodaj citarny', 'ISAV', 'Isavske pisne', 'isolace proti vlhku', 'Istar 1924',
                    'Istrati', 'Ivo Hausmann', 'Jack London 1928', 'Jahoda Josef Pazderna', 'Jak bydleti',
                    'Jak si zaridim byt', 'Jak zachazeti s detmi', 'jan bartos', 'Jan Bor', 'Jan Gillar', 'Jan Lukas',
                    'Jan Mancuska', 'jan svoboda 1968', 'Jan Svoboda 1980', 'jarmark 1947', 'Jarni vystava 1922',
                    'Jaromir Krejcar', 'Jaron', 'Jaroslav Dohal', 'Jaroslav Fragner', 'Jaroslav Hosek',
                    'Jaroslav Rossler', 'jaroslavu kralovi', 'jarpi', 'Jasno 1919', 'Jasszusch', 'jazz bulletin',
                    'Jazzpetit', 'Jeden den prazdnin', 'jednou nohou', 'Jelinek', 'Jilek', 'Jimmie Dolar',
                    'Jimmie Dollar', 'Jiri Frejka', 'Jiri Kolar', 'Jiri Linhart', 'Jiri Valoch', 'job boj',
                    'Josef Chochol', 'Josef Honys', 'Josef Koudelka', 'Josef Pleva 1930', 'Josef Svoboda 1971',
                    'Jozef Rybak', 'Kafka', 'Kalivoda 1967', 'KAMARADUM BIDY', 'Kameny zlomu', 'kapka vody',
                    'KARAVANA 1929', 'Karel Balling', 'Karel Dyrynk', 'karel fleischmann', 'Karel Malich',
                    'karel miler', 'Karel Valter', 'Kaspar Mir nedel', 'Katerina Seda', 'Kdyz se vali revoluce',
                    'Ketzek', 'KLECE DNI', 'kmen', 'Kmen 1920', 'KNEIPPOVY BYLINY LECIVE', 'knihovny technicke tribuny',
                    'knock out', 'kobliha', 'Kocmoud', 'kohout stavitelstvi 1928', 'kokaina 1928', 'koktejlu', 'kolaz',
                    'Kolotoc noci', 'Komu zvoni hrana', 'komunismus 1921', 'Komunisticke nakladatelstvi',
                    'Konec civilisace', 'Konupek fantasie', 'Korale 1932', 'Kornout', 'Koruna 1928', 'Koruna 1929',
                    'koruna obrazkovy magazin', 'kosmicke 1882', 'Kosoctverce na ohradach', 'Kotik',
                    'Koudelkuv Kuracky Kodex', 'Kouril', 'kozena vazba', 'Kraj dychal vecerem', 'krakatit 1924',
                    'Kral Ubu 1966', 'Kral uhel 1920', 'Krameriova expedice', 'krasna vazba',
                    'KRASNE PISMO VE VYVOJI LATINKY', 'Krasoumna jednota', 'Krasoumne jednoty',
                    'KRATOCHVILNY PRIBEH LVA KEFASE VYTECNIKA', 'kresleni', 'Kriz na rozcesti',
                    'KRIZACKA VYPRAVA DITEK', 'Krize literatury', 'krkavci 1924', 'Kroha', 'kruh osudu sekera',
                    'krvajici rany', 'kubismus', 'kubisticka', 'kubisticke', 'kubisticky', 'kudej humoresky 1916',
                    'Kultura regionalismus', 'Kulturni prace sovetskeho Ruska', 'Kuriosni revue', 'KUZE umelecka',
                    'Kvasnak', 'Kysela', 'La verrerie en tchecoslovaquie', 'Laboretismus', 'Labyrint 1962',
                    'Ladislav Bambasek', 'Ladislav Klima', 'Ladislav Nebesky', 'Ladislav Sotek', 'Lamarova 1967',
                    'Lasky halekani', 'Laviny kundera', 'Lazensky host', 'lbri prohibiti', 'legie', 'Legionar',
                    'legionari', 'Legionaru', 'Lelio', 'Leskle nacini', 'Letadlem ze Zlina do Kapskeho mesta',
                    'Letem svetem', 'leva fronta', 'Levana', 'Lewis carrol', 'libri prohibiti', 'Lidove noviny 1989',
                    'Limitovana basen', 'linorez teige', 'linoryt', 'Listy 1946 Chalupecky', 'Listy Casopis',
                    'literaturo', 'liwingstona', 'lodi jez 1928', 'Lomikel', 'Ludvik Kysela', 'Ludvik Vaculik',
                    'Luk dav', 'lyrika 1927', 'Lyrika Novak', 'Magazin 1930', 'Mahen 1907', 'Maj 57', 'Majakovskij',
                    'Majakovsky', 'Mala vlastiveda', 'malba malirsky rukopis', 'maldoror 1929', 'Malich Skicaky',
                    'malicke 1920', 'Malik Verlag', 'Mam rad Frycek', 'Marek Vlastimil', 'Maria magdaly 1908',
                    'marian palla', 'Markonoviny', 'Mary jedenactyricitky', 'MARY JEDNACTYRICITKY',
                    'Masarykuv studentsky domov', 'Masek', 'maslickovy', 'masurkovske', 'mat evropo', 'Matica', 'Mazac',
                    'mehedaha', 'Mekke dno', 'mene tekel fares', 'Merkur 1967 Vykladni skrin', 'Mess Mend',
                    'mesto slzach', 'mesto upravovaci plan', 'metropolis', 'Mezi vrstvami',
                    'Mezinarodni buletin surrealismu', 'mezinarodni spoje', 'Mezinarodni vystava fotografie',
                    'MEZINARODNI VYSTAVA KARIKATUR HUMORU', 'Mezinarodni vystava socialni fotografie',
                    'Mezopotamie Weiner', 'Milada Souckova', 'Milan Grygar', 'Milca Mayerova', 'Milen',
                    'Mileniny recepty', 'millenium 1927', 'Milos Fabian', 'Milovan Djilas', 'Miroslav Haller',
                    'Miroslav Korycan', 'Mlade Rokycansko', 'mladeho flauberta', 'Mladi vpred', 'Mladsi surrealiste',
                    'Mlady fotoamater', 'Mluvici pasmo', 'Moderni cesky plakat', 'Moderni romany', 'Modry plamen',
                    'moll dur veraikon', 'Mopr', 'Moravskoslezskeho sdruzeni vytvarnych umelcu', 'moskva hranice',
                    'most 81', 'Mrkvicka', 'MSA', 'MSA II', 'msvu', 'Mucha', 'Muj svetovy nazor',
                    'Muz na strazi MERLINOVA', 'Muzika', 'Mym dechem', 'Myslbek 1929', 'Mysticke jahody',
                    'mystikove visionari', 'Na brezich Indickeho oceanu', 'na okraj dnu', 'na promenade',
                    'NA SHLEDANOU 1935', 'Na suchu ve vzduchu', 'Na vzdory jim', 'nachazeni Laches',
                    'NAD STARYMI SCHODY HRADCANSKYMI', 'Nadtelevox', 'Nakladatel bez koncese', 'Narikajici motyl',
                    'Nasa skola', 'nasim hospodynkam 1934', 'nasledky horka', 'navrh nove sovetske ustavy', 'Nebojsa',
                    'necessismus', 'Nejdemokratictejsi', 'nejdemokratictejsi ustava sveta', 'nejmladsi poesii',
                    'Nekolik prokletych 1928', 'Nemsovsky', 'nesmrtelnosti dila basnickeho', 'Netvorice 81',
                    'Nezavisli', 'Nezval', 'nobuyoshi', 'Nohejl', 'NONSENS VYBOR POEZIE', 'NOTUS',
                    'nova bratislava funke', 'Nova kuchyne 1930', 'Nova skupina', 'NOVA ZEME 1927',
                    'noviny novinari 1927', 'novy ikarus', 'OBLAK KALHOTACH', 'Obratnik Raka 1938', 'obraz zvuk',
                    'Obrazkovy filmovy program 538', 'obrnenec', 'obrtel', 'obtize vodnich cest', 'Obytna krajina',
                    'Obzory 1934', 'OCISTEC KONCI RAJEM POZEMSKYM', 'od hroudy chlebu', 'Ohnivy cervenec',
                    'ohyb zelezobeton', 'okno otevrene zak', 'olaf hanel', 'Oldrich Stary', 'olejomalba', 'Olisbos',
                    'oparany jelen', 'opata longina', 'Opatstvi Typhainske', 'Orfeus', 'orfeus 1920', 'Orfeus 1921',
                    'orfeus 1928', 'ostrava spala', 'Ostrov slzi', 'Osudna vejce', 'Osvobozena domacnost',
                    'osvobozena slova', 'Osvobozeni Ostravy', 'otcenas', 'Ovcacek', 'ozehnuti', 'OZUBENE OKNO',
                    'pacient lekar 1938', 'pajda', 'pako', 'Pamatce Prokopa Koudely', 'Pameti Josefiny Bakerove',
                    'Paprsky inzenyra Garina 1927', 'paralelni polis', 'PARIZ NOCI', 'Pariz noci 1927',
                    'Paroubek Safra', 'Pasmo', 'pasmo 1919', 'Pasmo 1924', 'Pasmo 1925', 'Patocka samizdat',
                    'pavi oko 1922', 'Pelc', 'penzijni ustav', 'Pernikove srdce', 'Pesanek', 'pestry tyden',
                    'Petr Kien', 'Petrescu', 'Petrolejari', 'Pianista baru', 'Pierre de Lasenic', 'pink tank',
                    'Pisen neme tvari', 'Pisne Ostravskeho Kamelota', 'pitigrilli', 'Plan 1929', 'Plan 1930',
                    'plasticke hmoty 1972', 'Plebiscit', 'Plebiscit 1920', 'Plosna stylisace dle prirody',
                    'plyn voda 1934', 'Plzensky student', 'Pochodova tiskarna dostal', 'pod drobnohledem',
                    'Pod pustym kopcem', 'Podesva', 'Podivini 1907', 'PODIVUHODNA PUTOVANI KREJCIHO FOKINA',
                    'Podzemi velkeho mesta', 'Pohlavni ozvy', 'Polytonfox', 'Popelnice', 'PORCELANOVY HRNICEK',
                    'Porta apostolarum', 'Porta Apostolorum', 'Posklebek delnika', 'POSLANI MARIE JOSEFY',
                    'poutnickou holi 1936', 'Povesti zo Slovenska', 'Povidky ghetta', 'Povoden Hlouposti',
                    'pozdravac illusi', 'Prace Jaromira Krejcara', 'PRACE JE ZIVA', 'Pracovni kniha zemepisu',
                    'Pratelstvi osud', 'Prava lidu Sobota', 'Prazdninova cesta', 'Prazdniny na venkove',
                    'prazdniny na venkove Maresova', 'Prazska dramaturgie', 'predlohy kresleni', 'Predzvesti',
                    'Preissig', 'prepekne cteni', 'previsle konstrukce schmidt', 'Pricina  Frank Leonhard', 'princeps',
                    'Princezna Hyacinta', 'Princip slasti', 'Priroda jinak', 'prispevek rozliseni',
                    'Proc jsi Cechoslovak', 'prochazka 1897', 'profil 1930', 'Program vlady 1945', 'Proletar',
                    'proletkult', 'promena 1919', 'Promena 1929', 'Promeny humoru', 'Prospekt', 'Proto 1989', 'Prulom',
                    'prumyslova skola graficka', 'PRUMYSLOVE ODBORNE SKOLSTVI', 'prumyslove umeni', 'Prusvit',
                    'Pruvodce pokrokove zeny zivotem', 'Prvni estetik filmu Vaclav Tille', 'Prvni pismena', 'prvosenky',
                    'psisery 1921', 'Pstros se zavrenyma ocima',
                    'Psychologie zivota v terezinskem koncentracnim tabore', 'pulnoc medek', 'punk', 'punkrock',
                    'putovani elfa', 'pysvejc', 'RADIO AMATER', 'Radiojournal', 'radiospirala', 'Radost smutek',
                    'Rajnis', 'rako', 'Rakomos', 'Rambousek', 'Rebcovo', 'Reduktivismus', 'Reflektor 1927',
                    'Reflektor 1928', 'regionalismus', 'Rejman', 'Renega', 'Republika', 'Republika 1919',
                    'retez stesti', 'revolucni napevy', 'Revue Cervene sedmy', 'Richard Lander', 'Rijnova revoluce',
                    'ritualu toledskych haeretiku', 'Robert Whittmann', 'rocenka', 'Rocenka ceske odborne skoly',
                    'rocenka kruhu solistu 1933', 'rocenka mestskych vodaren', 'rock kridle',
                    'Romance pocestneho clowna', 'rondokubismus', 'Rossmann', 'Rozevreny vejir uvah', 'rozhlas',
                    'Rozhlasove umeni', 'ROZJIZVENE SRDCE', 'rozmary lasky', 'roztocene jeviste', 'Ruce 1946',
                    'Ruch 1918', 'Ruch 1919', 'Ruch 1920', 'Rudolf fabry', 'Rudolf Weiser', 'Rudy obchod', 'Ruiny',
                    'Ruske byliny', 'Ruzove pravo', 'Ruzove viry', 'Rykr', 'Sachovnica', 'Sado Maso',
                    'Saga Gunnlaugovi', 'SALUT AU MONDE', 'samizdat', 'SARAUER ALOIS', 'sbohem armado', 'sbornik',
                    'sbornik 1935', 'Scheinpflugova zabity', 'Sdruzeni umelcu 1925', 'sebe vas', 'Sebe vas 1920',
                    'seda cihla', 'Seifert', 'Seifert destnik', 'Seifert dokumenty', 'sesity 1966', 'sesity 1967',
                    'sesity 1968', 'sesity 1969', 'sesity pro literaturu', 'SEST DNU NA LUNE',
                    'Severomoravska pasivita', 'SFK parsek', 'Sibenicky', 'Sibirska matka', 'Signal 1928',
                    'Signal 1929', 'Signal Casopis', 'Sima', 'Simotova', 'Situace 89', 'Skleneny havelok', 'Sklepnik',
                    'skoba', 'Skola mrtvol', 'skola umeleckych remesiel', 'Skola zpevu na zaklade modernich metod',
                    'skorpil', 'skryte divadlo', 'skupiny Linie', 'skypala 1921', 'slameny klobouk', 'Slavdel',
                    'slavik svateho', 'slepecky tisk', 'Slepeji Deml', 'Slovenska Grafia', 'Slunce Hlubin',
                    'slunci Hlobilova', 'slunecni vuz', 'SLUNECNI VUZ Hloucha', 'smeral 1927', 'Smrt na jevisti',
                    'snajdr', 'Snurove projekty', 'Socgorod', 'Socialisace praksi', 'SOCIALISTICKA FOTOGRAFIE',
                    'Socialisticke epistoly', 'Socialni fotografie', 'Socialni inzenyr',
                    'Societas Incognitorum Eruditorum', 'Sodoma', 'Sohaj', 'Sokol Zapas', 'Sommer-Batek', 'Sondy',
                    'Soucasne cinske malirstvi', 'sovetska kultura',
                    'Sovetske Rusi cesti spisovatele umelci komunisticti', 'Sovietske filmove plagaty', 'SOVOVA, LUCIE',
                    'Spala', 'spanelsko krvaci', 'Spartakiada 1928', 'Spektralni Tabor', 'SPORT NA LYZICH Vavra',
                    'Spsg', 'Spusa', 'srot periferie', 'Srsatec', 'Stan casopisy', 'Statni graficka skola',
                    'statni graficka skola praze', 'statut akademie', 'stavba', 'Stavba basen', 'Stavba druhe tretiny',
                    'Stavba druhe tretiny prazske obecni plynarny Michli', 'Stavba osady Baba', 'stavby na pisku',
                    'Stefan Drug', 'stembera miler', 'Stembera Mlcoch', 'Stepan Bohumil', 'stesti dam 1921',
                    'Stogr Josef', 'STRACH 1930', 'strelnice toyen', 'Strieborny prach', 'STROJOKRESBY', 'strojopis',
                    'strom 1924', 'Studenti ceka 1938', 'Studenti ceka laska smrt 1938', 'styl casopis', 'Styrskeho',
                    'Styrsky', 'suess', 'Sumavansky', 'Surrealistika fotografie', 'Suss', 'sutnar', 'Sutnara', 'Svab',
                    'Svacinova', 'Svandovo', 'Svatebcane na Eiffelce', 'Svet ktery voni', 'Svetlo vytvarne umeni dile',
                    'svetozor 1937', 'Svezte se nami', 'Svobodne zednarstvi 1924', 'Sylvestrovska noc',
                    'synteticka magie', 'szpyk', 'Tajemstvi hanzlik', 'Tajemstvi zivota energie hmoty',
                    'Tak mluvil Wolker', 'Tak zpivam', 'tanci svrcek', 'tarot', 'Tater Miroslav dobrodruh',
                    'Taut Bruno Nove bydleni', 'technik radi', 'Technik SSSR', 'Tegtmaierovy zelezarny', 'teige',
                    'Teinitzova', 'telehor', 'tezka noc hampl', 'Thea von Harbou metropolis', 'Theorie relativity 1923',
                    'tiche melodie', 'Tichy', 'Tille', 'tisnovsky', 'Tittelbach', 'Tmy svetla 1918',
                    'to by se nemohlo lewis', 'To nebylo nic 1948', 'tolstoj chleb', 'Torsa 1934', 'Toyen',
                    'Tragedie ruska', 'Tramp Eso', 'TRAMPOTY 1932', 'Tribuna', 'trn', 'trn 1968', 'Trojan Zvon zeme',
                    'Trosecnikem Parizi Londyne', 'Truksa', 'tschichold', 'Tschinkel', 'Tschinkl', 'Tusar', 'Tvar 1965',
                    'Tvrdosijni', 'TYPOGRAF SI ZPIVA', 'typoreklama', 'tyranie nebo laska', 'Ubu Kral',
                    'Ucebnice praktickeho porodnictvi', 'ucnovske', 'ucnovskych', 'Udel umelce Chalupecky',
                    'Umela intelligence', 'umelecky ctrnactidenik mladych', 'umelych nader', 'umeni bojujici',
                    'Umeni instalace 1994', 'UP zavody', 'Upir tolstoj', 'Uprava zarizeni moderni kancelare',
                    'Usmevy slz', 'uspory investice', 'Ustredni budova elektrickych podniku',
                    'Ustredni studentske knihkupectvi', 'Uvod do zemedelske statistiky', 'Uvod povahopisny', 'vachal',
                    'Vaclav Jiru', 'Vaclav Martinec', 'Vaclav Polivka', 'Valka vojaci 1930', 'Valoch', 'Vanco',
                    'Var 1922', 'Vasceari', 'Vazba nebo Svejk ve vazbe', 'Vceli obec', 've smeru uhlopricny',
                    'Vecere pro cely rok', 'Vecernice', 'Vecne pohyby', 'vedro na palete', 'veliky lyrik', 'Veraikon',
                    'verre', 'VESELY VYBOJ', 'Vety 1977', 'videni sedmera', 'vigilie hodine', 'Viktor Razek',
                    'Vira dobre dilo', 'Vitek havlicek', ' vitezny zivot', 'Vizualni poezie', 'Vl Orel',
                    'Vladimir Boudnik', 'Vladimir Karfik', 'Vladislav kvart', 'VLKODLACI RODINA', 'Vodnikova nevesta',
                    'Vokno', 'Voknoviny', 'volna myslenka', 'Vons', 'VORBEMERKUNGEN', 'vrh kostek', 'VSUP',
                    'Vteleni Pampylasovo', 'vyber zajimovosti', 'Vycpalek Ladislav',
                    'VYHLEDOVA KONCEPCE MESTSKE HROMADNE DOPRAVY', 'Vyhruzny kompas',
                    'VYPOCTY KONSTRUKCE CASTI STROJOVYCH', 'Vyrocna zprava SUR', 'vyrocni zprava', 'vystava 1929',
                    'VYSTAVA FOTOGRAFIE ODBORNIKU', 'vystava harmonickeho domova', 'Vystava hygieny',
                    'Vystava moderni zeny', 'Vystavba Slovenska', 'vystavni sin', 'vystrel na slepo', 'Vytvarna prace',
                    'Vytvarna vychova', 'vytvarne snahy', 'vzduch vody', 'Vzhuru do kosmu', 'vzornik', 'Wachsman',
                    'Waschmann', 'Weil barvy', 'white star line', 'wojkowicz', 'wybrane', 'Wybrane werse',
                    'Za severnim sluncem', 'zachrana podstaty lesu', 'Zahrada hrichu', 'zahrada obydli',
                    'Zahradni mesta nezamestnanych', 'Zahradnicek Jan Pokuseni smrti', 'Zakulisi novin', 'zal neumann',
                    'Zapadly svet', 'zapas Sokol', 'Zarizeni uprava moderni', ' Zasnouci vojak', 'Zastavene hodiny',
                    'Zastrelen na uteku', 'zastreny profil', 'zatloukal kriz', 'Zatmeni Prave Poledne',
                    'Zavaznost obecneho vzdelani', 'Zborov 1921', 'Zdenek Kudelka Brnenska', 'zdravem tele zdravy duch',
                    'zdravotnicka vystava', 'Ze dne na den Nalevka', 'Zelena zaba', 'zelenka', 'ZEME ALVARGONZALEZOVA',
                    'zena ktera milovala', 'Zena ve svetle', 'Zensky svet', 'Zive vteriny', 'Zivot 1925',
                    'zivot na dlani', 'zlate rouno klein', 'zlaty disk', ' zlom', ' Zmatene hlasy', 'ZNAKOVA PARTITURA',
                    'Zora', 'zpevy rusku', 'Zpravodaj Kezbybyl', 'Zpravy Komise pro soupis stavebnich',
                    'Zpravy pro soupis stavebnich umelecky', 'Zrno Gide 1933', 'ztracene deste', 'Zurivy reporter',
                    'Zverokruh']
        #classes are made to find the element on the web page
        self.allclasses = ['para grow alt-odd', 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 2, 10, 2, 2, 2, 11, 12, 13, 14, 15, 16, 15, 17]  # 19
        self.alltags1 = ['div', 'div', 'div', 'div', 'div', 'p', 'div', 'div', 'div', 'div', 'div', 'div', 'div', 'div',
                    'div', 'div', 'div', 'div', 'div',
                    'h2', 'div', 'div', 'div', '']
        self.alltags2 = ['h3', 'h3', 'h3', 'h3', 'h3', 'a', 'h3', 'h3', 'costum', 'costum', 'a', 'h3', 'h3', 'h3', 'h3',
                    'h3', 'a', 'costum', 'costum', 'costom', 'a', 'a', 'a', 'costom']
        #all of the websites that are being scaned
        self.webpages = ['http://antik-stafl.cz/', 'http://antikvariat.obchodsvitavy.cz/category.php?id_category=2', 'http://antikvariat-avion.cz/', 'http://antikvariatmorava.cz/', 'http://antikvariatpaseka.cz/obchod/novinky', 'http://antikvariat-prelouc.cz/', 'http://shop.kniharium.eu/', 'http://www.adplus.cz/katalog/novinky', 'http://www.antik-klariani.cz/products_new.html', 'http://www.antikopava.cz/prodej-knih/novinky', 'http://www.antikvakorunni75.cz/novinky-v-katalogu', 'http://www.antik-variat.cz/', 'http://www.antikvariat-atlas.cz/', 'http://www.antikvariat-bohumin.cz/cz/knihy/novinky-tydne-sobota/', 'http://www.antikvariatik.cz/index', 'http://www.antikvariatkamyk.cz/', 'http://www.antikvariatnachod.cz/produkt.phtml?kat=newest', 'http://www.antikvariat-olomouc.cz/cz-sekce-novinky.html', 'http://www.antikvariatperla.cz/?inst=katalog&met=seznam&knihkupectvi=2', 'http://www.antikvariat-praha.cz/nabidka.asp', 'http://www.antikvariat-smichov.cz/index.php?page=knihy&kategorie=&od=&vypis=0', 'http://www.antikvariat-susice.cz/index.php?typ=php&kategorie=novinky', 'http://www.antikvariatukostela.cz/cz-kategorie_447699-0-nove-pridane-knihy-nejlepsi-vanocni-darky.html', 'http://www.antikvariat-vltavin.cz/', 'http://www.antikvariaty.cz/', 'http://www.karelkrenek.com/news.php?lang=cz', 'http://www.knizky.com/index.php?Akce=Prove%EF&CenterFrame=hledej.php&LeftFrame=prohlmenu.php&order_id=7&order_dir=1', 'http://www.samota.cz/katonline/nov/nov.html', 'http://www.spalena53.cz/knihy/', 'http://www.valentinska.cz/home', 'https://www.antikvariat-divis.cz/cze/novinky', 'https://www.antikvariatchrudim.cz/', 'https://www.antikalfa.cz/bibliofilie/', 'http://antikvariat-bohemia.cz/', 'http://antikvariat-cypris.cz/novinky.php', 'https://aukro.cz/knihy-a-casopisy?sort=startingTime_DESC', 'http://www.antikvariat-benes.cz/antikvariat/901-novinky.html?rp', 'http://www.antikvariat-cejka.com/', 'http://www.antikvariatik.sk/?podstranka=novinky&zoradenie=&poradie=&start=0#index_obsah_vnutri_vysledky', 'http://www.antikvariat-janos.cz/', 'http://www.antikvariatkarlin.cz/', 'http://www.antikvariatpocta.cz/novinky', 'http://www.antikvariat-trutnov.com/novinky-dne', 'http://www.antikvariaty.com/auction/index.php', 'http://www.antikvariat-zlin.cz/', 'http://www.e-antikvariat.com', 'http://www.e-antikvariat.cz/', 'http://www.galerie-ilonka.cz/galerie-ilonka/eshop/9-1-Antikvariat', 'http://www.leonclifton.cz/novinky?page=0&amp;size=50', 'http://www.levnyantikvariat.cz/czech/', 'http://www.shioriantikvariat.cz/', 'http://www.tichyantikvariat.cz/index.php?pg=katalog&akce=katalog&kat=5', 'http://www.trigon-knihy.cz/', 'http://www.ztichlaklika.cz/antikvariat?page=1', 'https://antikvarium.cz/', 'https://www.artbook.cz/collections/akutalni-nabidka', 'http://www.antikvariat-delta.cz/Novinky-RIJEN-c45_0_1.htm', 'https://www.novemportis.cz/cs/', 'https://antikvariatelement.cz/novinky']


    def retrieve_all_products(self,soup,tag1,class1,tag2):
        found = []
        #geting website content

        if class1 == 1:
            all_products = soup.find_all(tag1, class_='para grow alt-odd')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())

        elif class1 == 2:
            all_products = soup.find_all(tag1, class_='para grow alt-odd')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())

            all_products = soup.find_all(tag1, class_='para grow alt-even')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())

        elif class1 == 3:
            all_products = soup.find_all(tag1, class_='gb-ilist gbox gleft1')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())
            all_products = soup.find_all(tag1, class_='gb-ilist gbox gleft2')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())
            all_products = soup.find_all(tag1, class_='gb-ilist gbox gright')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())

        elif class1 == 4:
            all_products = soup.find_all(tag1, class_='author-title')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())

        elif class1 == 5:
            all_products = soup.find_all(tag1, class_='kniha-left-rest')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())

        elif class1 == 6:
            all_products = soup.find_all(tag1, class_='articles_content')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())

        elif class1 == 7:
            all_products = soup.find_all(tag1, class_='main_item_text')
            for element in all_products:
                f = element.find('h3')
                found.append(f.get_text())
                f = element.find('p')
                found.append(f.get_text())
        elif class1 == 8:
            all_products = soup.find_all(tag1, class_='zaznam')
            for element in all_products:
                f = element.find('h3')
                found.append(f.get_text())
                f = element.find('h2')
                found.append(f.get_text())
                f = element.find('p')
                found.append(f.get_text())

        elif class1 == 9:
            all_products = soup.find_all(tag1, class_='kniha')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())
        elif class1 == 10:
            all_products = soup.find_all(tag1, class_='center_block')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())

        elif class1 == 11:
            all_products = soup.find_all(tag1, class_='right-block')
            for element in all_products:
                f = element.find(tag2)
                found.append(f.get_text())
        elif class1 == 12:
            all_products = soup.find_all(tag1, class_='node-inner')
            for element in all_products:
                f = element.find('h2')
                found.append(f.get_text())
            all_products = soup.find_all('span', class_='field-items')
            for element in all_products:
                f = element.find('span')
                found.append(f.get_text())

        elif class1 == 13:

            all_products = soup.find_all('div', class_='popis')
            for element in all_products:
                f = element.find('h3')
                found.append(f.get_text())
                f = element.find('h2')
                found.append(f.get_text())
        elif class1 == 14:
            all_products = soup.find_all('div', class_='over-field-h2')
            for element in all_products:
                f = element.find('h2')
                found.append(f.get_text())
            all_products = soup.find_all('span', class_='field-item autor')
            for element in all_products:
                f = element.find('a')
                found.append(f.get_text())
        elif class1 == 15:
            all_products = soup.find_all(tag1, class_='akce_foto')

            for element in all_products:
                f = element.find(tag2)


        return found




    def checkforkey(self,web):
        Hunted = []





        #look throw website content for matches
        for name in self.found:
            for key in self.keywords:
                if unidecode.unidecode(str(key).lower()) in unidecode.unidecode(str(name).lower()):
                    if name not in self.all:
                        Hunted.append('(text: '+str(name)+'), (Key: '+str(key)+'), (website: '+str(web)+')')

        #retrun all found elements
        return Hunted


    def main(self):
        #allclasses
        #1 => para grow alt-odd
        #2 => para grow alt-even + para grow grow alt-odd
        #3 => gb-ilist gbox gleft1 + gb-ilist gbox gleft2 + gb-ilist gbox gright
        #4 => author-title
        #5 => kniha-left-rest
        #6 => articles_content
        #7 => main_item_text
        #8 => zaznam
        #9 => kniha
        #10 => center_block
        #-----------------
        #11 => right-block
        #12 => author
        #13 => kniha(popis)
        #14 => title
        #15 => akce_foto
        #16 => productTitleContent


        print(len(self.alltags1))
        print(len(self.alltags2))
        print(len(self.allclasses))
        print('\n')
        print("                     #######################################################################")
        print("                                                 THE BOOK HUNTER ®                          ")
        print('                     #######################################################################')
        print('\n')
        print('Looking into: '+str(len(self.webpages))+' webpages')
        print('\n')
        index = 0
        #main loop
        for web in self.webpages:
            page = requests.get(web)
            soup = BeautifulSoup(page.content, 'html.parser')


            self.found = self.retrieve_all_products(soup,self.alltags1[self.index],self.allclasses[self.index],self.alltags2[self.index])
            Hunted = self.checkforkey(web)



            for element in Hunted:
                print(element)
                self.all.append(element)
            print('here')


            self.index = self.index+1

BookHunter = BookHunter()
BookHunter.main()