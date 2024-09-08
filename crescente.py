def criar_arquivo():
     arq = open('crescente.txt', 'w')
     print(arq)
     arq.close()
     print('\n''Arquivo criado com sucesso!')

def criar_ordemcrescente():
     arq = open('crescente.txt', 'a')
     quantidade = 101
     for elemento in range(quantidade):
          arq.write(str(elemento)+'\n')
     arq.close()
criar_arquivo()
criar_ordemcrescente()
