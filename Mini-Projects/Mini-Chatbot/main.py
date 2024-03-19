dakhele = input('')
txt = dakhele.split()
kelmalowla=txt[0]
kelma2=txt[1]
l3ayba=''
chare7e={
'print':'hiya wa7ed fonctions katetba3e lk message ola variable ... liweste mnha fl terminal,example print("2020") atala3elina 2020 fterminal',
'print()':' hiya wa7ed fonctions katetba3e lk message ola variable ... liweste mnha fl terminal,example print("2020") atala3elina 2020 fterminal',
'commentere':'aya 7aja ketbti 9bele mnha # katssema comment o py maki direxe liha execusion b7al la makaynaxe',
'commentaire':'aya 7aja ketbti 9bele mnha # katssema comment o py maki direxe liha execusion b7al la makaynaxe',
'commente':'aya 7aja ketbti 9bele mnha # katssema comment o py maki direxe liha execusion b7al la makaynaxe',
'variable':'howa b7al wa7ed sandou9e katsstoka fih data(lma3loumate libaghi),bzxe declariha kate3tiha nichane smiya ,exemple: matixa = 80ryal ,kaynine bzaf dyal anwa3e dyal variables b7al entier (ra9eme sa7i7e mafihxe lfassila) string...',
'variables':'howa jame3e dyal variable b7al wa7ed sandou9e katsstoka fih data(lma3loumate libaghi),bzxe declariha kate3tiha nichane smiya ,exemple: matixa = 80ryal ,kaynine bzaf dyal anwa3e dyal variables b7al entier (ra9eme sa7i7e mafihxe lfassila) string...',
'variabl':'howa b7al wa7ed sandou9e katsstoka fih data(lma3loumate libaghi),bzxe declariha kate3tiha nichane smiya ,exemple: matixa = 80ryal ,kaynine bzaf dyal anwa3e dyal variables b7al entier (ra9eme sa7i7e mafihxe lfassila) string...',
'var':'howa b7al wa7ed sandou9e katsstoka fih data(lma3loumate libaghi),bzxe declariha kate3tiha nichane smiya ,exemple: matixa = 80ryal ,kaynine bzaf dyal anwa3e dyal variables b7al entier (ra9eme sa7i7e mafihxe lfassila) string...',
}

baxebda={
    'salam':'salam kine faxe n3awnek',
    'slm':'salam kine faxe n3awnek',
    'chra7e':f'{kelma2} {chare7e[kelma2]}',
    'chera7e':f'{kelma2} {chare7e[kelma2]}',
    'kifache':f'{kelma2} {chare7e[kelma2]}',
}
if kelmalowla in baxebda:
    print(baxebda[kelmalowla])