import re

endereco = "Loteamento Nova Itabaiana 0, Sitio, Itabaiana, Paraiba, PB, 58360-000"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)


