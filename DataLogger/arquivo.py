def criar(arq):
    try:
        with open(arq, 'r', encoding='utf-8') as arquivo:
            l = arquivo.read()
    except:
        with open(arq, 'w', encoding='utf-8') as arquivo:
            l = arquivo.write('')
        print(f'O arquivo {arq} foi criado com sucesso!')
    return l


def escrever(arq, msg):
    from datetime import datetime
    try:
        with open(arq, 'a') as arquivo:
            arquivo.write(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> {msg}\n')
    except:
        with open(arq, 'a') as arquivo:
            print('ERRO! Linha ignorada!')
            arquivo.write(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> ERRO! Linha ignorada!\n')