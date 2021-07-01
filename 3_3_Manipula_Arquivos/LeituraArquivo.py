with open("teste.txt","r") as arquivo:
    conteudo=arquivo.readlines()
print("Tipo de dado da variavel",type(conteudo))
print("Conteudo do arquivo:",conteudo)