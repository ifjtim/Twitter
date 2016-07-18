Dokumentace ISJ
Stahovaní twittru
autor: Tomasz Koderla
login: xkonde03

O skriptu:
Skript je napsán v Python . Testoval jsem ho na mém notebooku Asus K50NI v operačním
systému Ubuntu 14.10 . Verze Python 2.7.8. Skript jsem spouštěl pomocí příkazu 'python twiter.py'

Knihovny:
V skriptu jsem použil externí knihovnu tweepy. Tato knihovna nám slouží pro komunikaci z
twittrem.

Twitter:
Můj skript stahuje twetty a retwetty od uživatele z názvem @zdrojak. Jeho twitty jsou
zaměřene na IT a problémy kolem ni.

Skript:
Skript je rozdělen na dvě části na část aktualizační a část stahovací. Stahovací část stáhne do
souboru posledních 50 twettu a do adresaře stranky_twiter stáhne všechny html odkazy jako
samostatné html soubory. Twetty se stáhnou do souboru twiter.txt ,které se řadi od nejaktuálnějších
po nejstarší twetty . Každý záznam twettu je formátovat: první řádek je id twittu na dalším řádku
text twittu a další řádce je odkaz na stránky které byly v textu stránek a pak je jako oddělovač
jednotlivých záznamu zvolen pas hvězdiček. Aktualizační mod z aktualizuje do posledního
záznamu který byl stáhnu (rozpozná to dle id twittu)t nebo 150 posledních twittu.

Měření:
K měření jsem použil program time. Jak jsem už výše uvedl měřeni bylo prováděno na mém
notebooku. Prováděl jsem několik zkoušek tady jsou vypsaná tři měření.
stahovací
real
user
sys
0m38.049s
0m0.576s
0m0.227s
real
user
sys
0m41.523s
0m0.559s
0m0.258s
real 0m44.735s
user 0m0.578s
sys 0m0.262s
aktualizační
real
user
sys
0m1.422s
0m0.171s
0m0.040s
real
user
sys
0m1.379s
0m0.162s
0m0.046s
real 0m12.944s
user 0m0.185s
sys 0m0.058s

Zavěr:
Při aktualizačním modu skript neměl o moc když bylo co aktualizovat než když nebylo co
aktualizovat.
