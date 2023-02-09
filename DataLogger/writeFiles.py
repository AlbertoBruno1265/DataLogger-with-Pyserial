def create(arq):
    try:
        with open(arq, 'r', encoding='utf-8') as arquivo:
            arquivo.read()
    except:
        with open(arq, 'w', encoding='utf-8') as arquivo:
            arquivo.write('')
            print(f'O arquivo {arq} foi criado com sucesso!')


def write(arq, msg):
    from datetime import datetime
    try:
        with open(arq, 'a') as arquivo:
            arquivo.write(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> {msg}\n')
    except:
        with open(arq, 'a') as arquivo:
            print('ERRO! Linha ignorada!')
            arquivo.write(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> ERRO! Linha ignorada!\n')
