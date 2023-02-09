def create(files):
    try:
        with open(files, 'r', encoding='utf-8') as file:
            file.read()
    except:
        with open(files, 'w', encoding='utf-8') as file:
            file.write('')
            print(f'O arquivo {file} foi criado com sucesso!')


def write(files, msg):
    from datetime import datetime
    try:
        with open(files, 'a') as file:
            file.write(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> {msg}\n')
    except:
        with open(files, 'a') as file:
            print('ERRO! Linha ignorada!')
            file.write(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> ERRO! Linha ignorada!\n')
