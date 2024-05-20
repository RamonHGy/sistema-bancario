def linha(tam=42):
    return '='*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('OPERAÇÕES BANCO')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opcao = int(input('Escolha uma opcao: '))
    return opcao