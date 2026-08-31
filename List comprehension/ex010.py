# duas listas diferentes em uma biblioteca
paises = ["Brasil", "Japão", "França"]
capitais = ["Brasília", "Tóquio", "Paris"]

mydict = {}
mydict = {pais:capital for pais,capital in zip(paises,capitais)}

print(mydict)