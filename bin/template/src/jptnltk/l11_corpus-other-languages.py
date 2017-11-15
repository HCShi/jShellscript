#!/usr/bin/python3
# coding: utf-8
from nltk import corpus
print(corpus.cess_esp.words())  # ['El', 'grupo', 'estatal', 'Electricit\xe9_de_France', ...]
print(corpus.floresta.words())  # ['Um', 'revivalismo', 'refrescante', 'O', '7_e_Meio', ...]
print(corpus.indian.words('hindi.pos'))  # ['पूर्ण', 'प्रतिबंध', 'हटाओ', ':', 'इराक', 'संयुक्त', ...]
print(corpus.udhr.fileids())  # ['Abkhaz-Cyrillic+Abkh', 'Abkhaz-UTF8', 'Achehnese-Latin1', 'Achuar-Shiwiar-Latin1', 'Amahuaca-Latin1', ...]
print(corpus.udhr.words('Javanese-Latin1')[11:])  # ['Saben', 'umat', 'manungsa', 'lair', 'kanthi', 'hak', ...]
