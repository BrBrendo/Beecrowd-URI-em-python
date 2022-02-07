n = int(input())
for i in range(n):
    palavra = input()
    palavra = palavra.lower()
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    d = dict()
    for i in alfabeto:
        d[i] = 0
    for i in range((len(palavra))):
        if(palavra[i] in d):
            d[palavra[i]] = d[palavra[i]] + 1
    pontuacao = []
    for i in d:
        pontuacao.append(d[i])
    maximo = max(pontuacao)
    frequentes = []
    for i in d:
        if(d[i] == maximo):
            frequentes.append(i)
    for i in range(len(frequentes)):
        if(i<(len(frequentes))):
            print("%s"%(frequentes[i]), end='')
    print()