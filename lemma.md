How to lemmatize polish words in python, like:
"bankomatów" → "bankomat", 
"pożyczki" → "pożyczka", etc.

Rather to reduce dimensionality i ML/NLP tasks !!!!! (not perfect, yet quite useful). 
Use simple mapping of word-lemma pair written in dictionary, based on IPAN web resources: "PoliMorf-0.6.7"

You can choose between TWO dicts:
lemma_dict_1 : 3,8 mln word-lemma pairs in dict
lemma_dict_2 : 5,4 mln word-lemma pairs in dict


Both lemma dicts ( lemma_dict_1 and lemma_dict_2 ) have:
changed negative form ('neg' tag) lemma adding "nie" to string, ex. : 

was originally: "niedekompensującego" → "dekompensować"

changed to:     "niedekompensującego" → "niedekompensować"
for about 480k pairs
some words tagged as name, surname, geo, etc., changed like below in table, ex. "Andrzej" → "xximię", "Pekao" → "xxorganizacja"

geograficzna	xxgeograficzna
nazwisko	xxnazwisko
imię	xximię
własna	xxwłasna
organizacja	xxorganizacja
Extended lemma_dict_2 can handle words without polish diacritic letters (ą, ć, ę, ł, ń, ó, ś, ź, ż), like: 
"bankomatow" -> "bankomat" (without "ó"),  "pozyczki" → "pożyczka" (without "ż"), etc.
in lemma_dict_1 it will leave originally written words, like others not included in a dict, ex.: "bankomatow" ->"bankomatow" ,"pozyczki" → "pozyczki"


Description:

ZNACZNIKI MORFOSYNTAKTYCZNE
===========================

Zestaw znaczników jest zbliżony do zestawu korpusu NKJP (www.nkjp.pl).

* adj - przymiotnik (np. „niemiecki”)
* adja - przymiotnik przyprzymiotnikowy (np. „niemiecko”, w wyrażeniach typu „niemiecko-chiński”)
* adjc - przymiotnik predykatywny (np. „ciekaw”, „dłużen”)
* adjp - przymiotnik poprzyimkowy (np. „niemiecku”)
* adv - przysłówek (np. „głupio”)
* burk - burkinostka (np. „Burkina Faso”)
* depr - forma deprecjatywna
* ger - rzeczownik odsłowny
* conj - spójnik łączący zdania współrzędne
* comp - spójnik wprowadzający zdanie podrzędne
* num - liczebnik
* pact - imiesłów przymiotnikowy czynny
* pant - imiesłów przysłówkowy uprzedni
* pcon - imiesłów przysłówkowy współczesny
* ppas - imiesłów przymiotnikowy bierny
* ppron12 - zaimek nietrzecioosobowy
* ppron3 - zaimek trzecioosobowy
* pred - predykatyw (np. „trzeba”)
* prep - przyimek
* siebie - zaimek "siebie"
* subst - rzeczownik
* verb - czasownik
* brev - skrót
* interj - wykrzyknienie
* qub - kublik (np. „nie” lub „tak”)

Atrybuty podstawowych form:

* sg / pl - liczba pojedyncza / liczba mnoga 
* nom - mianownik
* gen - dopełniacz
* acc - biernik
* dat - celownik
* inst - narzędnik
* loc - miejscownik
* voc - wołacz
* pos - stopień równy
* com - stopień wyższy
* sup - stopień najwyższy
* m1, m2, m3 - rodzaje męskie
* n1, n2 - rodzaje nijakie
* p1, p2, p3 - rodzaje rzeczowników mających tylko liczbę mnogą (pluralium tantum)
* f - rodzaj żeński
* pri - pierwsza osoba
* sec - druga osoba
* ter - trzecia osoba
* aff - forma niezanegowana
* neg - forma zanegowana
* refl - forma zwrotna czasownika
* nonrefl - forma niezwrotna czasownika
* refl.nonrefl - forma może być zwrotna lub niezwrotna
* perf - czasownik dokonany
* imperf - czasownik niedokonany
* imperf.perf - czasownik, który może występować zarówno jako dokonany, jak i jako niedokonany
* nakc - forma nieakcentowana zaimka (ppron lub siebie)
* akc - forma akcentowana zaimka
* praep - forma poprzyimkowa
* npraep - forma niepoprzyimkowa
* ger - rzeczownik odsłowny
* imps - forma bezosobowa
* impt - tryb rozkazujący
* inf - bezokolicznik
* fin - forma nieprzeszła
* bedzie - forma przyszła "być"
* praet - forma przeszła czasownika (pseudoimiesłów)
* pot - tryb przypuszczający [nie występuje w znacznikach NKJP]
* pun - skrót z kropką [za NKJP]
* npun - bez kropki [za NKJP] 
* wok / nwok: forma wokaliczna / niewokaliczna
