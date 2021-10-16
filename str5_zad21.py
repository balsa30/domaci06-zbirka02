"""
21. Na svoj jedanaesti rođendan, Harry Potter je saznao da nije običan dječak već da je pred
njim uspješna čarobnjačka karijera. U početku mu nije bilo lako jer nije znao ni neke
najobičnije stvari iz čarobnjačkog svijeta, kao npr., kako izgleda i koja je vrijednost novca
kojim se plaća u tom svijetu. Zato mu je Rubeus Hagrid objasnio kako stoje stvari u
čarobnjačkoj ekonomiji. On je rekao: „U čarobnjačkom svijetu sve se plaća u kovanicama.
Postoje tri vrste kovanica, zlatni galeoni, srebrni srpovi i bronzani knutovi i među njima
vrijedi sljedeći odnos: jedan galeon vrijedi sedamnaest srpova, a jedan srp dvadeset
devet knutova“. Napiši program koji za zadatu količinu galeona, srpova i knutova koju
Harry ima na svom računu štampa kolika je ukupna količina tog novca izražena u
knutovima. ULAZ: U jedinom redu ulaza nalaze se, odvojena razmakom, tri prirodna broja
G, S i K (0 ≤ G, S, K ≤ 50), gdje je G količina galeona, S količina srpova, a K broj knutova
na Harryjevom računu. IZLAZ: U jedini red izlaza štampati prirodan broj koji predstavlja
traženu količinu novca. 
"""


G,S,K = input('Unesite vrijednost galeona, srpova i knutova razdvojeno zarezima: ').split(',')
galeoni = int(G)
srpovi = int(S)
knutovi = int(K)

print(galeoni*17*29 + srpovi*29 + knutovi)